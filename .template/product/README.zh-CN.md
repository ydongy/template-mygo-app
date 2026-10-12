<div align="center">

# Template

使用 Go 编写的桌面应用。

[![License](https://img.shields.io/badge/license-proprietary-lightgrey.svg)](LICENSE)
[![Go](https://img.shields.io/badge/go-1.27.1-00ADD8.svg)](.go-version)
[![Website](https://img.shields.io/badge/website-example.com-informational.svg)](https://example.com)

[English](README.md) · **简体中文**

</div>

当前状态：开发基线 0.1.0，一个计数器演示，尚无公开发布版本，详见[路线图](docs/roadmap.md)。上线前请把基线替换为产品规格。

## 功能特性

- 单一原生窗口，支持 macOS 12+、Windows 10/11 和带 GTK 3 的 Linux（amd64 与 arm64）。
- 修改内存中的计数，并跟随系统语言。

## 环境要求

- Go：版本见 [.go-version](.go-version)（必须与 `go.mod` 一致）。
- Python 3，用于辅助脚本。

## 快速开始

正式下载将发布在 https://example.com。开发包只是本地产物，不是公开的签名发布版；请按官网说明校验签名和校验和。

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

请私下将漏洞报告至 support@example.com，不要公开提 issue。各版本的安全审查保存在
[docs/security/](docs/security/README.md)。

## 致谢

基于 [MyGo](https://github.com/egoist/mygo)；依赖声明见 [THIRD_PARTY.md](THIRD_PARTY.md)。

## 许可证

专有软件，保留所有权利。[LICENSE](LICENSE) 包含服务条款，将发布在 https://example.com/terms。
