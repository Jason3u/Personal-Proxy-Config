"""Manually sync external rule snapshots using Python 3 and Git."""
import argparse,datetime,hashlib,json,re,subprocess,time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.request import Request,urlopen
ROOT=Path(__file__).resolve().parents[1]
MANIFEST=ROOT/'Stash/Rule/sources.json'
CLASSICAL={'DOMAIN','DOMAIN-SUFFIX','DOMAIN-KEYWORD','DOMAIN-WILDCARD','DOMAIN-REGEX','IP-CIDR','IP-CIDR6','IP-ASN','GEOIP','USER-AGENT','PROCESS-NAME','PROCESS-PATH','DST-PORT','NETWORK'}

def parse_payload(text,behavior):
    assert len(re.findall(r'^payload:\s*$',text,re.M))==1
    values=[]
    for raw in re.findall(r'^  - (.+)$',text,re.M):
        raw=raw.strip()
        if raw.startswith("'"):
            assert raw.endswith("'")
            value=raw[1:-1].replace("''", "'")
        elif raw.startswith('"'):
            value=json.loads(raw)
        else:
            value=raw
        assert value and not value.startswith(('*','&'))
        if behavior=='domain': assert ',' not in value
        else: assert value.split(',')[0] in CLASSICAL and len(value.split(','))>=2,value
        values.append(value)
    assert values
    return values

def latest_revision(item):
    repository,branch=item
    for attempt in range(3):
        try:
            result=subprocess.check_output(['git','-c','http.version=HTTP/1.1','ls-remote',f'https://github.com/{repository}.git','refs/heads/'+branch],text=True,timeout=30)
            revision=result.split()[0]
            assert re.fullmatch('[0-9a-f]{40}',revision)
            return item,revision
        except (subprocess.SubprocessError,IndexError):
            if attempt==2: raise
            time.sleep(1)

def fetch(item):
    name,entry=item
    revision=revisions[(entry['source_repository'],entry['source_branch'])]
    url=f"https://raw.githubusercontent.com/{entry['source_repository']}/{revision}/{entry['upstream_path']}"
    for attempt in range(3):
        try:
            with urlopen(Request(url,headers={'User-Agent':'Personal-Proxy-Config'}),timeout=30) as response:
                assert response.status==200
                data=response.read()
            break
        except Exception:
            if attempt==2: raise
            time.sleep(1)
    text=data.decode('utf-8-sig')
    original=parse_payload(text,entry['behavior'])
    modifications='none'
    if name=='Streaming':
        match=re.search(r'^  # TikTok\r?\n.*?(?=^  # [^ \r\n])',text,re.M|re.S)
        assert match,'Upstream TikTok section changed; existing snapshots preserved.'
        removed=parse_payload('payload:\n'+match.group(),'classical')
        text=text[:match.start()]+text[match.end():]
        data=(f'# Modified by Jason3u: removed the TikTok section ({len(removed)} rules).\n'+text).encode('utf-8')
        values=parse_payload(text,'classical')
        assert values==[r for r in original if r not in removed]
        modifications=f'Removed original TikTok section: {len(removed)} rules; all other payload entries and order preserved.'
    else: values=original
    return name,data,entry|{'source_url':url,'source_revision':revision,'rules':len(values),'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data),'modifications':modifications}

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source',help='Only sync this upstream repository')
    args=parser.parse_args()
    manifest=json.loads(MANIFEST.read_text(encoding='utf-8'))
    selected={n:e for n,e in manifest['rules'].items() if 'source_repository' in e and (not args.source or e['source_repository']==args.source)}
    assert selected,'No selected upstream rules.'
    identities=sorted({(e['source_repository'],e['source_branch']) for e in selected.values()})
    with ThreadPoolExecutor(max_workers=3) as pool: revisions=dict(pool.map(latest_revision,identities))
    # Validate every download before changing snapshots.
    with ThreadPoolExecutor(max_workers=5) as pool: snapshots=list(pool.map(fetch,selected.items()))
    for name,data,entry in snapshots:
        path=(ROOT/entry['path']).resolve()
        assert path.is_relative_to((ROOT/'Stash/Rule').resolve())
        path.write_bytes(data)
        manifest['rules'][name]=entry
    manifest['updated_at']=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))).isoformat(timespec='seconds')
    MANIFEST.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    readme=ROOT/'Stash/Rule/README.md'
    text=readme.read_text(encoding='utf-8')
    for name in selected:
        text=re.sub(r'^\| '+name+r' \| \d+ \|','| '+name+' | '+str(manifest['rules'][name]['rules'])+' |',text,flags=re.M)
    readme.write_text(text,encoding='utf-8')
    print(json.dumps({'rules':{n:e['rules'] for n,_,e in snapshots},'next':'Review git diff, then commit and push.'}))
