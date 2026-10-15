<div align="center">

# Template

使用 Go 编写的桌面应用。

[![License](https://img.shields.io/badge/license-proprietary-lightgrey.svg)](LICENSE)
[![Go](https://img.shields.io/badge/go-1.27.1-00ADD8.svg)](.go-version)
![Status](https://img.shields.io/badge/status-pre--release-orange)

[English](README.md) · **简体中文**

</div>

当前状态：预发布。Template 尚未上线，上线前剩余的事项见 [docs/launch.md](docs/launch.md)。开发基线 0.1.0 是一个计数器演示，上线前请把它替换为产品规格。

## 功能特性

- 单一原生窗口，支持 macOS 12+、Windows 10/11 和带 GTK 3 的 Linux（amd64 与 arm64）。
- 修改内存中的计数，并跟随系统语言。

## 环境要求

- Go：版本见 [.go-version](.go-version)（必须与 `go.mod` 一致）。
- Python 3，用于辅助脚本。

## 快速开始

目前还没有下载。开发包只是本地产物，不是公开的签名发布版。

## 开发

```bash
scripts/check.sh --cross   # gofmt、go mod tidy、vet、测试、脚本测试、交叉编译
go tool mygo dev           # 运行应用
go tool mygo build         # 为当前平台打包
```

用 `python3 scripts/bump.py <version>` 同时更新版本号和两份 changelog。

### 文档索引

| 文档 | 内容 |
|---|---|
| [docs/spec.md](docs/spec.md) | 行为与验收标准 |
| [docs/design.md](docs/design.md) | 设计语言 |
| [docs/roadmap.md](docs/roadmap.md) | 发布范围 |
| [docs/launch.md](docs/launch.md) | 上线检查清单 |
| [docs/legal.md](docs/legal.md) | 法律事实及必须与之一致的代码 |
| [docs/website.md](docs/website.md) | 应用对官网的依赖 |
| [docs/releasing.md](docs/releasing.md) | 发布流程 |
| [docs/security/](docs/security/README.md) | 每个版本一份安全审查 |
| [docs/adr/](docs/adr/README.md) | 架构决策 |
| [CHANGELOG.md](CHANGELOG.md) | 变更记录 |
| [THIRD_PARTY.md](THIRD_PARTY.md) | 依赖声明 |
| [AGENTS.md](AGENTS.md) | 面向 AI 协作者的说明 |

## 参与贡献

贡献规则见 [CONTRIBUTING.md](CONTRIBUTING.md)。提交信息和 Pull Request 标题遵循
[Conventional Commits](https://www.conventionalcommits.org/)。

## 安全

请按账号的安全策略（GitHub 私密漏洞报告）报告漏洞，不要公开提 issue。各版本的安全审查保存在
[docs/security/](docs/security/README.md)。

## 致谢

基于 [MyGo](https://github.com/egoist/mygo)；依赖声明见 [THIRD_PARTY.md](THIRD_PARTY.md)。

## 许可证

专有软件，保留所有权利。[LICENSE](LICENSE) 包含服务条款，上线时将发布在产品官网上。
