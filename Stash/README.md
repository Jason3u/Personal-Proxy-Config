# Stash

`Config/` 放脱敏模板，`Rule/` 放本仓库的规则快照。私人节点保存在本机。

## 配置

34 个规则集通过自己的 GitHub Raw 链接调用，每类在 `rules` 中仅一行，不展开域名清单。国际媒体使用 Streaming（ACL4SSR）和 YouTube（BM7）；未设置 TikTok 专用分流，Streaming 内的 TikTok 段已剔除。

局域网直连置于最前，随后 APNs 推送走英国伦敦，再拦截广告、匹配 AI / OpenAI 与 Crypto，以及各项服务和通用国内/国外规则。国内网站默认 DIRECT，国外网站默认英国伦敦；Telegram、X、AI、Crypto 和 InternationalStreaming 保留独立策略组。

OpenAI 规则指向现有 AI 分组，不另建 AI 分组。Apple 服务按 APNs、Apple、AppleProxy、AppleMedia 四个策略组处理；具体服务及优先级见 [Apple.md](Apple.md)。Microsoft、WeChat、China 指向国内网站，Google、Global 指向国外网站。GEOIP 国内直连与 MATCH 国外兜底置于最后。

Adblock、Global 与 AppleDomain 使用 domain；其他使用 classical。全部为 YAML / HTTP 规则集，间隔 86400 秒，未指定缓存 path。原生启动与 APNs 推送仍需手机验证。

## 规则说明

第三方镜像保留来源与作者信息。AI 原文包含共享云服务域名，优先匹配的连接可能进入 AI 分组。BM7 的进程规则在 Stash iOS 会被忽略，其域名/IP/ASN 规则保留。

这是手动维护的仓库快照。`Scripts/sync_bm7.py` 同步已选择的 BM7 规则；Streaming 和 Global 可通过 `Scripts/sync_rules.py` 同步。更新脚本保留 Streaming 的 TikTok 排除策略。

官方文档：[规则类型](https://stash.wiki/rules/rule-types)、[规则集合](https://stash.wiki/rules/rule-set)。
