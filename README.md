# GitHub Actions 测试项目

这是一个用于测试 GitHub Actions CI/CD 功能的 Python 小项目。

## 项目简介

本项目包含一个简单的字符串处理工具库，用于演示和测试 GitHub Actions 的各种功能。

## 功能特性

- `reverse_string()` - 反转字符串
- `capitalize_words()` - 首字母大写
- `remove_whitespace()` - 移除空白字符
- `count_words()` - 统计单词数量
- `is_palindrome()` - 判断是否为回文

## 本地开发

### 安装依赖

```bash
pip install -r requirements.txt
```

### 运行测试

```bash
pytest
```

### 代码检查

```bash
flake8 app/ tests/
```

## GitHub Actions

本项目包含以下 GitHub Actions 工作流：

### CI 工作流 (ci.yml)
- 推送代码到 `main` 或 `develop` 分支时自动触发
- 运行代码质量检查 (flake8)
- 运行单元测试 (pytest)
- 构建打包项目

### PR 检查工作流 (pr-check.yml)
- 对 Pull Request 进行自动检查
- 在 PR 页面显示检查状态

### 发布工作流 (release.yml)
- 手动触发发布流程
- 构建并上传发布产物

## 目录结构

```
.
├── app/
│   ├── __init__.py
│   └── string_utils.py
├── tests/
│   ├── __init__.py
│   └── test_string_utils.py
├── .github/
│   └── workflows/
│       ├── ci.yml
│       ├── pr-check.yml
│       └── release.yml
├── requirements.txt
├── pyproject.toml
├── README.md
└── .gitignore
```

## 许可证

MIT License
