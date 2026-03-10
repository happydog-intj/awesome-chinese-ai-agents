# 贡献指南 Contributing Guide

[English](#english) | [中文](#中文)

---

## 中文

感谢你考虑为 Awesome Chinese AI Agents 做出贡献! 🎉

### 贡献方式

我们欢迎以下类型的贡献:

1. **添加新资源** 📝
   - 新的工具、框架、库
   - 有用的文档和教程
   - 实用的技能和模板
   - 优秀的项目案例

2. **改进现有内容** ✏️
   - 修复错误链接
   - 更新过时信息
   - 改进描述和说明
   - 添加缺失的详细信息

3. **翻译内容** 🌐
   - 翻译英文资源为中文
   - 翻译中文资源为英文
   - 改进现有翻译质量

4. **分享经验** 💡
   - 添加实战案例
   - 分享最佳实践
   - 提供使用技巧
   - 记录常见问题解决方案

### 提交流程

1. **Fork 项目**
   ```bash
   # 在 GitHub 页面点击 Fork 按钮
   ```

2. **克隆到本地**
   ```bash
   git clone https://github.com/YOUR_USERNAME/awesome-chinese-ai-agents.git
   cd awesome-chinese-ai-agents
   ```

3. **创建新分支**
   ```bash
   git checkout -b add-new-resource
   ```

4. **进行修改**
   - 编辑 README.md 或其他文件
   - 遵循格式规范(见下文)

5. **提交更改**
   ```bash
   git add .
   git commit -m "Add: 新增XXX资源"
   ```

6. **推送到 GitHub**
   ```bash
   git push origin add-new-resource
   ```

7. **创建 Pull Request**
   - 在 GitHub 上打开你的 fork
   - 点击 "New Pull Request"
   - 填写描述信息

### 格式规范

#### 添加新资源

使用以下格式添加新资源:

```markdown
- **[资源名称](链接地址)** - 简短描述(20-50字) (可选: star数)
  - 特点1
  - 特点2
  - 特点3 (可选)
```

**示例**:
```markdown
- **[WeChaty](https://github.com/wechaty/wechaty)** - 微信机器人框架 (18K+ ⭐)
  - 支持多平台
  - TypeScript编写
  - 活跃的中文社区
```

#### 提交信息规范

使用以下前缀:
- `Add:` 添加新内容
- `Update:` 更新现有内容
- `Fix:` 修复错误
- `Remove:` 删除过时内容
- `Docs:` 文档相关改动

**示例**:
- `Add: 新增WeChaty微信机器人框架`
- `Update: 更新LangChain文档链接`
- `Fix: 修复Qwen-Agent仓库链接`
- `Remove: 删除已归档的项目`

### 质量标准

为了保持项目质量,提交的资源应该:

✅ **必须满足**:
- 与 AI Agent 或中文开发相关
- 链接有效且可访问
- 有清晰的文档或说明
- 项目活跃或有持续维护

✅ **优先考虑**:
- 开源项目
- 有中文文档
- Star 数较高
- 社区活跃
- 有实际使用案例

❌ **不接受**:
- 纯商业推广
- 过时或废弃的项目
- 质量低劣的资源
- 与主题无关的内容
- 重复的资源

### 审核流程

1. **自动检查** - CI会检查:
   - Markdown格式
   - 链接有效性
   - 拼写错误

2. **人工审核** - 维护者会检查:
   - 内容质量
   - 分类准确性
   - 描述清晰度
   - 格式规范

3. **合并时间**:
   - 简单修改: 1-2天
   - 大量添加: 3-5天
   - 有问题需要讨论: 视情况而定

### 行为准则

参与本项目时,请:
- 尊重他人
- 建设性讨论
- 保持友善
- 遵守开源精神

### 问题反馈

如果你有问题或建议,可以:
- 提交 [Issue](https://github.com/happydog-intj/awesome-chinese-ai-agents/issues)
- 加入微信群讨论
- 发送邮件至维护者

---

## English

Thank you for considering contributing to Awesome Chinese AI Agents! 🎉

### Ways to Contribute

We welcome the following types of contributions:

1. **Add New Resources** 📝
   - New tools, frameworks, libraries
   - Useful documentation and tutorials
   - Practical skills and templates
   - Excellent project examples

2. **Improve Existing Content** ✏️
   - Fix broken links
   - Update outdated information
   - Improve descriptions
   - Add missing details

3. **Translate Content** 🌐
   - Translate English resources to Chinese
   - Translate Chinese resources to English
   - Improve existing translations

4. **Share Experience** 💡
   - Add use cases
   - Share best practices
   - Provide usage tips
   - Document common solutions

### Submission Process

1. **Fork the Project**
   ```bash
   # Click the Fork button on GitHub
   ```

2. **Clone Locally**
   ```bash
   git clone https://github.com/YOUR_USERNAME/awesome-chinese-ai-agents.git
   cd awesome-chinese-ai-agents
   ```

3. **Create New Branch**
   ```bash
   git checkout -b add-new-resource
   ```

4. **Make Changes**
   - Edit README.md or other files
   - Follow format guidelines (see below)

5. **Commit Changes**
   ```bash
   git add .
   git commit -m "Add: new XXX resource"
   ```

6. **Push to GitHub**
   ```bash
   git push origin add-new-resource
   ```

7. **Create Pull Request**
   - Open your fork on GitHub
   - Click "New Pull Request"
   - Fill in description

### Format Guidelines

#### Adding New Resources

Use this format:

```markdown
- **[Resource Name](Link)** - Brief description (20-50 words) (Optional: stars)
  - Feature 1
  - Feature 2
  - Feature 3 (optional)
```

**Example**:
```markdown
- **[WeChaty](https://github.com/wechaty/wechaty)** - WeChat bot framework (18K+ ⭐)
  - Multi-platform support
  - Written in TypeScript
  - Active Chinese community
```

#### Commit Message Guidelines

Use these prefixes:
- `Add:` Adding new content
- `Update:` Updating existing content
- `Fix:` Fixing errors
- `Remove:` Removing outdated content
- `Docs:` Documentation changes

**Examples**:
- `Add: new WeChaty WeChat bot framework`
- `Update: LangChain documentation link`
- `Fix: Qwen-Agent repository link`
- `Remove: archived project`

### Quality Standards

Submitted resources should:

✅ **Must Have**:
- Related to AI Agent or Chinese development
- Valid and accessible links
- Clear documentation
- Active or maintained

✅ **Preferred**:
- Open source projects
- Chinese documentation
- High star count
- Active community
- Real use cases

❌ **Not Accepted**:
- Pure commercial promotion
- Outdated or abandoned
- Low quality
- Off-topic
- Duplicates

### Review Process

1. **Automated Checks** - CI checks:
   - Markdown format
   - Link validity
   - Spelling

2. **Manual Review** - Maintainers check:
   - Content quality
   - Categorization
   - Description clarity
   - Format compliance

3. **Merge Timeline**:
   - Simple changes: 1-2 days
   - Large additions: 3-5 days
   - Needs discussion: Case by case

### Code of Conduct

When participating:
- Respect others
- Constructive discussion
- Be friendly
- Follow open source spirit

### Feedback

If you have questions:
- Submit an [Issue](https://github.com/happydog-intj/awesome-chinese-ai-agents/issues)
- Join WeChat group
- Email maintainers

---

## 🙏 谢谢你的贡献! Thank You for Your Contribution!
