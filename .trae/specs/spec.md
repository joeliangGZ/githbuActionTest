# GitHub Actions 测试项目 - 产品需求文档

## 概述
- **摘要**: 这是一个用于测试 GitHub Actions CI/CD 功能的 Python 小项目，包含代码质量检查、测试运行、打包构建等常见的 CI/CD 工作流。
- **目的**: 创建一个完整的示例项目，用于学习和测试 GitHub Actions 的各种功能，包括推送特定分支时自动触发 CI/CD 流程。
- **目标用户**: 开发者学习 GitHub Actions CI/CD 流程

## 目标
- 创建可运行的 Python 项目作为 CI/CD 测试载体
- 实现推送 main 或 develop 分支时自动触发 GitHub Actions
- 包含完整的 CI 流程：代码检查、单元测试、构建打包
- 包含 CD 流程示例：构建产物上传、发布版本

## 非目标（不在范围内）
- 不实现实际的部署到生产环境
- 不包含复杂的微服务架构
- 不包含数据库或外部依赖服务

## 背景与上下文
- 这是一个学习性质的测试项目
- 用于演示 GitHub Actions 的核心功能
- 项目采用 Python 语言，适合快速构建和测试

## 功能需求
- **FR-1**: Python 项目基础结构
  - 包含简单的 Python 应用代码（计算器或字符串处理工具）
  - 包含 requirements.txt 依赖管理
  - 包含基本的单元测试

- **FR-2**: GitHub Actions CI 工作流
  - 在推送 main 或 develop 分支时自动触发
  - 代码质量检查（flake8、pylint）
  - 单元测试运行（pytest）
  - 构建产物生成

- **FR-3**: GitHub Actions CD 工作流示例
  - 构建产物上传到 Artifacts
  - 版本发布工作流（手动触发）

- **FR-4**: PR 检查工作流
  - 对 Pull Request 进行自动检查
  - 在 PR 页面显示检查状态

## 非功能需求
- **NFR-1**: CI 工作流执行时间应控制在 5 分钟以内
- **NFR-2**: 所有检查和测试必须通过才能合并 PR
- **NFR-3**: 工作流配置使用最新稳定版的 Actions

## 约束
- **技术**: Python 3.9+, GitHub Actions
- **依赖**: pytest, flake8, build
- **平台**: GitHub

## 假设
- 用户已了解 GitHub 仓库的基本操作
- 用户有权限创建 GitHub Actions 工作流

## 验收标准

### AC-1: 项目结构完整
- **Given**: 初始化完成的项目
- **When**: 查看项目文件结构
- **Then**: 包含 app/、tests/、requirements.txt、pyproject.toml 等必要文件
- **Verification**: `human-judgment`

### AC-2: CI 工作流触发
- **Given**: 已配置好的 GitHub Actions 工作流
- **When**: 推送代码到 main 或 develop 分支
- **Then**: 自动触发 CI 工作流并执行检查
- **Verification**: `programmatic` - 检查 GitHub Actions 运行状态

### AC-3: 代码质量检查通过
- **Given**: Python 代码符合规范
- **When**: CI 工作流运行 flake8/pylint 检查
- **Then**: 检查通过，无警告和错误
- **Verification**: `programmatic` - 检查 Actions 日志

### AC-4: 单元测试通过
- **Given**: 存在单元测试
- **When**: CI 工作流运行 pytest
- **Then**: 所有测试通过
- **Verification**: `programmatic` - 检查测试结果

### AC-5: PR 检查工作流
- **Given**: 创建 Pull Request
- **When**: 推送代码到 PR
- **Then**: 自动运行检查并在 PR 页面显示状态
- **Verification**: `human-judgment`

### AC-6: 构建产物生成
- **Given**: CI 工作流执行完成
- **When**: 构建步骤执行
- **Then**: 生成可分发的 wheel 包
- **Verification**: `programmatic` - 检查 Artifacts

## 待定问题
- [ ] 是否需要添加更多的代码质量检查工具（如 mypy）？
- [ ] 是否需要配置 Dependabot 自动更新依赖？
- [ ] 是否需要添加语义化版本发布（Semantic Release）？
