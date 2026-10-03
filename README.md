# Personal Proxy Config

个人代理配置与分流规则备份。当前主要维护 Stash；仓库名保持 `Proxy-Rules-Collection`，原有链接继续可用。

## 目录

```text
Stash/
  Config/Morin-stash.yaml   # 脱敏配置模板
  Rule/                    # AI、Crypto、X、Telegram 规则快照
    sources.json           # 来源、版本、规则数量、SHA-256
licenses/                  # 第三方规则许可证
scripts/sync_bm7.py         # 手动同步选中的 BM7 规则
clash/                     # 原有 Clash 规则，保留兼容
qx/                        # 原有 Quantumult X 规则，保留兼容
```

## 使用

下载 [Morin-stash 模板](Stash/Config/Morin-stash.yaml)，将 `proxies` 中的占位节点替换为自己的完整节点。仓库模板不能直接连通；私人节点、订阅与密钥仅保存在本机。

详细说明见 [Stash](Stash/README.md)，来源见 [规则清单](Stash/Rule/README.md)。规则存放在自己的仓库中，配置通过 GitHub Raw 引用，不把域名清单展开到主配置。

AI、Crypto、Telegram、X 已接入。Apple 不启用；流媒体等待选择，相关流量暂时使用通用分流与兜底。

## 维护与备份

规则是快照，客户端每天读取本仓库最新文件；这不代表本仓库自动跟随上游更新。BM7 规则可用 `python scripts/sync_bm7.py` 手动更新，检查差异后提交。AI 保留现有原文快照，Crypto 保留自己的合并规则。

Git 提交历史作为版本备份，可按提交恢复配置和规则。原 `clash/`、`qx/` 文件保持原内容，新配置统一引用 `Stash/Rule/`。仓库不启用定时同步。

## 来源

- [blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script)：X（Twitter）、Telegram；保留作者注释及 [GPL-2.0 许可证](licenses/blackmatrix7-GPL-2.0.txt)。
- [ddgksf2013 Ai.yaml](https://ddgksf2013.top/filter/Ai.yaml)：AI，保留先前复制的原文。
- 本仓库原 `clash/Trading.yaml`：Crypto；合并 Binance、OKX、Bybit、Bitget、Gate、Cornix、Fomo、TradingView。
- [jnlaoshu/MySelf](https://github.com/jnlaoshu/MySelf)：参考目录组织方式，未复制其配置或 Apple 文件。

第三方文件保留其各自作者和许可；BM7 许可证适用于对应的规则镜像，不替换其他来源的许可。
