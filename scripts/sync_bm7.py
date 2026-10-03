"""Manually refresh the selected BM7 snapshots; requires Python 3 and Git."""
import datetime
import hashlib
import json
import re
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'Stash/Rule/sources.json'
SELECTED = {'X':'Twitter/Twitter.yaml', 'Telegram':'Telegram/Telegram.yaml'}
ALLOWED = {'DOMAIN','DOMAIN-SUFFIX','DOMAIN-KEYWORD','IP-CIDR','IP-CIDR6','IP-ASN','PROCESS-NAME'}

def download(item):
    name, suffix = item
    url = f'https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/{revision}/rule/Clash/{suffix}'
    with urlopen(Request(url, headers={'User-Agent':'Personal-Proxy-Config'}), timeout=30) as response:
        contents = response.read()
    text = contents.decode('utf-8-sig')
    assert len(re.findall(r'^payload:\s*$', text, re.M)) == 1, name
    rules = re.findall(r'^  - (.+)$', text, re.M)
    assert rules, name
    for rule in rules:
        fields = rule.split(',')
        assert fields[0] in ALLOWED and len(fields) in {2,3}, rule
        assert len(fields) == 2 or fields[-1] == 'no-resolve', rule
    return name, url, contents, len(rules)

def latest_revision():
    last_error = None
    for attempt in range(3):
        try:
            result = subprocess.check_output(['git','-c','http.version=HTTP/1.1','ls-remote','https://github.com/blackmatrix7/ios_rule_script.git','refs/heads/master'],text=True,timeout=30)
            return result.split()[0]
        except (subprocess.SubprocessError, IndexError) as error:
            last_error = error
            if attempt < 2:
                time.sleep(1)
    raise RuntimeError('Unable to read upstream revision; existing snapshots were preserved.') from last_error

if __name__ == '__main__':
    revision = latest_revision()
    assert re.fullmatch(r'[0-9a-f]{40}', revision)
    manifest = json.loads(MANIFEST.read_text(encoding='utf-8'))
    # Download and validate both sources before replacing any file.
    with ThreadPoolExecutor(max_workers=2) as pool:
        snapshots = list(pool.map(download, SELECTED.items()))
    for name, url, contents, count in snapshots:
        entry = manifest['rules'][name]
        (ROOT / entry['path']).write_bytes(contents)
        entry.update(source_url=url, source_revision=revision, rules=count,
                     sha256=hashlib.sha256(contents).hexdigest(), modifications='none')
    manifest['updated_at'] = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))).isoformat(timespec='seconds')
    MANIFEST.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    readme = ROOT / 'Stash/Rule/README.md'
    text = readme.read_text(encoding='utf-8')
    for name in SELECTED:
        text = re.sub(r'^\| '+name+r' \| \d+ \|', '| '+name+' | '+str(manifest['rules'][name]['rules'])+' |', text, flags=re.M)
    readme.write_text(text,encoding='utf-8')
    print(json.dumps({'revision':revision,'rules':{name:count for name,_,_,count in snapshots},'next':'Review git diff, then commit and push.'}))
