# Awesome Chinese AI Agents 🦞🤖

> *为什么是小龙虾 🦞?* 因为 OpenClaw = Open + Claw(钳子),所以大家都叫它"小龙虾",开发 AI Agent 就是"养小龙虾"!

<div align="center">

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![GitHub stars](https://img.shields.io/github/stars/happydog-intj/awesome-chinese-ai-agents?style=social)](https://github.com/happydog-intj/awesome-chinese-ai-agents)
[![GitHub forks](https://img.shields.io/github/forks/happydog-intj/awesome-chinese-ai-agents?style=social)](https://github.com/happydog-intj/awesome-chinese-ai-agents/fork)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/happydog-intj/awesome-chinese-ai-agents)](https://github.com/happydog-intj/awesome-chinese-ai-agents/issues)
[![GitHub contributors](https://img.shields.io/github/contributors/happydog-intj/awesome-chinese-ai-agents)](https://github.com/happydog-intj/awesome-chinese-ai-agents/graphs/contributors)
[![Last commit](https://img.shields.io/github/last-commit/happydog-intj/awesome-chinese-ai-agents)](https://github.com/happydog-intj/awesome-chinese-ai-agents/commits/main)

**最全面的中文 AI Agent 资源库** - 为中文开发者打造的 AI Agent 工具、技能、文档和最佳实践合集

[English](README_EN.md) | 简体中文

[⭐ Star](https://github.com/happydog-intj/awesome-chinese-ai-agents) · [🐛 Report Bug](https://github.com/happydog-intj/awesome-chinese-ai-agents/issues/new?template=bug_report.md) · [💡 Request Feature](https://github.com/happydog-intj/awesome-chinese-ai-agents/issues/new?template=add_resource.md)

</div>

## ✨ 项目亮点

- 🎯 *专注中文生态* - 收录专门适配中文场景的 AI Agent 资源
- 🔥 *真实可用* - 所有项目均为真实存在、可直接使用的开源项目
- 📈 *持续更新* - 紧跟中文 AI Agent 领域最新动态
- 🌟 *精选推荐* - 按 GitHub Star 数和社区活跃度筛选优质资源
- 💡 *实战导向* - 包含完整的实战案例和最佳实践
- 🤝 *社区驱动* - 欢迎所有开发者贡献和完善

## 📊 资源统计

- 🔥 *Agent Harness*: 10+ (Claude Code、Codex、Gemini CLI、Hermes Agent 等) **🆕**
- 🔧 *AI Agent 框架*: 26+ **🆕**
- 🤖 *中文 LLM*: 10+
- 🛠️ *开发工具*: 38+ **🆕**
- 💬 *平台集成*: 10+ (微信、飞书、抖音、小红书等) **🆕**
- 📚 *学习资源*: 28+ **🆕**
- 🎨 *提示词模板*: 15+
- 📊 *实战案例*: 6+ **🆕**
- 🔌 *中国服务 API*: 30+

> 🗓️ **最近更新**：2026-05-01 - 新增 Hermes Agent、nanobot、browser-use、AstrBot、TradingAgents、hello-agents 等 8 个热门项目

---

## 📖 目录

- [🔥 Agent Harness -- 让 AI 直接写代码](#-agent-harness--让-ai-直接写代码) ⬅️ **新增置顶**
- [🚀 快速开始](#-快速开始)
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
- [❓ 常见问题速查](#-常见问题速查)
- [💡 最佳实践](#-最佳实践)
- [🤝 贡献指南](#-贡献指南)

---

## 🔥 Agent Harness -- 让 AI 直接写代码

> **什么是 Agent Harness？**
> Harness（执行框架）是让 AI Agent **直接操控编码工具**的调度层 -- 不只是生成代码建议，而是真正打开编辑器、读写文件、跑测试、提 PR，全流程自动完成。

### 🎯 核心概念

| 概念 | 说明 |
|------|------|
| **Harness** | Agent 的"身体"--与代码工具（Claude Code、Codex、Gemini CLI 等）交互的执行层 |
| **ACP 协议** | Agent Control Protocol，OpenClaw 用于调度 Harness 的标准接口 |
| **Coding Agent** | 在 Harness 中运行的代码智能体，可自主规划、编写、调试代码 |
| **Session** | 每次 Harness 调用的独立上下文，支持一次性（run）和持久（session）两种模式 |

### 🚀 主流 Agent Harness 对比

| Harness | 背后模型 | 适用场景 | 中文支持 | 开源 |
|---------|---------|---------|---------|------|
| **[Claude Code](https://github.com/anthropics/claude-code)** | Claude 3.5/3.7 | 全流程代码任务、复杂重构 | ✅ 中文指令友好 | 部分开源 |
| **[Codex CLI](https://github.com/openai/codex)** | GPT-4o / o3 | 终端命令、脚本生成 | ✅ | ✅ 开源 |
| **[Gemini CLI](https://github.com/google-gemini/gemini-cli)** | Gemini 2.5 Pro | 大上下文代码理解 | ✅ | ✅ 开源 |
| **[Aider](https://github.com/paul-gauthier/aider)** | 多模型 | 对话式代码修改、Git 集成 | ✅ | ✅ 开源 |
| **[Cursor](https://cursor.sh/)** | 多模型 | IDE 级别 AI 辅助 | ✅ | ❌ 商业 |
| **[OpenCode](https://github.com/anomalyco/opencode)** | 多模型 | 终端原生、轻量 (152K+ ⭐) | ✅ | ✅ 开源 |
| **[Hermes Agent](https://github.com/NousResearch/hermes-agent)** | 多模型 | 自主规划、持久记忆 (127K+ ⭐) | ✅ 中文友好 | ✅ 开源 |

### ⚡ OpenClaw ACP Harness

[OpenClaw](https://github.com/openclaw/openclaw) 通过 **ACP（Agent Control Protocol）** 原生支持 Harness 调度，可在对话中直接唤起 Claude Code、Codex 等 Coding Agent：

```
# 在 OpenClaw 中直接对话触发 Harness
"帮我用 Codex 重构这个函数"
"让 Claude Code 审查一下 PR #42"
"在 Gemini CLI 里分析整个代码库"
```

**核心特性：**
- 🔄 **多 Harness 并行调度** - 同时启动多个 Coding Agent 处理不同子任务
- 📌 **Thread 绑定** - Discord/Slack 频道中每个对话线程独立维护一个 Agent Session
- 🔁 **Push 完成通知** - 任务完成后主动推送结果，无需轮询
- 🔒 **权限隔离** - `bypassPermissions` 模式下 Agent 可全自动操作，无需人工确认
- 🌐 **中文指令透传** - 直接用中文描述任务，OpenClaw 自动适配各 Harness 协议

**快速配置示例：**

```jsonc
// openclaw.config.json
{
  "acp": {
    "defaultAgent": "claude-code",  // 默认 Harness
    "allowedAgents": ["claude-code", "codex", "gemini-cli", "aider"],
    "sessionTarget": "isolated"     // 隔离执行，不污染主会话
  }
}
```

**对话触发示例（Discord/Telegram/微信）：**

```
用户: 帮我在 Codex 里实现一个微信消息去重模块
AI:  好的，正在启动 Codex... [spawn isolated session]
     任务完成后会通知你 🚀

# 几分钟后
AI:  ✅ Codex 完成了！已在 feat/dedup-wechat 分支提交代码：
     - 新增 MessageDeduplicator 类
     - 单元测试覆盖率 92%
     - PR 链接：https://github.com/...
```

### 🛠️ 主流 Harness 安装与配置

#### Claude Code（推荐）

```bash
# 安装
npm install -g @anthropic-ai/claude-code

# 配置国内可访问的 API 端点（支持 BRConnector 等中转）
export ANTHROPIC_BASE_URL="https://your-proxy.example.com"
export ANTHROPIC_API_KEY="sk-..."

# 验证
claude --version

# 以非交互模式运行（适合 Harness 调度）
claude --print --permission-mode bypassPermissions "重构 utils.py 中的缓存逻辑"
```

#### Codex CLI

```bash
# 安装
npm install -g @openai/codex

# 配置
export OPENAI_API_KEY="sk-..."
# 国内用户可配置 baseURL
export OPENAI_BASE_URL="https://your-proxy.example.com/v1"

# 运行（需要 PTY 终端）
codex "用 Python 写一个飞书消息推送脚本"
```

#### Aider（多模型，中文友好）

```bash
# 安装
pip install aider-chat

# 配置通义千问（国内直连）
export OPENAI_API_KEY="your-qwen-api-key"
export OPENAI_API_BASE="https://dashscope.aliyuncs.com/compatible-mode/v1"

# 启动，绑定到 Git 仓库
cd your-project
aider --model qwen-max --chinese  # 全程中文交互
```

### 📋 Harness 使用场景速查

| 场景 | 推荐 Harness | 说明 |
|------|-------------|------|
| **新功能开发** | Claude Code | 理解需求 → 规划 → 实现 → 测试，全自动 |
| **PR 代码审查** | Claude Code / Gemini CLI | 分析 diff，给出中文审查意见 |
| **大型重构** | Gemini CLI | 200K 上下文，适合大代码库 |
| **脚本生成** | Codex | 快速生成 shell/Python 工具脚本 |
| **对话式修改** | Aider | 持续对话，每步提交 Git |
| **IDE 辅助** | Cursor | 图形化，适合不习惯终端的开发者 |
| **企业私有化** | Aider + 本地 LLM | Ollama + Qwen，数据不出内网 |

### 🔗 相关资源

- **[OpenClaw 官方文档 - Coding Agent](https://docs.openclaw.ai)** - ACP Harness 配置完整指南
- **[Claude Code GitHub](https://github.com/anthropics/claude-code)** - 官方仓库
- **[Codex CLI GitHub](https://github.com/openai/codex)** - OpenAI 开源 Harness
- **[Aider GitHub](https://github.com/paul-gauthier/aider)** - 多模型对话式 Harness（18K+ ⭐）
- **[Gemini CLI GitHub](https://github.com/google-gemini/gemini-cli)** - Google 官方 CLI Harness

---

## 🚀 快速开始

### 给贡献者

欢迎参与建设这个资源库!你可以:

1. *⭐ Star 本项目* - 支持我们持续更新
2. *📝 提交资源* - 分享你发现的优质工具和教程
3. *💬 参与讨论* - 在 [Discussions](https://github.com/happydog-intj/awesome-chinese-ai-agents/discussions) 分享经验
4. *🐛 报告问题* - 发现错误或过时信息请提 [Issue](https://github.com/happydog-intj/awesome-chinese-ai-agents/issues)

详细贡献指南: [CONTRIBUTING.md](CONTRIBUTING.md)

### 给使用者

*新手入门建议*:
1. 浏览 [精选项目](#-精选项目) 选择一个框架(推荐 LangChain 或 Dify)
2. 查看 [对话平台集成](#-对话平台集成) 了解如何接入微信/抖音等平台
3. 参考 [实战案例](#-实战案例) 学习完整的实现方案
4. 阅读 [FAQ](docs/FAQ.md) 解决常见问题

*5分钟快速上手*:

```bash
# 方案1: 使用 Dify (可视化,零代码)
git clone https://github.com/langgenius/dify.git
cd dify/docker
docker-compose up -d
# 访问 http://localhost/install 完成安装

# 方案2: 使用 LangChain (代码开发)
pip install langchain openai
# 创建你的第一个 Agent
python -c "
from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI

llm = OpenAI(temperature=0)
tools = []
agent = initialize_agent(tools, llm, agent='zero-shot-react-description')
print(agent.run('你好,请介绍一下自己'))
"

# 方案3: 使用 Ollama (本地运行)
curl https://ollama.ai/install.sh | sh
ollama run qwen  # 运行通义千问模型
```

### 给项目发起者

如果你正在发起一个 AI Agent 项目,参考我们的经验:
- *📋 发布策略* - [LAUNCH_STRATEGY.md](LAUNCH_STRATEGY.md) 完整的3天发布计划
- *📝 文案模板* - [LAUNCH_CONTENT.md](LAUNCH_CONTENT.md) 各平台宣传文案
- *⚡ 2小时行动指南* - [QUICK_START_GUIDE.md](QUICK_START_GUIDE.md) 快速启动清单

---

## 🌟 精选项目

### AI Agent 框架

- **[LangChain](https://github.com/langchain-ai/langchain)** - 最流行的 LLM 应用开发框架
  - 官方中文文档
  - 庞大的中文社区
  - 海量的中文教程
  - [中文入门指南](https://github.com/liaokongVFX/LangChain-Chinese-Getting-Started-Guide) (8.8K+ ⭐)

- **[MetaGPT](https://github.com/FoundationAgents/MetaGPT)** - 多 Agent 元编程框架 (中国团队)
  - 完全中文支持
  - 软件公司级别的协作
  - 自动生成PRD、设计文档、代码

- **[AutoGen](https://github.com/microsoft/autogen)** - 微软开源的多 Agent 对话框架
  - 中文文档完善
  - 支持多 Agent 协作
  - 丰富的示例代码

- **[万物 Wanwu](https://github.com/UnicomAI/wanwu)** - 中国联通元景万物 Agent 平台 (3.9K+ ⭐)
  - 企业级多租户 AI Agent 开发平台
  - 支持智能体、工作流、RAG 应用构建
  - 模型管理功能
  - 开发者友好的许可证

- **[Deer-Flow](https://github.com/bytedance/deer-flow)** 🆕 - 字节跳动开源 SuperAgent 框架 (63K+ ⭐)
  - 长程任务：可执行需要数分钟至数小时的复杂任务
  - 集成沙箱隔离环境、长期记忆、多种工具调用
  - 支持子 Agent 并行协作与消息网关
  - 适合研究、编码、内容创作等复杂场景

- **[LobeHub](https://github.com/lobehub/lobehub)** 🆕 - 新一代多 Agent 协作平台 (75K+ ⭐)
  - 支持多 Agent 团队设计和协作
  - 以 Agent 为工作交互单元
  - 集成 AI 市场，可发现和复用 Agent 团队
  - 支持中英文界面

- **[openai/openai-agents-python](https://github.com/openai/openai-agents-python)** 🆕 - OpenAI 官方 Agent 框架 (25K+ ⭐)
  - OpenAI 官方出品，轻量但功能完整的多 Agent 框架
  - 支持 handoff（Agent 切换）、guardrails（护栏）、tracing（链路追踪）
  - 生产就绪，与 GPT 系列深度集成

- **[google/adk-python](https://github.com/google/adk-python)** 🆕 - Google Agent Development Kit (19K+ ⭐)
  - Google 官方 Agent 开发套件，代码优先、模型无关
  - 内置评估、安全护栏和多 Agent 编排能力
  - 与 Gemini CLI 协同构建完整 Google AI 生态

- **[HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything)** 🆕 - 全能 RAG 框架（香港大学）(18.6K+ ⭐)
  - 支持文本、图像、表格、音频等多模态文档检索
  - 统一检索接口，大幅简化 RAG 管道构建
  - 学术团队背景，论文级别的方法论落地

- **[Tencent/WeKnora](https://github.com/Tencent/WeKnora)** 🆕 - 腾讯企业级 RAG 知识库平台 (14K+ ⭐)
  - 腾讯出品，基于深度文档理解的语义检索平台
  - 支持上下文感知问答，企业级可靠性
  - RAG 范式优化，适合大规模知识库场景

- **[NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)** 🆕 - 新一代开源 AI Agent 框架 (127K+ ⭐)
  - 全新架构设计，与用户共同成长的 Agent
  - 支持持久记忆、技能学习和自主规划
  - 多模型兼容，可接入 OpenAI、Claude、Qwen 等
  - 活跃社区，Hermes 系列在中文圈广受关注

- **[HKUDS/nanobot](https://github.com/HKUDS/nanobot)** 🆕 - 超轻量个人 AI Agent（香港大学）(41K+ ⭐)
  - 极简架构，单机部署成本极低
  - 支持个人知识库、任务自动化
  - 与 RAG-Anything 同团队出品，中文优化良好
  - 适合个人开发者快速落地

- **[mem0ai/mem0](https://github.com/mem0ai/mem0)** 🆕 - AI Agent 通用记忆层 (54K+ ⭐)
  - 为 Agent 提供持久化、个性化的跨会话记忆
  - 自动学习用户偏好，支持记忆增删改查
  - 可插拔架构，与 LangChain、AutoGen 无缝集成
  - 多语言支持，中文记忆效果良好

- **[Langchain-Chatchat](https://github.com/chatchat-space/Langchain-Chatchat)** - 基于 LangChain 的知识库问答应用
  - 完整的中文支持
  - 本地知识库问答
  - 支持多种中文 LLM

### 中文原生 LLM 与工具

- **[LLamaFactory](https://github.com/hiyouga/LLamaFactory)** - 易用的 LLM 微调框架
  - 支持多种中文模型
  - 一键训练和部署
  - Web UI 界面

- **[ChatGLM-6B](https://github.com/THUDM/ChatGLM-6B)** - 清华开源的中文对话模型
  - 针对中文优化
  - 可本地部署
  - 适合私有化场景

- **[Qwen-Agent](https://github.com/QwenLM/Qwen-Agent)** - 阿里巴巴通义千问 Agent 框架
  - 完整的中文文档
  - 官方技术支持
  - 与通义千问深度集成

- **[Chinese-LangChain](https://github.com/yanqiangmiffy/Chinese-LangChain)** - 中文 LangChain 项目集合 (2.8K+ ⭐)
  - 中文 LLM 应用案例
  - 实战项目代码

- **[shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code)** 🆕 - 中文 Agent Harness 实战教程 (56K+ ⭐)
  - 中国团队出品："Bash is all you need"
  - 从零仿造 Claude Code 风格的终端 Agent Harness
  - 中文注释详尽，适合国内开发者学习 Agent 底层原理

- **[liyupi/ai-guide](https://github.com/liyupi/ai-guide)** 🆕 - 程序员鱼皮 AI 资源大全 (12K+ ⭐)
  - 中国知名开发者鱼皮出品，覆盖 OpenClaw/Vibe Coding 全生态
  - DeepSeek/GPT/Gemini/Claude 玩法 + Prompt 大全
  - 含 Agent Skills/RAG/MCP/A2A 知识百科，持续更新

- **[ModelEngine-Group/nexent](https://github.com/ModelEngine-Group/nexent)** 🆕 - 零代码 Agent 自动生成平台 (4.3K+ ⭐)
  - 基于 Harness Engineering 原则的零代码 Agent 平台
  - 统一工具、技能、记忆和编排，内置约束和反馈循环
  - 自动生成生产级 AI Agent，无需编写代码

### 框架对比

| 框架 | 上手难度 | 中文支持 | 社区活跃度 | 适用场景 | Star数 |
|------|---------|---------|----------|---------|--------|
| *LangChain* | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | 通用开发 | 135K+ |
| *MetaGPT* | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | 多Agent协作 | 45K+ |
| *AutoGen* | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | 对话系统 | 35K+ |
| *万物 Wanwu* | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | 企业应用 | 3.9K |
| *Dify* | ⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | 可视化开发 | 138K+ |
| *Deer-Flow* 🆕 | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | 长程复杂任务 | 63K+ |
| *LobeHub* 🆕 | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | 多Agent协作平台 | 75K+ |

---

## 🛠️ 开发工具

### 开发框架

- **[LangGraph](https://github.com/langchain-ai/langgraph)** - 构建有状态的 Agent 工作流
  - 可视化工作流编辑
  - 中文示例丰富
  - 与 LangChain 无缝集成

- **[CrewAI](https://github.com/joaomdmoura/crewAI)** - 角色扮演型多 Agent 协作框架
  - 简单易用的 API
  - 适合团队协作场景
  - 支持中文场景

- **[DD-OS](https://github.com/FatBy/DD-OS)** - 基于事件驱动与 Nexus 记忆机制的 AI Agent 操作系统
  - 可视化的节点，开箱即用
  - V3 状态机架构配合 Nexus 分层记忆，执行更稳定
  - 独创"模拟城市"等轴测 UI，全景监控 Agent 任务流

- **[browser-use/browser-use](https://github.com/browser-use/browser-use)** 🆕 - 让 AI Agent 直接操控浏览器 (91K+ ⭐)
  - 一行代码让 Agent 访问任意网页、填表、点击
  - 基于 Playwright，支持视觉+DOM 双模式理解
  - 兼容 OpenAI、Claude、通义千问等主流模型
  - 国内淘宝、微博、小红书等场景已有实测案例

- **[ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp)** 🆕 - Chrome 官方 MCP 工具（Google 出品）(37K+ ⭐)
  - Google 官方将 Chrome DevTools 接入 MCP 协议
  - 允许 Coding Agent 直接调试页面、检查 Network、查看 Console
  - 配合 Claude Code / Codex 实现前端自动化调试
  - 无需插件，直接对接已打开的 Chrome 实例

### RAG 与知识库

- **[Langchain-Chatchat](https://github.com/chatchat-space/Langchain-Chatchat)** - 本地知识库问答系统
  - 支持多种文档格式
  - 向量数据库集成
  - 完整的中文支持

- **[QAnything](https://github.com/netease-youdao/QAnything)** - 网易有道的本地知识库问答
  - 支持任意格式文件
  - 离线运行
  - 中文优化

- **[RAGFlow](https://github.com/infiniflow/ragflow)** - 基于深度文档理解的 RAG 引擎
  - 可视化管理界面
  - 支持复杂文档解析
  - 中文文档完善

### 可视化开发平台

- **[Dify](https://github.com/langgenius/dify)** - 开源的 LLM 应用开发平台
  - 可视化 Prompt 编排
  - 支持多种 LLM
  - 完整的中文界面
  - Agent 和工作流设计

- **[FastGPT](https://github.com/labring/FastGPT)** - 知识库问答系统
  - 拖拽式工作流
  - 可视化调试
  - 支持 API 调用
  - 数据集管理

### 提示词工程

- **[ChatGPT-Prompt-Engineering-for-Developers-in-Chinese](https://github.com/GitHubDaily/ChatGPT-Prompt-Engineering-for-Developers-in-Chinese)** - 吴恩达提示词课程中文版
  - 系统化的提示词教程
  - 实战案例丰富
  - 适合入门学习

- **[Prompt-Engineering-Guide-Chinese](https://github.com/wangxuqi/Prompt-Engineering-Guide-Chinese)** - 提示词工程指南中文版
  - 全面的提示词技巧
  - 最佳实践案例
  - 持续更新

### 监控与调试

- **[Langfuse](https://github.com/langfuse/langfuse)** - 开源 LLM 工程平台
  - LLM 可观测性
  - Prompt 管理和版本控制
  - 成本追踪和分析
  - 支持多种 LLM 框架集成

- **[LangSmith](https://smith.langchain.com/)** - LangChain 官方监控平台
  - 实时追踪 Agent 执行
  - 调试和优化 Prompt
  - 性能分析
  - 中文界面支持

- **[OpenLLMetry](https://github.com/traceloop/openllmetry)** - LLM 可观测性工具
  - OpenTelemetry 集成
  - 追踪 LLM 调用
  - 性能监控
  - 开源免费

### 向量数据库

- **[Qdrant](https://github.com/qdrant/qdrant)** - 高性能向量搜索引擎
  - Rust 编写,性能优秀
  - 支持过滤和分组
  - 完善的中文文档
  - Docker 一键部署

- **[Milvus](https://github.com/milvus-io/milvus)** - 云原生向量数据库
  - 支持海量数据
  - 多种索引算法
  - 中国团队开发
  - 企业级特性

- **[Chroma](https://github.com/chroma-core/chroma)** - AI 原生向量数据库
  - 轻量级,易于使用
  - Python/JS SDK
  - 适合快速原型开发
  - 开源免费

### 部署与运维

- **[Ollama](https://github.com/ollama/ollama)** - 本地运行大语言模型
  - 一键安装部署
  - 支持多种模型
  - API 兼容 OpenAI
  - 资源占用可控

- **[LocalAI](https://github.com/mudler/LocalAI)** - 本地 AI API 服务
  - OpenAI 兼容 API
  - 支持 CPU 运行
  - Docker 部署
  - 隐私保护

- **[vLLM](https://github.com/vllm-project/vllm)** - 高性能 LLM 推理引擎
  - 吞吐量提升 10-20倍
  - 支持主流 LLM
  - 生产环境可用
  - PagedAttention 优化

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

### 微信生态

- **[WeChaty](https://github.com/wechaty/wechaty)** - 对话机器人 SDK
  - 支持多种微信协议
  - TypeScript/JavaScript
  - 活跃的社区支持

- **[CowAgent (chatgpt-on-wechat)](https://github.com/zhayujie/CowAgent)** 🆕 - 超级 AI 助理，已升级为全功能 Agent (43K+ ⭐)
  - 从微信机器人升级为具备自主思考和任务规划的 AI 助理
  - 支持微信、飞书、钉钉、企微、QQ、公众号等全平台
  - 可选 DeepSeek/OpenAI/Claude/Gemini/Qwen/GLM 等模型
  - 支持长期记忆、知识库、技能创建与执行

- **[wechat-chatgpt](https://github.com/fuergaosi233/wechat-chatgpt)** - 微信 + ChatGPT 集成
  - 简单易用
  - Docker 部署
  - 支持群聊

- **[wechat-bot](https://github.com/wangrongding/wechat-bot)** - 功能丰富的微信机器人
  - 支持多种功能
  - 定时任务
  - 群管理

- **[wechatbot-webhook](https://github.com/danni-cool/wechatbot-webhook)** - 微信机器人 Webhook 方案
  - RESTful API
  - 易于集成
  - 支持企业微信

- **[AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot)** 🆕 - 多平台 AI Agent 助理 (31K+ ⭐)
  - 支持微信、QQ、飞书、Telegram、Discord 等多平台
  - 插件系统丰富，支持自定义 AI 技能
  - 内置对话管理、任务调度、知识库
  - 可作为 OpenClaw 的轻量替代方案，中文文档完善

### 即时通讯

| 平台 | 集成难度 | 文档质量 | 推荐方案 |
|------|---------|---------|---------|
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

### 优质学习资源

- **[datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents)** 🆕 - 《从零开始构建智能体》(42K+ ⭐)
  - Datawhale 出品，系统性中文 AI Agent 教程
  - 从原理到实战，覆盖 Agent 完整知识体系
  - 含代码示例、图解和实验环境，零基础友好
  - 持续更新，社区活跃，配套视频课程

- **[Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)** 🆕 - 100+ 可运行 AI Agent & RAG 应用合集 (108K+ ⭐)
  - 涵盖金融、医疗、教育、代码等多个垂直场景
  - 每个项目均可 clone 后直接运行，学习成本极低
  - 持续新增中文友好的应用示例
  - 配套详细文档和视频教程

- **[LangChain-Chinese-Getting-Started-Guide](https://github.com/liaokongVFX/LangChain-Chinese-Getting-Started-Guide)** (8.8K+ ⭐)
  - LangChain 中文入门教程
  - 从零开始的完整指南
  - 实战案例丰富

- **[Chinese-LangChain](https://github.com/yanqiangmiffy/Chinese-LangChain)** (2.8K+ ⭐)
  - 中文 LangChain 项目集合
  - 包含多个实战项目
  - 代码可直接运行

- **[Hugging Face 中文课程](https://huggingface.co/learn/nlp-course/zh-CN)** - 免费 NLP 在线课程
  - 官方中文翻译
  - 交互式学习
  - 涵盖 Transformers 库

### 视频教程

- **B站搜索关键词**: "AI Agent 教程", "LangChain 实战", "大模型应用开发"
- **推荐UP主**:
  - [@李沐](https://space.bilibili.com/1567748478) - 深度学习论文精读
  - 搜索 "LangChain 中文教程"
  - 搜索 "ChatGPT API 开发"

### 博客与社区

- **[知乎 - AI Agent 话题](https://www.zhihu.com/topic/20436836)** - 高质量讨论
- **[掘金 - AI Agent 标签](https://juejin.cn/tag/AI%20Agent)** - 技术文章
- **[CSDN - AI 专区](https://blog.csdn.com/nav/ai)** - 实战教程

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

### Agent 系统提示词

```markdown
#### 多步骤任务执行 Agent

你是一个任务执行助手,能够将复杂任务分解为多个步骤并逐步完成。

对于用户的请求,请:
1. 分析任务需求,列出需要完成的子任务
2. 为每个子任务制定执行计划
3. 按顺序执行各个子任务
4. 每完成一个子任务后,总结结果并继续下一步
5. 如遇到问题,说明原因并调整计划
6. 所有子任务完成后,提供完整总结

工具使用规则:
- 需要搜索信息时使用 search 工具
- 需要计算时使用 calculator 工具
- 需要生成代码时使用 code_generator 工具
- 每次只调用一个工具,等待结果后再继续

请用中文清晰地说明你的思考过程和执行步骤。
```

```markdown
#### RAG 知识库问答 Agent

你是一个专业的知识库助手,基于提供的上下文回答用户问题。

回答规则:
1. 仔细阅读检索到的上下文信息
2. 只基于上下文中的内容回答,不要编造
3. 如果上下文中没有相关信息,诚实地说"根据现有资料无法回答"
4. 引用时请注明来源段落
5. 回答要准确、简洁、专业
6. 使用中文回答

上下文信息:
{context}

用户问题:
{question}

请基于以上上下文回答用户问题。
```

```markdown
#### 微信客服机器人

你是 {公司名称} 的智能客服助手,负责解答用户咨询。

服务准则:
- 态度友好,回复及时
- 用简单易懂的语言
- 提供准确的信息
- 无法解决时及时转人工

常见问题处理:
1. 订单查询 → 引导提供订单号,调用订单查询接口
2. 物流查询 → 引导提供运单号,调用物流接口
3. 退换货 → 说明政策,引导填写申请表单
4. 产品咨询 → 基于产品知识库回答
5. 投诉建议 → 记录并转人工处理

触发转人工关键词:
"人工客服"、"转人工"、"投诉"、"经理"

请用温暖、专业的语气与用户交流,使用中文回复。
```

### 数据分析提示词

```markdown
#### 数据分析与可视化

作为数据分析师,请分析以下数据并生成报告:

数据: {数据内容或数据描述}

分析要求:
1. 数据清洗: 识别并处理异常值、缺失值
2. 描述性统计: 计算均值、中位数、标准差等
3. 趋势分析: 识别数据中的规律和趋势
4. 相关性分析: 分析变量之间的关系
5. 可视化建议: 推荐合适的图表类型
6. 结论总结: 提炼关键发现和建议

输出格式:
- 使用 Markdown 表格展示统计结果
- 用中文描述发现和洞察
- 提供 Python/Pandas 代码示例
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
- LangChain (Agent框架)
- ChatGPT/Claude (内容生成)
- 小红书开放平台 (内容发布)
- MongoDB (数据存储)

**功能**:
- 根据关键词生成笔记
- 自动添加标签和emoji
- 定时发布
- 数据监控与分析

**代码**: [查看完整实现](examples/xiaohongshu-content-agent/)

---

### 案例3: 金融多 Agent 投研系统 🆕

**场景**: 多 Agent 协作完成 A/H/美股的实时分析与交易决策

**参考项目**: **[TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)** (58K+ ⭐)

**技术栈**:
- LangGraph (多 Agent 工作流编排)
- GPT-4o / Claude (分析决策)
- 多数据源（行情+新闻+财报）
- PostgreSQL / Redis (数据持久化)

**Agent 分工**:
- 数据采集 Agent — 实时获取行情和新闻
- 分析 Agent — 技术面+基本面综合研判
- 风控 Agent — Kelly 准则仓位管理
- 执行 Agent — 下单与持仓管理

**代码**: [查看 TradingAgents 完整实现](https://github.com/TauricResearch/TradingAgents)

---

### 案例4: 自动化SEO优化工具

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

### 快速上手代码示例

#### 示例1: 最简单的 LangChain Agent

```python
from langchain.agents import initialize_agent, Tool, AgentType
from langchain_openai import ChatOpenAI
from langchain.tools import DuckDuckGoSearchRun

# 初始化 LLM
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0,
    openai_api_key="your-api-key"
)

# 定义工具
search = DuckDuckGoSearchRun()
tools = [
    Tool(
        name="搜索",
        func=search.run,
        description="用于搜索最新信息。输入应该是搜索查询。"
    )
]

# 创建 Agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    max_iterations=3
)

# 运行 Agent
result = agent.run("2024年中国AI发展现状")
print(result)
```

#### 示例2: 简单的 RAG 知识库问答

```python
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA

# 1. 加载文档
loader = TextLoader("knowledge_base.txt", encoding="utf-8")
documents = loader.load()

# 2. 文档分块
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
texts = text_splitter.split_documents(documents)

# 3. 创建向量数据库
embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(
    documents=texts,
    embedding=embeddings
)

# 4. 创建问答链
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever(search_kwargs={"k": 3})
)

# 5. 提问
question = "这个产品的主要功能是什么?"
answer = qa_chain.run(question)
print(answer)
```

#### 示例3: 微信机器人集成 (基于 WeChaty)

```javascript
const { WechatyBuilder } = require('wechaty')
const { OpenAI } = require('openai')

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY
})

// 创建机器人
const bot = WechatyBuilder.build({
  name: 'ai-assistant'
})

// 监听消息
bot.on('message', async (message) => {
  // 忽略自己的消息
  if (message.self()) return

  // 获取消息内容
  const text = message.text()
  const contact = message.talker()

  // 只响应包含 @机器人 的消息
  if (!text.includes('@AI助手')) return

  try {
    // 调用 OpenAI
    const response = await openai.chat.completions.create({
      model: 'gpt-3.5-turbo',
      messages: [
        { role: 'system', content: '你是一个友好的助手,用简洁的中文回答问题。' },
        { role: 'user', content: text.replace('@AI助手', '').trim() }
      ],
      max_tokens: 500
    })

    const reply = response.choices[0].message.content
    await message.say(reply)

  } catch (error) {
    console.error('Error:', error)
    await message.say('抱歉,我遇到了一些问题,请稍后再试。')
  }
})

// 启动机器人
bot.start()
  .then(() => console.log('机器人启动成功'))
  .catch(e => console.error('启动失败:', e))
```

#### 示例4: 使用 Dify API 调用 Agent

```python
import requests

# Dify API 配置
DIFY_API_KEY = "your-dify-api-key"
DIFY_API_URL = "https://api.dify.ai/v1/chat-messages"

def chat_with_dify(query, conversation_id=None):
    """调用 Dify Agent"""

    headers = {
        "Authorization": f"Bearer {DIFY_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "inputs": {},
        "query": query,
        "response_mode": "blocking",
        "user": "user-123"
    }

    if conversation_id:
        data["conversation_id"] = conversation_id

    response = requests.post(DIFY_API_URL, headers=headers, json=data)
    result = response.json()

    return {
        "answer": result["answer"],
        "conversation_id": result["conversation_id"]
    }

# 使用示例
response1 = chat_with_dify("你好,介绍一下自己")
print(response1["answer"])

# 继续对话
response2 = chat_with_dify(
    "你能做什么?",
    conversation_id=response1["conversation_id"]
)
print(response2["answer"])
```

#### 示例5: 成本监控和缓存优化

```python
from functools import lru_cache
import hashlib
import json
from langchain_openai import ChatOpenAI
from langchain.cache import InMemoryCache
import langchain

# 启用 LangChain 缓存
langchain.llm_cache = InMemoryCache()

class CostTracker:
    """成本追踪器"""
    def __init__(self):
        self.total_tokens = 0
        self.total_cost = 0
        # GPT-3.5-turbo 价格 (每1K tokens)
        self.input_cost_per_1k = 0.0015
        self.output_cost_per_1k = 0.002

    def track(self, input_tokens, output_tokens):
        self.total_tokens += (input_tokens + output_tokens)
        cost = (input_tokens * self.input_cost_per_1k / 1000 +
                output_tokens * self.output_cost_per_1k / 1000)
        self.total_cost += cost
        return cost

    def get_stats(self):
        return {
            "total_tokens": self.total_tokens,
            "total_cost_usd": round(self.total_cost, 4)
        }

# 初始化
tracker = CostTracker()
llm = ChatOpenAI(model="gpt-3.5-turbo")

# 使用缓存的装饰器
@lru_cache(maxsize=100)
def get_cached_response(query_hash):
    """缓存相似查询的响应"""
    return None

def chat(query):
    # 计算查询哈希
    query_hash = hashlib.md5(query.encode()).hexdigest()

    # 检查缓存
    cached = get_cached_response(query_hash)
    if cached:
        print("✓ 使用缓存响应,节省成本")
        return cached

    # 调用 LLM
    response = llm.predict(query)

    # 追踪成本 (估算)
    input_tokens = len(query) // 4
    output_tokens = len(response) // 4
    cost = tracker.track(input_tokens, output_tokens)

    print(f"✓ 本次调用成本: ${cost:.4f}")

    # 缓存响应
    get_cached_response.cache_info()

    return response

# 测试
print(chat("什么是人工智能?"))
print(chat("什么是人工智能?"))  # 第二次调用会使用缓存

# 查看统计
print("\n成本统计:", tracker.get_stats())
```

---

## 🔧 常见错误与故障排除

### 安装和环境问题

<details>
<summary><b>错误: ImportError: No module named 'langchain'</b></summary>

*原因*: LangChain 未安装或安装版本不正确

*解决方案*:
```bash
# 安装最新版本
pip install langchain langchain-openai langchain-community

# 或指定版本
pip install langchain==0.1.0

# 检查安装
python -c "import langchain; print(langchain.__version__)"
```
</details>

<details>
<summary><b>错误: SSL Certificate Verification Failed</b></summary>

*原因*: SSL 证书验证失败,常见于国内网络环境

*解决方案*:
```python
# 临时禁用 SSL 验证 (不推荐生产环境)
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 或设置代理
import os
os.environ['HTTP_PROXY'] = 'http://your-proxy:port'
os.environ['HTTPS_PROXY'] = 'http://your-proxy:port'
```
</details>

### API 调用问题

<details>
<summary><b>错误: RateLimitError: Rate limit exceeded</b></summary>

*原因*: API 调用频率超限

*解决方案*:
```python
from time import sleep
from tenacity import retry, wait_exponential, stop_after_attempt

@retry(
    wait=wait_exponential(multiplier=1, min=4, max=60),
    stop=stop_after_attempt(5)
)
def call_llm_with_retry(prompt):
    try:
        return llm.predict(prompt)
    except Exception as e:
        print(f"错误: {e}, 重试中...")
        raise

# 或添加延迟
sleep(1)  # 每次调用间隔 1 秒
```
</details>

<details>
<summary><b>错误: AuthenticationError: Invalid API key</b></summary>

*原因*: API 密钥无效或未设置

*解决方案*:
```bash
# 设置环境变量
export OPENAI_API_KEY="sk-..."

# 或在代码中设置
import os
os.environ['OPENAI_API_KEY'] = 'sk-...'

# 验证密钥
from openai import OpenAI
client = OpenAI()
print(client.models.list())  # 测试连接
```
</details>

### 向量数据库问题

<details>
<summary><b>错误: ChromaDB dimension mismatch</b></summary>

*原因*: Embedding 维度与数据库中存储的不一致

*解决方案*:
```python
# 删除旧数据库重新创建
import shutil
shutil.rmtree("./chroma_db")

# 确保使用相同的 Embedding 模型
from langchain_openai import OpenAIEmbeddings
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# 重新创建向量库
vectorstore = Chroma.from_documents(
    documents=docs,
    embedding=embeddings,
    persist_directory="./chroma_db"
)
```
</details>

### 性能问题

<details>
<summary><b>问题: 响应速度太慢</b></summary>

*优化方案*:

1. *使用流式输出*
```python
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

llm = ChatOpenAI(
    streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()]
)
```

2. *减少 Top-K*
```python
retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}  # 从 10 减少到 3
)
```

3. *使用更快的模型*
```python
llm = ChatOpenAI(model="gpt-3.5-turbo")  # 而不是 gpt-4
```

4. *并行处理*
```python
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=5) as executor:
    results = executor.map(process_query, queries)
```
</details>

### 中文处理问题

<details>
<summary><b>问题: 中文分词效果差</b></summary>

*解决方案*:
```python
# 使用专门的中文分词器
from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
    separators=["\n\n", "\n", "。", "!", "?", ";", ",", " ", ""],
    keep_separator=True
)

# 或使用 jieba
import jieba
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
    length_function=lambda x: len(jieba.lcut(x))
)
```
</details>

---

## 🌐 社区资源

### 中文技术社区

- **[知乎 - 人工智能话题](https://www.zhihu.com/topic/19551275)** - 高质量技术讨论
  - AI Agent 相关话题活跃
  - 行业专家分享经验
  - 最新技术动态

- **[掘金 - AI 标签](https://juejin.cn/tag/AI)** - 开发者社区
  - 技术文章分享
  - 实战经验交流
  - 开源项目推荐

- **[CSDN - AI 专区](https://blog.csdn.com/nav/ai)** - 中文技术博客
  - 入门教程丰富
  - 代码示例完整
  - 问题解答及时

- **[GitHub 中文社区](https://github.com/topics/chinese)** - 开源项目聚集地
  - 中文开源项目
  - 协作开发
  - Issue 讨论

### 学习资源

- **B站 UP主推荐**:
  - 搜索"AI Agent 教程"
  - 搜索"LangChain 实战"
  - 搜索"大模型应用开发"

- **公众号推荐**:
  - "AI科技大本营"
  - "机器之心"
  - "量子位"
  - "新智元"

### 开源贡献

欢迎为本项目贡献资源!
- 提交 Issue 报告问题
- 提交 PR 添加资源
- Star 本项目支持我们
- 分享给更多开发者

---

## ❓ 常见问题速查

<details>
<summary><b>Q: 我是新手,应该从哪个框架开始?</b></summary>

A: 推荐顺序:
- *零代码*: Dify (可视化界面,拖拽式开发)
- *Python 开发者*: LangChain (生态完善,中文资源多)
- *企业应用*: 万物 Wanwu (多租户,开箱即用)
</details>

<details>
<summary><b>Q: 如何选择中文 LLM?</b></summary>

A: 根据需求选择:
- *预算充足*: GPT-4 或 Claude (能力最强)
- *性价比*: 通义千问、文心一言 (中文优化好)
- *私有部署*: ChatGLM、Qwen (可本地运行)
- *免费测试*: Ollama + Qwen (完全本地)
</details>

<details>
<summary><b>Q: 微信机器人会被封号吗?</b></summary>

A: 风险评估:
- *个人微信 + WeChaty*: 有封号风险,建议用小号测试
- *企业微信*: 官方支持,稳定可靠
- *微信公众号*: 官方 API,完全合规
- *建议*: 生产环境优先使用企业微信或公众号
</details>

<details>
<summary><b>Q: RAG 系统的准确率低怎么办?</b></summary>

A: 优化方案:
1. *文档质量*: 清洗格式,去除无效信息
2. *分块策略*: 调整 chunk_size (建议 500-1000 字符)
3. *检索优化*: 使用混合检索 (向量 + 关键词)
4. *Rerank*: 添加重排序模型提升准确率
5. *Prompt 优化*: 明确告诉模型如何使用检索内容
</details>

<details>
<summary><b>Q: 如何降低 API 调用成本?</b></summary>

A: 成本优化技巧:
- *缓存*: 相似问题直接返回缓存结果
- *模型选择*: 简单任务用小模型 (GPT-3.5/通义千问)
- *Prompt 压缩*: 减少不必要的上下文
- *本地模型*: 高频场景考虑 Ollama 本地部署
- *流式输出*: 避免重复生成
</details>

---

## 💡 最佳实践

### 选择合适的框架

- *入门推荐*: LangChain - 文档完善,社区活跃,中文资源丰富
- *企业应用*: 万物 Wanwu - 企业级平台,多租户支持
- *多 Agent 协作*: MetaGPT - 软件开发场景,自动化协作
- *本地部署*: ChatGLM + LangChain - 数据安全,私有化部署

### 中文 LLM 选择

| 模型 | 适用场景 | 优势 | 成本 |
|------|---------|------|------|
| *通义千问* | 通用对话、内容生成 | 中文理解好,API稳定 | 中等 |
| *ChatGLM* | 私有化部署 | 可本地运行,数据安全 | 硬件成本 |
| *文心一言* | 企业应用 | 百度生态集成 | 中等 |
| *GPT-4* | 复杂推理 | 能力最强 | 较高 |

### 微信集成最佳实践

1. *选择合适的接入方案*:
   - 个人微信: WeChaty (注意封号风险)
   - 企业微信: 官方 SDK (稳定可靠)
   - 公众号: 微信公众平台 API (官方支持)

2. *避免常见问题*:
   - 消息去重处理
   - 频率限制控制
   - 异常重连机制
   - 日志监控告警

3. *性能优化*:
   - 使用消息队列异步处理
   - Redis 缓存会话状态
   - 限流防止滥用
   - 定期清理历史数据

### RAG 系统优化

1. *文档预处理*:
   - 清洗格式和无效字符
   - 合理分块 (chunk size 建议 500-1000 字符)
   - 添加元数据信息

2. *向量库选择*:
   - 小规模 (<10万): Chroma, FAISS
   - 中规模 (10万-100万): Qdrant, Milvus
   - 大规模 (>100万): Elasticsearch, Weaviate

3. *检索优化*:
   - 混合检索 (向量 + 关键词)
   - Rerank 重排序
   - 动态调整 Top-K
   - 结果去重和过滤

### 成本优化策略

#### API 调用成本对比 (每百万 tokens)

| 模型 | 输入成本 | 输出成本 | 性价比 | 推荐场景 |
|------|---------|---------|--------|---------|
| *GPT-4 Turbo* | $10 | $30 | ⭐⭐⭐ | 复杂推理 |
| *GPT-3.5 Turbo* | $0.5 | $1.5 | ⭐⭐⭐⭐⭐ | 日常对话 |
| *通义千问 Plus* | ¥8 | ¥20 | ⭐⭐⭐⭐ | 中文场景 |
| *通义千问* | ¥2 | ¥6 | ⭐⭐⭐⭐⭐ | 高频调用 |
| *文心一言* | ¥12 | ¥12 | ⭐⭐⭐⭐ | 企业应用 |
| *Claude 3.5 Sonnet* | $3 | $15 | ⭐⭐⭐⭐ | 代码生成 |

#### 降低成本的 10 个技巧

1. *智能路由*: 简单任务用便宜模型,复杂任务用贵模型
2. *Prompt 压缩*: 移除冗余信息,使用缩写和简洁表达
3. *缓存策略*: 相同/相似问题直接返回缓存 (可节省 60-80%)
4. *流式输出*: 使用 streaming 避免重复生成
5. *批处理*: 合并多个请求,减少 API 调用次数
6. *本地模型*: 高频简单任务用 Ollama 本地模型
7. *Token 限制*: 设置 max_tokens 避免超长输出
8. *异步处理*: 非实时场景使用异步,降低并发成本
9. *模型微调*: 专有场景微调小模型替代大模型
10. *监控告警*: 使用 Langfuse 实时监控成本,设置预算告警

### 安全与隐私保护

#### 数据安全checklist

- [ ] *API 密钥管理*
  - 使用环境变量,不要硬编码
  - 定期轮换密钥
  - 不同环境使用不同密钥
  - 启用 IP 白名单

- [ ] *敏感信息过滤*
  - 过滤身份证号、手机号
  - 脱敏处理用户数据
  - 避免将敏感数据发送到 LLM
  - 加密存储历史对话

- [ ] *访问控制*
  - 实施用户认证和授权
  - 限制 API 调用频率
  - 记录操作审计日志
  - 实施最小权限原则

- [ ] *本地化部署*
  - 敏感场景使用本地模型 (Ollama + ChatGLM)
  - 私有向量数据库 (Qdrant/Milvus 私有部署)
  - 内网隔离,不连接公网
  - 定期安全审计

#### 常见安全风险

1. *Prompt 注入攻击*
   - 风险: 用户输入包含恶意 Prompt 覆盖原始指令
   - 防范: 输入验证,使用系统角色分离,添加安全边界

2. *数据泄露*
   - 风险: 将用户敏感数据发送到第三方 LLM
   - 防范: 数据脱敏,本地模型,加密传输

3. *DDoS 和滥用*
   - 风险: 恶意用户大量调用 API 消耗资源
   - 防范: 限流限频,CAPTCHA,成本预算告警

4. *模型输出有害内容*
   - 风险: LLM 生成违规、有害或错误信息
   - 防范: 内容审核,输出过滤,人工审核机制

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

- 📚 收录资源: **175+** 🆕
- 🔥 Agent Harness: **10+** 🆕
- 🛠️ 开发工具: **35+** 🆕
- 🎯 Agent技能: **80+**
- 💬 平台集成: **15+**
- 📖 教程文档: **55+** 🆕
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
