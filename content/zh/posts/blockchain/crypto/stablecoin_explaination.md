---
title: "加密世界与现实世界的桥梁，稳定币的前世今生"
date: 2022-08-14T15:13:06+08:00
draft: true
tags: ["blockchain", "cryptocurrency", "stablecoin", "tether", "terra", "luna", "finance"]
categories: ["Develop"]
authors:
- "Arthur"
---

{{<audio src="audios/here_after_us.mp3" caption="《后来的我们 - 五月天》" >}}

## 前言

![stablecoin_page_photo](https://pseudoyu.oss-cn-hangzhou.aliyuncs.com/images/stablecoin_page_photo.jpg)

相信大家近几年对加密货币，尤其是比特币、以太坊等名词并不陌生，从一波一波的价格新高或是新低，到活跃在各类媒体的马斯克与“狗狗币”，再到前段时间沸沸扬扬的“Luna”崩盘，数字货币尽管规模不大，却已然是现今经济体系尤其是货币市场不可忽略的一部分了。

然而，加密货币的价格是如何变化的呢？其与现实世界的资产是如何交互的呢？其中的所谓“稳定币”又是怎么一回事呢？

本文将从原理、运行机制、商业模式等方面浅析一下加密货币中非常特殊的存在 —— 稳定币。

## 加密货币概述

![crypto_currency_bg](https://pseudoyu.oss-cn-hangzhou.aliyuncs.com/images/crypto_currency_bg.jpg)

加密货币是一种基于密码学、分布式系统等技术原理运作的一种货币形式与交易媒介。例如，Bitcoin 是在 2009 年由中本聪发明的一种加密货币，主要是为了反抗中心化的银行体系，因为其精巧的系统设计和安全性，价值也在迅速提升，与 ETH（以太坊区块链使用的代币）等热门数字资产共同构成了加密货币生态系统。

有别于腾讯的 “Q 币”或是少数派平台推出的“派币”等虚拟资产，加密货币是一种在不受中心化机构平台管理的基础上依旧具备价格度量、交易等功能的虚拟货币形式，其价格由市场决定的，更确切地说，其价值主要由资产持有者信任与市场中的购买意愿等决定的。然而，由于目前其依旧是一个很小规模的市场，极易受到各类因素影响，其价格具备极高的波动性与不可预测性。

加密货币可以通过区块链网络打破地域限制，在世界范围内快速流通，无需经历繁琐的购汇、国际转账等手续与高昂的手续费。然而，主流加密货币目前更多作为一种交易媒介及投资方式，而很难作为一种像是法定货币这样课用于真正的生产、消费等现实活动的稳定货币载体，毕竟没有人想一觉醒来自己的资产莫名缩水一半还无处说理。

随着区块链与加密货币生态持续发展，其不仅仅局限于投资用途，国际汇款、跨境贸易乃至日常交易使用等应用场景也逐渐涌现出了需求，那有没有一种方式能够兼具加密货币的便利与法定货币的稳定性呢？

稳定币（Stablecoin）即是基于这种需求诞生的一种解决方案。

## 稳定币

![stable_coin_bg](https://pseudoyu.oss-cn-hangzhou.aliyuncs.com/images/stable_coin_bg.jpg)

稳定币是一种特殊的加密货币，它能够与某种传统的法定货币（如美元、韩元等）挂钩，因为其与法币价格锚定而不是随着市场剧烈波动，因此常用于不同数字资产的一种避险方案、中转方案以及满足日常支付需求。稳定币能够在缓解价格波动的同时，保有数字货币安全、公开透明、可追溯、低费用等特征。

那么，既然没有政府与银行为其背书与调控，稳定币是如何与现实世界的法币锚定，也就是如何实现 Pegging 的呢？

### 分类

从锚定方式来看，稳定币可以分为以下两大类：

1. 抵押稳定币
2. 算法稳定币

#### 抵押稳定币

抵押稳定币通常是以既有的一些政府发行的法定货币为基础进行 1:1 锚定，每一枚稳定币的背后都有等值的法定货币进行抵押，从而保障其价值的相对恒定。如上文所述，加密货币的价格主要取决于持有者及市场的信任与信心决定的，因此，抵押稳定币通过与中心化的现实资产绑定来维持这种信心，从而维护其价值。

除了与法定货币锚定外，也可以与黄金、钻石、石油以及其他主流数字货币等价值载体锚定，减少价格的波动性。然而，因为这种方式依托于一些组织机构或联盟进行管理运营，一定程度上背离了去中心化的设计原则，也存在一定风险（如没有足够的抵押物），但总体来说是比较普适与稳定的解决方案。

例如，Tether 推出的 USDT 就是一种锚定美元的稳定币，他们持有与其发行的 USDT 等值的美元抵押，定期公布并接受相关机构审计以维持消费者的信任。它自 2015 年起运行至今，一直保持相对稳定，然而，一直有声音称其并未持有与流通的 USDT 等量的美元资产抵押，存在中心化风险。

此外，在 2022 年 5 月 Luna 崩盘（后续会讲到）之后，随着市场对稳定币的质疑，Tether 也经历了一场短暂的波动，从 1 美元降低至 95 美分，对整个加密市场都造成了很大的影响。尽管 Tether 背后的公司通过临时性应对措施（如提高提现门槛与手续费）恢复了锚定，依然暴露出了其依赖于市场信心与中心化公司调控能力的风险。

#### 算法稳定币

为了解决抵押稳定币的中心化问题，还有另一种方式，即算法稳定币。这是一种基于特定算法组成的机制运作的加密货币，无需抵押任何现实世界的资产，而是通过智能合约对货币流通量进行动态调整来实现价格锚定。

这是一种巧妙的解决方案，运作原理类似于一个去中心化的央行，根据市场的反馈来动态调整货币供应量，因为其是一种基于智能合约的方式，我们减少了对公司持有现实资产的依赖，极大减少了中心化风险。

然而，基于算法的稳定币在实际运作过程中易受一些外部影响，供应量调整也并不能完全保障其价格稳定，具备一定的风险，例如前段时间 Terra 发行的 LUNA 崩盘事件就是一个典型的例子。

## Terra 生态详解

Terra 是基于 Cosmos SDK 创建的区块链网络，采用了算法稳定币的模式，构筑了独特的生态系统。其发行了与美元、韩元、欧元等锚定的稳定币（分别为 UST、KRT 与 EUT），并通过弹性的货币供应量来保障价格稳定。其并没有使用美元抵押来维系价格，而是通过智能合约实现的调节算法来进行价格调控。

![terra_usd_high](https://pseudoyu.oss-cn-hangzhou.aliyuncs.com/images/terra_usd_high.png)

当 UST 价格高于现实美元价格时，算法会自动增加供应量，随着市场上 UST 流通量提高，价格自然会下降，直到与现实美元价格相等。

![terra_usd_low](https://pseudoyu.oss-cn-hangzhou.aliyuncs.com/images/terra_usd_low.png)

反之，当 UST 价格低于现实美元价格时，算法会自动减少供应量，随着市场上 UST 流通量减少，价格自然会提高，直到与现实美元价格相等。

LUNA 代币主要用于维持稳定币价格，提高 UST 供应量时，用户可以通过协议销毁一定数量的 LUNA 得到对应价值的 UST，卖出后可以获取一定收益；而降低 UST 供给量时，则可以通过低于 1 美元价值的 LUNA 代币购买 1 美元 UST，卖出后可以获取一定收益。

以上两种情况下 LUNA 的持有者都能通过价格差异获取一定收益，当越来越多人购买 UST 时，LUNA 的价格会上涨，激励持有者们更积极参与 Terra 生态系统的运作。

而为了吸引市场持有 LUNA，参与 Terra 生态，Terra 提供了两种协议，Mirror 与 Anchor。Mirror 协议让 Terra 用户可以通过 LUNA 与 UST 资产便捷地购买一些现实资产在生态中的映射用于投资，如黄金、证券、股票等；而 Anchor 则是提供了类似银行存款但更可观的利息收益。这两种协议的结合推动更多人参与到 Terra 生态并吸引了更多资产留存。

有了以上对 Terra 运作机制的了解，我们可以从算法调控的角度更好地理解 LUNA 崩盘事件。

2022 年 5 月 9 日，UST 由于市场波动等外部原因与美元锚定被打破，当天跌至约 0.72 美元。随着大家对 UST 价格的恐慌影响，大量用户开始挤兑 UST 代币；而 LUNA 也因为用户不断通过 UST 铸造，总量不断增加，价格随之不断下跌，再进一步引起恐慌，形成更大的价差，最终几乎归零。

## 总结

以上就是我们对加密货币，尤其是稳定币生态的概述，并对抵押稳定币与算法稳定币两种主要稳定币分类进行详细分析。加密世界是一个充满创新与挑战的领域，也依然处在发展早期，后续也将会对区块链技术原理、公链、智能合约、去中心化应用、DAO 等有趣的概念进行探索与讨论。

## 参考资料

> 1. [What Are Stablecoins?](https://www.gemini.com/cryptopedia/what-are-stablecoins-how-do-they-work)
> 2. [The not-so-stable coins: How Terra’s collapse is dragging down crypto markets](https://www.grid.news/story/technology/2022/05/12/the-not-so-stable-coins-how-terras-collapse-is-dragging-down-crypto-markets/)
> 3. [Tether Loses $1 Peg, Bitcoin Drops to 2020 Levels of Near $24K](https://www.coindesk.com/markets/2022/05/12/tether-loses-1-peg-bitcoin-drops-to-2020-levels-of-near-24k/)
> 4. [The Complete Beginner’s Guide to Stablecoins](https://99bitcoins.com/what-are-stablecoins/)
> 5. [Is Terra — whose LUNA coin is now at another all-time high — really where the smart money is?](https://forkast.news/what-is-terra-luna-stablecoin/)
> 6. [Terra Money: Stability and Adoption](https://assets.website-files.com/611153e7af981472d8da199c/618b02d13e938ae1f8ad1e45_Terra_White_paper.pdf)
> 7. [稳定币常识：什么是稳定币，它如何保护您的资金](https://paxful.com/university/zh/what-are-stablecoins-cn/)
> 8. [Luna 崩盘分析与启发](https://zhuanlan.zhihu.com/p/524447156)