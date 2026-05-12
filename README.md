# Daily Brief - 全球科技时讯日报

自动收集全球科技新闻，整理成日报，每天早上9点发送到邮箱。

## 📰 功能特性

- **自动采集** - 从多个权威科技媒体采集最新新闻
- **智能聚合** - 去重、分类、排序
- **定时发送** - 每天早上9点自动发送到邮箱
- **精选内容** - 每次发送20条最热门的新闻
- **持续更新** - 使用 GitHub Actions 自动化执行

## 🎯 新闻源

- HackerNews
- TechCrunch
- Ars Technica
- The Verge
- IEEE Spectrum
- ArXiv (AI/ML 论文)
- Product Hunt
- 及其他科技媒体的 RSS 源

## 🚀 快速开始

### 环境要求
- Python 3.8+
- GitHub 账户（用于 Actions）
- 邮箱账户（用于发送日报）

### 安装依赖

```bash
pip install -r requirements.txt
```

### 配置

1. 复制配置文件模板：
```bash
cp config.example.yaml config.yaml
```

2. 编辑 `config.yaml`，填入你的信息：
```yaml
email:
  sender: your_email@gmail.com
  password: your_app_password
  recipient: your_email@gmail.com
  smtp_server: smtp.gmail.com
  smtp_port: 587

sources:
  enable_hackernews: true
  enable_techcrunch: true
  enable_rss: true
```

### 本地测试

```bash
python src/main.py
```

### GitHub Actions 配置

1. 在项目设置中添加 Secrets：
   - `EMAIL_SENDER` - 发件邮箱
   - `EMAIL_PASSWORD` - 邮箱密码或应用密码
   - `EMAIL_RECIPIENT` - 收件邮箱

2. 工作流会在每天 UTC 1:00 (北京时间 9:00) 自动运行

## 📋 项目结构

```
daily-brief/
├── src/
│   ├── main.py              # 主程序入口
│   ├── news_collector.py    # 新闻采集器
│   ├── news_processor.py    # 新闻处理和排序
│   ├── email_sender.py      # 邮件发送
│   └── sources/             # 新闻源模块
│       ├── hackernews.py
│       ├── techcrunch.py
│       ├── rss_feeds.py
│       └── arxiv.py
├── config.yaml              # 配置文件
├── requirements.txt         # 依赖包列表
└── data/
    └── sent_news.json       # 已发送新闻记录
```

## 🛠️ 开发

### 添加新的新闻源

在 `src/sources/` 目录下创建新文件，实现 `NewsSource` 接口：

```python
class MyNewsSource(NewsSource):
    def fetch_news(self):
        # 返回 [{title, url, description, timestamp}, ...]
        pass
```

## 📧 邮件格式

生成的邮件包含：
- 📌 热点话题摘要
- 🔗 20条精选新闻链接
- 📊 新闻来源分布
- ⏰ 发送时间

## 🔐 隐私和安全

- 不存储或转发您的个人信息
- 邮箱密码仅存储在 GitHub Secrets
- 所有数据都是公开的新闻内容

## 📝 许可证

MIT License

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 💡 常见问题

**Q: 如何修改发送时间？**
A: 编辑 `.github/workflows/daily-brief.yml` 中的 cron 表达式

**Q: 如何修改发送数量？**
A: 编辑 `config.yaml` 中的 `news_count` 参数

**Q: 为什么没有收到邮件？**
A: 检查 GitHub Actions 日志，确认 Secrets 配置正确

---

**创建时间**: 2026-05-12  
**作者**: aronxu723-lab
