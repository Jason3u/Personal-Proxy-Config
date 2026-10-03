# Rule

| 规则 | 条数 | 类型 | 文件 |
| --- | ---: | --- | --- |
| X | 33 | classical | [X.yaml](X.yaml) |
| Telegram | 46 | classical | [Telegram.yaml](Telegram.yaml) |
| AI | 101 | classical | [AI.yaml](AI.yaml) |
| Crypto | 54 | classical | [Crypto.yaml](Crypto.yaml) |
| Adblock | 37692 | domain | [Adblock.yaml](Adblock.yaml) |
| Apple | 33 | classical | [Apple.yaml](Apple.yaml) |
| Google | 701 | classical | [Google.yaml](Google.yaml) |
| Microsoft | 670 | classical | [Microsoft.yaml](Microsoft.yaml) |
| WeChat | 31 | classical | [WeChat.yaml](WeChat.yaml) |
| OpenAI | 35 | classical | [OpenAI.yaml](OpenAI.yaml) |
| YouTube | 183 | classical | [YouTube.yaml](YouTube.yaml) |
| China | 30 | classical | [China.yaml](China.yaml) |
| Lan | 140 | classical | [Lan.yaml](Lan.yaml) |
| Streaming | 358 | classical | [Streaming.yaml](Streaming.yaml) |
| Global | 27110 | domain | [Global.yaml](Global.yaml) |
| APNs | 12 | classical | [APNs.yaml](APNs.yaml) |
| AppleProxy | 40 | classical | [AppleProxy.yaml](AppleProxy.yaml) |
| AppleMedia | 52 | classical | [AppleMedia.yaml](AppleMedia.yaml) |
| AppStore | 2 | classical | [AppStore.yaml](AppStore.yaml) |
| AppleID | 4 | classical | [AppleID.yaml](AppleID.yaml) |
| iCloud | 61 | classical | [iCloud.yaml](iCloud.yaml) |
| iCloudPrivateRelay | 6 | classical | [iCloudPrivateRelay.yaml](iCloudPrivateRelay.yaml) |
| SystemOTA | 78 | classical | [SystemOTA.yaml](SystemOTA.yaml) |
| TestFlight | 3 | classical | [TestFlight.yaml](TestFlight.yaml) |
| FindMy | 3 | classical | [FindMy.yaml](FindMy.yaml) |
| Siri | 1 | classical | [Siri.yaml](Siri.yaml) |
| AppleMail | 2 | classical | [AppleMail.yaml](AppleMail.yaml) |
| AppleDev | 40 | classical | [AppleDev.yaml](AppleDev.yaml) |
| AppleFirmware | 175 | classical | [AppleFirmware.yaml](AppleFirmware.yaml) |
| AppleHardware | 226 | classical | [AppleHardware.yaml](AppleHardware.yaml) |
| AppleTV | 8 | classical | [AppleTV.yaml](AppleTV.yaml) |
| AppleMusic | 10 | classical | [AppleMusic.yaml](AppleMusic.yaml) |
| AppleNews | 2 | classical | [AppleNews.yaml](AppleNews.yaml) |
| AppleDomain | 1560 | domain | [AppleDomain.yaml](AppleDomain.yaml) |

## 来源

- [blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script)：Adblock、Apple 系列、AppStore、iCloud、FindMy、Siri、SystemOTA、TestFlight、Google、Microsoft、WeChat、Telegram、OpenAI、X（Twitter）、YouTube、China、Lan。原文保留，许可证见 [GPL-2.0](../../Licenses/blackmatrix7-GPL-2.0.txt)。
- [ACL4SSR/ProxyMedia](https://github.com/ACL4SSR/ACL4SSR/blob/master/Clash/Providers/ProxyMedia.yaml)：Streaming，剔除原文标注的 TikTok 段共 10 条，其余规则及顺序保持不变；许可见 [LICENCE](../../Licenses/ACL4SSR-LICENCE.txt)。
- [Loyalsoldier/clash-rules](https://github.com/Loyalsoldier/clash-rules/tree/release)：Global，采用 proxy.txt 原文字节，按 domain/YAML 使用；许可见 [LICENSE](../../Licenses/Loyalsoldier-LICENSE.txt)。
- AI：保留原有 ddgksf2013 快照；Crypto：保留自己的合并清单。

具体来源、版本、获取时间与 SHA-256 见 [sources.json](sources.json)。主配置不直接使用第三方规则 URL。

没有 TikTok 专用规则集。Streaming 的 TikTok 段已删除；通用 Global 仍可能匹配相关域名，未添加额外的直连或拒绝规则。

APNs 是依据 [Stash 推送说明](https://stash.wiki/faq/ios-push-notifications) 和 [Apple 官方 APNs 网段](https://support.apple.com/en-us/102266) 整理的独立规则集，优先于 Apple 通用规则。苹果分流及启用步骤见 [Apple.md](../Apple.md)。
