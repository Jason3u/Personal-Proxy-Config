# Apple

主配置用远程规则集引用苹果服务，不在配置中展开域名列表。每份 BM7 文件保留上游原文，包含来源与许可证；AppleDomain 对应上游 Apple_Domain.yaml，补齐 Apple.yaml 中未包含的通用域名部分。

| 策略组 | 默认出口 | 内容 |
| --- | --- | --- |
| APNs | 英国伦敦 | iOS 系统推送；独立 IPv4 / IPv6 地址段与域名，优先于广告和 Apple 通用规则 |
| Apple | DIRECT | Apple ID、iCloud、查找、邮件、Siri、系统更新、固件、硬件站点及通用苹果服务 |
| AppleProxy | 英国伦敦 | App Store 商店接口、TestFlight、iCloud Private Relay 相关域名及 BM7 AppleProxy 清单 |
| AppleMedia | 英国伦敦 | Apple TV、Apple Music、Apple News 和 AppleMedia 清单 |

各组可以手动切换出口。商店接口走代理不表示全部下载 CDN 都走代理；通用下载与更新默认直连。媒体能否播放仍取决于账号、订阅和地区。Private Relay 分流不会自动启用该功能。

## 推送

Telegram 前台能收消息、后台没有通知时，需要分别检查 Telegram 连接和 iOS 的 APNs 长连接。按需连接用于保持或启动 VPN；它不能替代 APNs 分流和系统级 APNs 代理设置。

1. 导入更新后的私人配置，更新规则资源，确认 APNs 策略组选中英国伦敦，且节点可用。
2. 在 Stash 中启用 Apple 推送通知（APNs）相关的系统级代理选项。蜂窝网络下仅写分流规则可能仍不能稳定捕获推送流量。
3. 启用保持 Stash 开启，并确认按需连接未排除当前 Wi-Fi 或蜂窝网络。
4. 开关一次飞行模式，重建已有的 APNs 长连接。返回正常网络后锁屏，请另一个账号发送 Telegram 消息测试；Wi-Fi 和蜂窝网络分别测试。
5. 若仍不推送，检查 Stash 连接记录中的 push.apple.com 或 APNs 官方网段是否进入 APNs / 英国伦敦；同时核对 Telegram 与 iOS 通知权限、聊天静音和专注模式。

APNs 不加入 MitM 解密。配置只对 push.apple.com 及其子域名补充 fake-ip-filter，保留原 DNS 配置。

APNs 采用 Stash 官方建议的 3 条域名规则与 Apple 官方 9 个 IPv4 / IPv6 地址段，没有把整个 17.0.0.0/8 送入代理。官方建议中的 akadns.net 和 apple.com.edgekey.net 也可能覆盖部分 CDN 流量。

系统级 APNs 代理会让各应用推送依赖节点的可用性；节点不可用时，推送可能同时受影响。若个人热点或 CarPlay 出现问题，可暂时停用相关系统级代理选项排查。

配置引用的规则集由 Stash 按 interval 更新；本仓库的 BM7 快照由 Scripts/sync_bm7.py 手动同步。APNs 规则根据官方文档人工维护。配置语法和路由验证不能代替 iPhone 实际通知测试。

来源：[Stash 推送文档](https://stash.wiki/faq/ios-push-notifications)、[按需启动](https://stash.wiki/features/on-demand)、[Apple 官方 APNs 网络范围](https://support.apple.com/en-us/102266)、[BM7](https://github.com/blackmatrix7/ios_rule_script/tree/master/rule/Clash)。
