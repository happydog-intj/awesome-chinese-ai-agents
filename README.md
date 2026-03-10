# Awesome Chinese AI Agents 🤖🇨🇳

<div align="center">

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![GitHub stars](https://img.shields.io/github/stars/happydog-intj/awesome-chinese-ai-agents?style=social)](https://github.com/happydog-intj/awesome-chinese-ai-agents)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**最全面的中文 AI Agent 资源库** - 为中文开发者打造的 AI Agent 工具、技能、文档和最佳实践合集

[English](README_EN.md) | 简体中文

</div>

---

## 📖 目录

- [🌟 精选项目](#-精选项目)
- [🛠️ 开发工具](#️-开发工具)
- [🎯 Agent 技能](#-agent-技能)
  - [通用技能](#通用技能)
  - [中文特色技能](#中文特色技能)
  - [营销与运营](#营销与运营)
  - [开发与DevOps](#开发与devops)
- [💬 对话平台集成](#-对话平台集成)
- [📚 中文文档与教程](#-中文文档与教程)
- [🎨 提示词库](#-提示词库)
- [🔌 中国服务API集成](#-中国服务api集成)
- [📊 实战案例](#-实战案例)
- [🌐 社区资源](#-社区资源)
- [🤝 贡献指南](#-贡献指南)

---

## 🌟 精选项目

### AI Agent 框架

- **[OpenClaw](https://github.com/openclaw/openclaw)** - 最流行的开源 AI Agent 框架 (293K+ ⭐)
  - 完整的中文文档
  - 支持微信、钉钉、飞书集成

- **[NanoClaw](https://github.com/qwibitai/nanoclaw)** - 轻量级 AI Agent 框架 (21K+ ⭐)
  - 原生支持 WhatsApp、Telegram
  - 内置调度任务和记忆系统
  - TypeScript 编写,易于二次开发

- **[AutoGen](https://github.com/microsoft/autogen)** - 微软开源的多 Agent 对话框架
  - 中文文档完善
  - 支持多 Agent 协作
  - 丰富的示例代码

- **[LangChain](https://github.com/langchain-ai/langchain)** - 最流行的 LLM 应用开发框架
  - 官方中文文档
  - 庞大的中文社区
  - 海量的中文教程

- **[MetaGPT](https://github.com/geekan/MetaGPT)** - 多 Agent 元编程框架 (中国团队)
  - 完全中文支持
  - 软件公司级别的协作
  - 自动生成PRD、设计文档、代码

### 中文原生 AI Agent

- **[ChatGLM-6B](https://github.com/THUDM/ChatGLM-6B)** - 清华开源的中文对话模型
  - 针对中文优化
  - 可本地部署
  - 适合私有化场景

- **[Qwen-Agent](https://github.com/QwenLM/Qwen-Agent)** - 阿里巴巴通义千问 Agent 框架
  - 完整的中文文档
  - 官方技术支持
  - 与通义千问深度集成

---

## 🛠️ 开发工具

### CLI 工具

- **[agent-browser](https://github.com/vercel-labs/agent-browser)** - AI Agent 浏览器自动化工具 (20K+ ⭐)
  - 支持中文网页交互
  - Rust 编写,性能强劲
  - 易于集成到 Agent 中

- **[skills](https://github.com/vercel-labs/skills)** - Agent 技能管理工具
  - `npx skills` 一键安装
  - 支持技能市场
  - 中文技能不断增加

### 开发框架

- **[LangGraph](https://github.com/langchain-ai/langgraph)** - 构建有状态的 Agent 工作流
  - 可视化工作流编辑
  - 中文示例丰富
  - 与 LangChain 无缝集成

- **[CrewAI](https://github.com/joaomdmoura/crewAI)** - 角色扮演型多 Agent 协作框架
  - 简单易用的中文配置
  - 适合团队协作场景
  - 丰富的预设角色

### 测试与调试

- **[LangSmith](https://smith.langchain.com/)** - LLM 应用监控平台
  - 实时追踪 Agent 执行
  - 中文界面
  - 性能分析

- **[Prompt Flow](https://github.com/microsoft/promptflow)** - 微软的 LLM 应用开发套件
  - 可视化 Prompt 调试
  - 中文文档
  - VS Code 插件

---

## 🎯 Agent 技能

### 通用技能

#### 文本处理

- **文档解析与摘要**
  - PDF/Word/Excel 文档解析
  - 智能摘要生成
  - 多语言翻译(中英互译)
  - 文档格式转换

- **内容创作**
  - 文章写作助手
  - 营销文案生成
  - 小红书文案生成器
  - 公众号排版助手

#### 数据分析

- **数据可视化**
  - 自动生成图表
  - 数据报告生成
  - Pandas/NumPy 代码生成
  - Excel 自动化

- **网页抓取**
  - 中文网站爬虫
  - 反爬虫策略处理
  - 数据清洗与结构化
  - 定时监控与告警

### 中文特色技能

#### 社交媒体自动化

- **微信生态**
  - 微信公众号自动发文
  - 企业微信机器人
  - 微信群聊机器人
  - 朋友圈自动发布

- **抖音/快手**
  - 视频文案生成
  - 评论自动回复
  - 数据分析与报告
  - 热点追踪

- **小红书**
  - 笔记自动生成
  - 标签推荐
  - 爆款文案分析
  - 达人数据监控

- **微博**
  - 热搜追踪
  - 自动转发评论
  - 舆情监控
  - 粉丝互动

#### 电商平台

- **淘宝/天猫**
  - 商品标题优化
  - 详情页文案生成
  - 客服自动回复
  - 订单数据分析

- **拼多多**
  - 价格监控
  - 竞品分析
  - 自动改价策略
  - 评价管理

- **京东**
  - 库存监控
  - 促销活动分析
  - 物流追踪
  - 售后处理

#### 办公协作

- **钉钉**
  - 钉钉机器人
  - 审批流程自动化
  - 考勤统计
  - 日报周报生成

- **飞书**
  - 飞书机器人
  - 文档协作
  - 日程管理
  - 会议纪要生成

- **企业微信**
  - 客户管理
  - 群发消息
  - 数据统计
  - CRM集成

### 营销与运营

#### 增长黑客

- **SEO优化**
  - 中文关键词研究
  - 百度SEO优化
  - 内容优化建议
  - 竞品分析

- **SEM投放**
  - 百度广告优化
  - 关键词出价建议
  - A/B测试分析
  - ROI计算

- **内容营销**
  - 爆款内容分析
  - 选题推荐
  - 发布时间优化
  - 数据追踪

#### 用户运营

- **用户增长**
  - 裂变活动策划
  - 拉新文案生成
  - 增长漏斗分析
  - 用户分层

- **用户留存**
  - 流失预警
  - 召回策略
  - 个性化推荐
  - 社群运营

### 开发与DevOps

#### 代码辅助

- **中文代码生成**
  - 根据中文描述生成代码
  - 代码注释中文化
  - API文档生成
  - 单元测试生成

- **代码审查**
  - 中文代码审查报告
  - 安全漏洞检测
  - 性能优化建议
  - 最佳实践检查

#### 运维自动化

- **监控告警**
  - 服务器监控
  - 日志分析
  - 异常检测
  - 告警处理(中文通知)

- **CI/CD**
  - 自动化部署
  - 构建优化
  - 测试报告生成
  - 发布笔记生成

---

## 💬 对话平台集成

### 即时通讯

| 平台 | 集成难度 | 文档质量 | 推荐工具 |
|------|---------|---------|---------|
| **微信** | ⭐⭐⭐⭐ | ⭐⭐⭐ | [WeChaty](https://github.com/wechaty/wechaty) |
| **企业微信** | ⭐⭐⭐ | ⭐⭐⭐⭐ | [企业微信SDK](https://developer.work.weixin.qq.com/) |
| **钉钉** | ⭐⭐ | ⭐⭐⭐⭐⭐ | [钉钉开放平台](https://open.dingtalk.com/) |
| **飞书** | ⭐⭐ | ⭐⭐⭐⭐⭐ | [飞书开放平台](https://open.feishu.cn/) |
| **Telegram** | ⭐ | ⭐⭐⭐⭐⭐ | [Telegraf](https://github.com/telegraf/telegraf) |
| **WhatsApp** | ⭐⭐⭐ | ⭐⭐⭐⭐ | [whatsapp-web.js](https://github.com/pedroslopez/whatsapp-web.js) |

### 社交媒体

- **微博开放平台** - [官方文档](https://open.weibo.com/)
- **小红书开放平台** - [官方文档](https://open.xiaohongshu.com/)
- **抖音开放平台** - [官方文档](https://open.douyin.com/)
- **快手开放平台** - [官方文档](https://open.kuaishou.com/)

---

## 📚 中文文档与教程

### 官方文档翻译

- **[LangChain 中文文档](https://python.langchain.com.cn/)** - 完整的中文翻译
- **[OpenAI 中文文档](https://openai.xiniushu.com/)** - 社区维护
- **[Anthropic Claude 中文指南](https://claude.ai/docs/zh)** - 官方中文版
- **[Hugging Face 中文课程](https://huggingface.co/learn/nlp-course/zh-CN)** - 免费在线课程

### 视频教程

- **B站搜索关键词**: "AI Agent 教程", "LangChain 实战", "大模型应用开发"
- **推荐UP主**:
  - [@吴恩达深度学习](https://space.bilibili.com/1567748478)
  - [@李沐](https://space.bilibili.com/1567748478)
  - [@跟李沐学AI](https://space.bilibili.com/1567748478)

### 博客文章

- **[知乎 - AI Agent 话题](https://www.zhihu.com/topic/20436836)** - 高质量讨论
- **[掘金 - AI Agent 标签](https://juejin.cn/tag/AI%20Agent)** - 技术文章
- **[CSDN - AI Agent 专栏](https://blog.csdn.com/nav/ai)** - 实战教程

### 书籍推荐

- 《大模型应用开发实战》
- 《LangChain 实战指南》
- 《AI Agent 设计模式》
- 《ChatGPT 提示工程》

---

## 🎨 提示词库

### 通用提示词

```markdown
#### 角色扮演

你是一位资深的{角色},拥有{经验年限}年的{领域}经验。
你的任务是帮助用户{目标},需要注意以下要点:
1. {要点1}
2. {要点2}
3. {要点3}

请使用专业但易懂的中文进行回答。
```

### 中文写作

```markdown
#### 小红书笔记生成

请根据以下信息生成一篇小红书笔记:
- 主题: {主题}
- 关键词: {关键词1}, {关键词2}, {关键词3}
- 风格: {风格}(如: 种草/测评/教程)
- 字数: {字数}

要求:
1. 标题吸引眼球,包含emoji
2. 开头引起共鸣
3. 内容有价值,有干货
4. 结尾有互动引导
5. 合理使用emoji和排版
6. 添加5-10个相关标签
```

### 营销文案

```markdown
#### 广告文案生成

产品/服务: {产品名称}
目标用户: {用户画像}
核心卖点: {卖点1}, {卖点2}, {卖点3}
文案类型: {类型}(如: 朋友圈/海报/短视频)

请生成3个版本的文案,每个版本风格不同:
1. 理性说服型
2. 情感共鸣型
3. 幽默娱乐型

每个文案包含:
- 标题(20字以内)
- 正文(根据类型调整长度)
- Call-to-Action
```

### 技术文档

```markdown
#### API文档生成

请根据以下代码生成完整的中文API文档:

{粘贴代码}

文档应包含:
1. 功能描述
2. 参数说明(类型、必填、默认值、示例)
3. 返回值说明
4. 使用示例
5. 注意事项
6. 常见错误及解决方案
```

---

## 🔌 中国服务API集成

### 支付

- **微信支付** - [官方文档](https://pay.weixin.qq.com/wiki/doc/api/index.html)
- **支付宝** - [官方文档](https://opendocs.alipay.com/open)
- **银联支付** - [官方文档](https://open.unionpay.com/)

### 地图导航

- **高德地图API** - [官方文档](https://lbs.amap.com/)
- **百度地图API** - [官方文档](https://lbsyun.baidu.com/)
- **腾讯地图API** - [官方文档](https://lbs.qq.com/)

### 短信/邮件

- **阿里云短信** - [官方文档](https://help.aliyun.com/product/44282.html)
- **腾讯云短信** - [官方文档](https://cloud.tencent.com/document/product/382)
- **网易云邮件** - [官方文档](https://www.163yun.com/help/documents/15588062314858496)

### 身份验证

- **手机号验证** - 阿里云/腾讯云号码认证服务
- **身份证OCR** - 百度AI/腾讯云/阿里云
- **人脸识别** - Face++ / 腾讯云 / 阿里云

### 存储

- **阿里云OSS** - [官方文档](https://help.aliyun.com/product/31815.html)
- **腾讯云COS** - [官方文档](https://cloud.tencent.com/document/product/436)
- **七牛云存储** - [官方文档](https://developer.qiniu.com/)

---

## 📊 实战案例

### 案例1: 微信客服机器人

**场景**: 电商公司需要24小时自动回复客户咨询

**技术栈**:
- WeChaty (微信接入)
- LangChain (对话管理)
- 通义千问 (LLM)
- Redis (会话存储)

**功能**:
- 自动回复常见问题
- 订单查询
- 物流跟踪
- 人工客服转接

**代码**: [查看完整实现](examples/wechat-customer-service/)

---

### 案例2: 小红书内容运营助手

**场景**: 品牌方需要批量生成小红书内容并监控数据

**技术栈**:
- OpenClaw (Agent框架)
- Claude Sonnet (内容生成)
- 小红书API (内容发布)
- Google Sheets (数据管理)

**功能**:
- 根据关键词生成笔记
- 自动添加标签和emoji
- 定时发布
- 数据监控与分析

**代码**: [查看完整实现](examples/xiaohongshu-content-agent/)

---

### 案例3: 自动化SEO优化工具

**场景**: SEO团队需要批量优化网站内容

**技术栈**:
- Python
- LangChain
- 百度搜索API
- 站长工具API

**功能**:
- 关键词研究
- 内容优化建议
- 竞品分析
- 排名监控

**代码**: [查看完整实现](examples/seo-automation/)

---

## 🌐 社区资源

### 中文社区

- **[AI研习社](https://www.yanxishe.com/)** - AI技术交流社区
- **[Paper With Code](https://paperswithcode.com/)** - 论文与代码
- **[知乎 - 人工智能话题](https://www.zhihu.com/topic/19551275)** - 高质量讨论
- **[掘金 - AI标签](https://juejin.cn/tag/AI)** - 技术文章分享

### 微信群/Discord

- 加入我们的微信交流群: [扫码加入](images/wechat-group-qr.png)
- Discord服务器: [点击加入](https://discord.gg/awesome-chinese-ai-agents)
- Telegram群组: [点击加入](https://t.me/awesome_chinese_ai_agents)

### 定期活动

- **每周直播**: 周三晚8点,分享最新技术
- **月度Meetup**: 线下技术交流
- **黑客松**: 季度一次,奖金丰厚

---

## 🤝 贡献指南

我们欢迎所有形式的贡献!

### 如何贡献

1. Fork 本项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开Pull Request

### 贡献内容

你可以贡献:
- 📝 新的资源链接
- 🔧 新的工具推荐
- 📚 教程和文档
- 💡 实战案例
- 🐛 修复错误
- 🌐 翻译内容

### 格式规范

添加新资源时,请遵循以下格式:

```markdown
- **[项目名称](项目链接)** - 简短描述 (可选: stars数量)
  - 特点1
  - 特点2
```

---

## 📊 项目统计

- 📚 收录资源: **150+**
- 🛠️ 开发工具: **30+**
- 🎯 Agent技能: **80+**
- 💬 平台集成: **15+**
- 📖 教程文档: **50+**
- 🔌 API集成: **25+**

---

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=happydog-intj/awesome-chinese-ai-agents&type=Date)](https://star-history.com/#happydog-intj/awesome-chinese-ai-agents&Date)

---

## 📄 License

本项目采用 [MIT License](LICENSE)

---

## 💖 致谢

感谢所有贡献者的付出! 🎉

特别感谢以下项目和组织:
- [OpenClaw](https://github.com/openclaw/openclaw)
- [LangChain](https://github.com/langchain-ai/langchain)
- [Anthropic](https://www.anthropic.com/)
- [阿里云通义千问](https://tongyi.aliyun.com/)

---

## 🔗 相关项目

- [Awesome AI Agents](https://github.com/e2b-dev/awesome-ai-agents) - 英文版AI Agent资源
- [Awesome LLM Apps](https://github.com/Shubhamsaboo/awesome-llm-apps) - LLM应用集合
- [Awesome ChatGPT Prompts ZH](https://github.com/PlexPt/awesome-chatgpt-prompts-zh) - 中文ChatGPT提示词

---

<div align="center">

**如果这个项目对你有帮助,请给我们一个 ⭐️!**

Made with ❤️ by Chinese AI Community

</div>
