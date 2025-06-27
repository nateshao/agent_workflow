# Agent Workflow - 批量图片智能换背景自动化平台

## 项目简介

Agent Workflow 是一个面向企业和开发者的批量图片智能换背景自动化平台。支持本地/云端图片批量处理、AI抠图、智能合成、数据库记录、自动通知、定时任务与 n8n 工作流无缝集成，助力内容生产、素材管理、自动化办公等多场景。

---

## 功能亮点
- 🚀 **批量图片处理**：支持本地文件夹批量导入，自动抠图+换背景
- 🤖 **AI智能抠图**：集成 remove.bg API，支持自定义/扩展本地AI模型
- 🖼️ **多背景合成**：支持多背景图片自动合成，适配多业务场景
- 🗄️ **数据库记录**：支持 SQLite/MySQL/PostgreSQL 等主流数据库
- 🔔 **自动通知**：支持邮件、企业微信、钉钉等多渠道消息推送
- ⏰ **定时任务&n8n调度**：支持 crontab 定时、n8n 工作流自动触发
- 🧩 **易于集成**：回调接口可对接任意业务系统，支持二次开发

---

## 目录结构

```
agent_workflow/
├── images/
│   ├── input/         # 待处理图片
│   ├── output/        # 处理后图片
│   └── background/    # 背景图片（支持多张）
├── db.sqlite3         # 默认数据库（可切换MySQL等）
├── process_images.py  # 主处理脚本
├── notify_api.py      # 回调通知接口
├── requirements.txt   # 依赖
├── README.md          # 项目说明
```

---

## 快速开始

1. **安装依赖**
   ```bash
   pip install -r requirements.txt
   ```
2. **准备图片**
   - 待处理图片放入 `images/input/`
   - 背景图片放入 `images/background/bg.jpg`（可多张）
3. **启动回调API**
   ```bash
   python notify_api.py
   ```
4. **运行批量处理脚本**
   ```bash
   python process_images.py
   ```
5. **查看结果**
   - 处理后图片在 `images/output/`
   - 处理记录在数据库
   - 回调日志见 notify_api 控制台

---

## 定时任务与 n8n 调度

### 1. crontab 定时任务
```bash
0 * * * * cd /path/to/agent_workflow && /usr/bin/python3 process_images.py
```

### 2. n8n 工作流调度
- 使用 Execute Command 节点，命令：
  ```bash
  python /path/to/agent_workflow/process_images.py
  ```
- 可配合 Cron/Webhook 节点实现自动化

---

## 数据库集成
- 默认支持 SQLite
- 切换 MySQL/PostgreSQL 只需修改 `process_images.py` 的数据库部分，参考注释配置
- 支持自动建表、记录原图/新图/处理时间等

---

## 邮件/消息通知集成
- 支持邮件（yagmail）、企业微信、钉钉等
- 在 `process_images.py` 的 `notify_project` 函数中配置
- 可多渠道并发推送

---

## 常见问题
- **remove.bg 报错**：检查 API Key、额度、图片格式
- **数据库连接失败**：检查配置、网络、权限
- **图片未输出**：检查 input/output/background 路径、图片格式
- **通知未收到**：检查邮件/微信/钉钉配置、网络

---

## 进阶用法
- 多背景批量合成、按规则分组处理
- 并发/分布式处理大批量图片
- 与主业务系统深度集成（回调、数据库、API）
- 支持自定义AI模型、本地推理
- 结合 n8n 实现更复杂的自动化编排

---

## 贡献方式
- 欢迎提交 PR、Issue，或邮件联系作者
- 支持企业定制、私有化部署、功能扩展

---

## 联系方式
- 作者：Your Name
- 邮箱：your@email.com
- 企业微信/钉钉：请邮件联系获取

---

> 本项目适用于内容生产、素材管理、自动化办公、AI数据处理等多种场景，欢迎二次开发与集成！ 