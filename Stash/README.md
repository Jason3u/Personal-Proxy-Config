# Stash

`Config/` 放脱敏的个人配置模板，`Rule/` 放本仓库提供的规则快照。私人可用配置保存于本机，不提交到 GitHub。

## 配置

默认节点名称为 `英国伦敦`。AI、Crypto、Telegram、X 分别通过一条 `RULE-SET` 引用自己的规则文件；策略组名 `Crypto` 替代原“交易行情”。规则顺序为内网直连、AI、Crypto、Telegram、X、国内 IP 直连、兜底。

模板中的节点字段都是占位符，需替换整个节点后导入。InternationalStreaming 暂保留策略组，未接入规则；Apple 分流未启用。

规则集合采用 `classical` / YAML，更新间隔 86400 秒，不设置自定义 `path`。规则集注册错误是否恢复仍需在 Stash iOS Build 1319 实测；本仓库不能替代手机启动验证。

## 规则说明

X 对应 BM7 的 Twitter 规则，文件内容和作者头保持不变。Telegram 原文包含 `PROCESS-NAME`，Stash iOS 会忽略进程规则；域名、IP、ASN 规则保留。

AI 原文包含共享云服务域名，且优先于其他业务规则，因此相关连接可能匹配 AI。Crypto 沿用自己的合并清单。

规则匹配从上到下，详见 [Stash 规则类型](https://stash.wiki/rules/rule-types) 和 [规则集合](https://stash.wiki/rules/rule-set)。
