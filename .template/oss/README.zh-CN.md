<div align="center">

# Template

使用 Go 和 MyGo 原生 UI 编写的桌面应用。

[![CI](https://github.com/ydongy/template/actions/workflows/ci.yml/badge.svg)](https://github.com/ydongy/template/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Go](https://img.shields.io/badge/go-1.27.1-00ADD8.svg)](.go-version)
[![Website](https://img.shields.io/badge/website-example.com-informational.svg)](https://example.com)

[English](README.md) · **简体中文**

</div>

Template 是使用 Go 和 [MyGo](https://github.com/egoist/mygo) 原生 UI 编写的桌面应用。当前是一个计数器演示，请替换成你自己的应用。

## 功能特性

- 单一原生窗口，支持 macOS 12+、Windows 10/11 和带 GTK 3 的 Linux（amd64 与 arm64）；无 WebView、HTML 或 Node。
- 跟随系统语言，所有界面文字都在内嵌的文案目录中。
- 支持原生更新窗口。
- 成文的设计语言（[docs/design.md](docs/design.md)）、[设计令牌](design/tokens.md)，以及亮/暗两种外观的[原型](design/screens/example-appearance.html)。

## 环境要求

- Go：版本见 [.go-version](.go-version)（必须与 `go.mod` 一致）。
- Python 3，用于辅助脚本。

## 快速开始

正式下载将发布在 https://example.com。首个版本发布前请自行构建：

```bash
go tool mygo dev     # 运行应用
go tool mygo build   # 为当前平台打包
```

## 开发

```bash
scripts/check.sh --cross   # gofmt、go mod tidy、vet、测试、脚本测试、交叉编译
go test -race ./...
```

## 参与贡献

请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。提交信息和 Pull Request 标题遵循
[Conventional Commits](https://www.conventionalcommits.org/)。

## 安全

请通过 GitHub 私下报告漏洞：**Security → Report a vulnerability**，或访问
<https://github.com/ydongy/template/security/advisories/new>。

## 致谢

基于 [MyGo](https://github.com/egoist/mygo)；依赖声明见 [THIRD_PARTY.md](THIRD_PARTY.md)。

## 许可证

[MIT](LICENSE)。
