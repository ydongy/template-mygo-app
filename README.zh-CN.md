<div align="center">

# template-mygo-app

纯 Go 桌面应用的 GitHub 模板：基于 MyGo 原生 UI，支持 macOS、Windows 和 Linux，无 WebView、HTML、Node 或 Bun。

[![CI](https://github.com/ydongy/template-mygo-app/actions/workflows/ci.yml/badge.svg)](https://github.com/ydongy/template-mygo-app/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Go](https://img.shields.io/badge/go-1.27.1-00ADD8.svg)](.go-version)

[English](README.md) · **简体中文**

</div>

本仓库是一个 **GitHub template**。在 `scripts/init.sh` 给它起真正的名字之前，产品名为 `Template`，域名为 `example.com`。

## 功能特性

- 基于 [MyGo](https://github.com/egoist/mygo) 的原生窗口，覆盖 macOS、Windows 和 Linux（amd64 与 arm64），无需前端工具链。
- 带本地化的计数器示例及交互测试，以及原生更新窗口。
- 设计体系：[设计语言](docs/design.md)（原生优先、语义色与暗色模式、组件选用、可访问性、动效、本地化）、[设计令牌](design/tokens.md)和亮/暗两种外观的[原型](design/screens/example-appearance.html)。
- 一条命令 `scripts/check.sh --cross` 完成 gofmt、`go mod tidy`、vet、测试、脚本测试和六个目标平台的交叉编译。
- 版本号脚本、脱敏的密钥扫描，以及手动触发的本地打包 workflow。
- 初始化时二选一：开源（MIT）项目，或闭源产品骨架。

## 环境要求

- Go：版本以 [.go-version](.go-version) 和 `go.mod` 为准（当前为 1.27.1），两者不一致时 `scripts/check.sh` 会报错。
- Python 3，用于辅助脚本。
- 生成的应用支持：macOS 12+、Windows 10/11、带 GTK 3 的 Linux。

## 快速开始

1. 在 GitHub 上点击 **Use this template**，创建你自己的仓库。
2. clone 后运行 `scripts/init.sh <Name> <domain>`：

   ```bash
   scripts/init.sh Acme acme.com                       # 开源项目（MIT），默认
   scripts/init.sh Acme acme.com --license proprietary # 闭源产品骨架
   ```

3. 运行 `scripts/check.sh --cross`。
4. 运行 `go tool mygo dev` 调试；用 `go tool mygo build` 在本机打包。
5. 把计数器示例换成你的应用，并在提交前检查变更文件列表。

初始化会设置 Go module 路径和反向域名标识符，安装所选 license 对应的骨架，然后删除自身。
它不会创建任何凭据，不会发布，也不会替你提交。

## 使用方法

### `scripts/init.sh` 选项

```text
scripts/init.sh <Name> <domain> [--license mit|proprietary] [--owner <github-user>] [--repo <name>]
```

| 选项 | 说明 |
|---|---|
| `<Name>` | PascalCase 产品名 |
| `<domain>` | 小写产品域名；标识符为 `<反转域名>.app`（`acme.com` 得到 `com.acme.app`） |
| `--license mit`（默认） | 开源项目，见下表 |
| `--license proprietary` | 闭源产品骨架，见下表 |
| `--owner <user>` | 用于 `CODEOWNERS` 和 module 路径的 GitHub 用户或组织；省略时从 `git remote origin` 推断，推断不出则 `CODEOWNERS` 写入占位符 `* @<owner>`，需要你补上 |
| `--repo <name>` | 仓库名（默认为小写的产品名） |

### `mit` 与 `proprietary` 的区别

| | `--license mit` | `--license proprietary` |
|---|---|---|
| `LICENSE` | MIT | 服务条款，保留所有权利 |
| `README.md` 与 `README.zh-CN.md` | 开源 README，带 MIT 徽章和 CI 徽章 | 产品 README，带 proprietary 徽章、无 CI 徽章，并附文档索引 |
| 共有文件 | `CONTRIBUTING.md`、`AGENTS.md`、`CLAUDE.md`、`CHANGELOG.md`、`CODEOWNERS`、`ci.yml`、`pr-title.yml`、Dependabot | 同样这些，措辞改为闭源版本 |
| 额外文档 | 无 | `docs/spec.md`、`legal.md`、`website.md`、`releasing.md`、`roadmap.md`、`docs/security/`、`CHANGELOG.zh.md` 和精简的 `design/README.md` |

骨架文件位于 `.template/oss/` 与 `.template/product/`。`init.py` 把其中一份覆盖到工程上，改写所有文本文件中的名称、标识符和 URL
（两份 README 同样会被改写），并删除 `.template/`、自身及其测试。生成项目的 `README.md` 与 `README.zh-CN.md`
会取代你正在读的这两份。详见 [.template/README.md](.template/README.md)。

### 生成后的目录

| 路径 | 作用 |
|---|---|
| `main.go`、`internal/ui/example/` | 原生窗口、原生更新器，以及带交互测试的本地化计数器 |
| `go.mod`、`go.sum`、`.go-version` | 固定版本的 Go、MyGo 与 CLI；无前端工具链 |
| `mygo.json`、`resources/` | 打包配置与随应用分发的依赖声明 |
| `scripts/` | 版本号、检查、脱敏密钥扫描和本地打包 |
| `docs/`、`design/` | 设计语言（`docs/design.md`）、设计令牌、原型和架构决策记录 |
| `.github/workflows/` | `ci.yml`、`pr-title.yml` 和手动触发的打包 workflow |

## 开发

```bash
scripts/check.sh --cross          # gofmt、go mod tidy、vet、测试、脚本测试、交叉编译
go test -race ./...
python3 scripts/test_init.py      # 在临时副本上对两种 license 各跑一遍 init
```

`Template`、`example.com` 和 `com.example.template` 是 `init` 会替换的占位符，请勿在本仓库任何位置写入真实产品名。

## 参与贡献

请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。提交信息和 Pull Request 标题遵循
[Conventional Commits](https://www.conventionalcommits.org/)。

## 安全

请通过 GitHub 私下报告漏洞：**Security → Report a vulnerability**，或访问
<https://github.com/ydongy/template-mygo-app/security/advisories/new>。

## 致谢

基于 [MyGo](https://github.com/egoist/mygo)；依赖声明见 [THIRD_PARTY.md](THIRD_PARTY.md)。

## 许可证

[MIT](LICENSE)。
