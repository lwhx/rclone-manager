<p align="center">
  <img src="assets/App Banner.png" alt="RClone Manager">
</p>

<h1 align="center">
  RClone Manager
</h1>

<p align="center">
  <a href="README.md">🇺🇸 English</a> •
  <a href="README.tr-TR.md">🇹🇷 Türkçe</a> •
  <a href="README.zh-CN.md">🇨🇳 简体中文</a> •
  <a href="CONTRIBUTING.md#adding-translations">帮助翻译</a> •
  <a href="https://crowdin.com/project/rclone-manger">Crowdin</a>
</p>

<p align="center">
  <b>一款功能强大、跨平台的 Rclone 远程存储管理 GUI 工具。</b><br>
  <i>基于 Angular 21 + Tauri 开发 · 支持 Linux • Windows • macOS • ARM</i>
</p>

<p align="center">
  <a href="https://crowdin.com/project/rclone-manger">
    <img src="https://badges.crowdin.net/rclone-manger/localized.svg?style=for-the-badge" alt="Crowdin">
  </a>
</p>

<p align="center">
  <a href="https://hakanismail.info/zarestia/rclone-manager/docs">
    <img src="https://img.shields.io/badge/📚_文档_Wiki-blue?style=for-the-badge" alt="文档">
  </a>
  <a href="https://github.com/Zarestia-Dev/rclone-manager/releases">
    <img src="https://img.shields.io/github/v/release/Zarestia-Dev/rclone-manager?style=for-the-badge&color=2ec27e" alt="最新版本">
  </a>
</p>

<p align="center">
  <a href="https://github.com/Zarestia-Dev/rclone-manager/blob/master/LICENSE">
    <img src="https://img.shields.io/github/license/Zarestia-Dev/rclone-manager?style=flat&color=9141ac" alt="许可证">
  </a>
  <a href="https://github.com/Zarestia-Dev/rclone-manager/stargazers">
    <img src="https://img.shields.io/github/stars/Zarestia-Dev/rclone-manager?style=flat&color=3584e4" alt="Stars">
  </a>
</p>

---

## 简介

**RClone Manager** 是一款**现代化的跨平台 GUI 工具**，让管理 [Rclone](https://rclone.org/) 远程存储变得轻而易举。无论是在不同云存储提供商之间同步文件、挂载远程驱动器，还是执行复杂的文件操作，RClone Manager 都能提供直观的界面，即使是最先进的 Rclone 功能也能轻松驾驭。

它还内置了**文件管理器 (Nautilus)**，让您可以优雅地浏览远程文件。您可以显示和编辑文件、移动、删除、复制和重命名文件及文件夹，还可以创建新文件夹。集成文件查看器让您可以轻松预览视频、图片、PDF、音频文件和文本文档。软件支持几乎所有文件操作，包括右键菜单和详细的属性弹窗！

> 大写的 `RC` 来自 `Rclone RC`。

<div align="center">
  
### 🌐 **需要无头模式？**

查看 **[RClone Manager Headless](headless/README.md)** – 在 Linux 服务器上作为 Web 服务器运行，无需 GUI！  
非常适合 NAS、VPS 和远程系统。可通过任何浏览器访问。🚀

</div>

定期更新，带来新功能和改进。查看我们的[路线图](https://github.com/users/Zarestia-Dev/projects/2)了解最新动态！

---

## 📸 截图

<p align="center">
  <img src="assets/desktop-ui.png" alt="桌面 UI" width="40%">
</p>

<p align="center">

|                                首页                                 |                             远程存储概览                             |                             挂载控制                             |
| :----------------------------------------------------------------: | :-----------------------------------------------------------------: | :-------------------------------------------------------------: |
| <img src="assets/general-home.png" alt="首页" width="250"/> | <img src="assets/general-remote.png" alt="远程存储概览" width="250"/> | <img src="assets/mount-control.png" alt="挂载控制" width="250"/> |

|                            任务监控                            |                             服务控制                             |                          深色模式                          |
| :------------------------------------------------------------: | :------------------------------------------------------------: | :-------------------------------------------------------: |
| <img src="assets/job-watcher.png" alt="任务监控" width="250"/> | <img src="assets/serve-control.png" alt="服务控制" width="250"/> | <img src="assets/dark-ui.png" alt="深色模式" width="250"/> |

|                      Nautilus 文件管理器                      |                            文件查看器                            |                                                             |
| :-----------------------------------------------------------: | :------------------------------------------------------------: | :--------------------------------------------------------: |
|  <img src="assets/nautilus.png" alt="Nautilus" width="250"/>    | <img src="assets/file-viewer.png" alt="文件查看器" width="250"/> |                                                            |

</p>

---

## 📦 下载

通过您喜欢的包管理器安装，或直接下载安装包。

### Linux

| 仓库              | 版本                                                                                                                                                                                     | 安装命令                                                                                                                                                             |
| :---------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **AUR**           | [![AUR 版本](https://img.shields.io/aur/version/rclone-manager?style=flat&label=)](https://aur.archlinux.org/packages/rclone-manager)                                                | `yay -S rclone-manager`                                                                                                                                             |
| **AUR (Git)**     | [![AUR 版本](https://img.shields.io/aur/version/rclone-manager-git?style=flat&label=)](https://aur.archlinux.org/packages/rclone-manager-git)                                        | `yay -S rclone-manager-git`                                                                                                                                         |
| **Flathub**       | [![Flathub](https://img.shields.io/flathub/v/io.github.zarestia_dev.rclone-manager?style=flat&label=&color=2ec27e)](https://flathub.org/en/apps/io.github.zarestia_dev.rclone-manager) | `flatpak install io.github.zarestia_dev.rclone-manager`                                                                                                             |
| **直接下载**      | [![最新版本](https://img.shields.io/github/v/release/Zarestia-Dev/rclone-manager?style=flat&label=&color=2ec27e)](https://github.com/Zarestia-Dev/rclone-manager/releases/latest)      | <a href="https://github.com/Zarestia-Dev/rclone-manager/releases/latest"><img src="https://img.shields.io/badge/下载-3584e4?style=flat&logo=github" alt="下载"></a> |

> 📚 **详细指南：** [Wiki: 安装 - Linux](https://hakanismail.info/zarestia/rclone-manager/docs/installation-linux)  
> _包含 Flatpak 故障排除说明。_

### macOS

| 仓库              | 版本                                                                                                                                                                                     | 安装命令                                                                                                                                                             |
| :---------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Homebrew**      | ![待定](https://img.shields.io/badge/待定-gray?style=flat)                                                                                                                              | _即将推出_                                                                                                                                                           |
| **直接下载**      | [![最新版本](https://img.shields.io/github/v/release/Zarestia-Dev/rclone-manager?style=flat&label=&color=2ec27e)](https://github.com/Zarestia-Dev/rclone-manager/releases/latest)      | <a href="https://github.com/Zarestia-Dev/rclone-manager/releases/latest"><img src="https://img.shields.io/badge/下载-3584e4?style=flat&logo=github" alt="下载"></a> |

> 📚 **详细指南：** [Wiki: 安装 - macOS](https://hakanismail.info/zarestia/rclone-manager/docs/installation-macos)  
> _重要提示：阅读此了解"应用已损坏"修复和 macFUSE 设置。_

### Windows

| 仓库              | 版本                                                                                                                                                                                     | 安装命令                                                                                                                                                             |
| :---------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Chocolatey**    | [![Chocolatey](https://img.shields.io/chocolatey/v/rclone-manager?style=flat&label=&color=2ec27e)](https://community.chocolatey.org/packages/rclone-manager)                            | `choco install rclone-manager`                                                                                                                                        |
| **Scoop**         | [![Scoop](https://img.shields.io/scoop/v/rclone-manager?bucket=extras&style=flat&label=&color=2ec27e)](https://github.com/ScoopInstaller/Extras/blob/master/bucket/rclone-manager.json) | `scoop bucket add extras` 然后 `scoop install rclone-manager`                                                                                                         |
| **Winget**        | ![Winget](https://img.shields.io/winget/v/RClone-Manager.rclone-manager?style=flat&label=&color=2ec27e)                                                                                 | `winget install RClone-Manager.rclone-manager`                                                                                                                      |
| **直接下载**      | [![最新版本](https://img.shields.io/github/v/release/Zarestia-Dev/rclone-manager?style=flat&label=&color=2ec27e)](https://github.com/Zarestia-Dev/rclone-manager/releases/latest)      | <a href="https://github.com/Zarestia-Dev/rclone-manager/releases/latest"><img src="https://img.shields.io/badge/下载-3584e4?style=flat&logo=github" alt="下载"></a> |

> 📚 **详细指南：** [Wiki: 安装 - Windows](https://hakanismail.info/zarestia/rclone-manager/docs/installation-windows)  
> _包含 WinFsp（挂载必需）和 SmartScreen 说明。_

---

## 🛠️ 系统要求

RClone Manager 会自动处理大部分依赖项。

- **Rclone：** 如果缺失，应用会自动为您下载。
- **挂载（可选）：** 需要 **WinFsp**（Windows）、**macFUSE**（macOS）或 **FUSE3**（Linux）。
- **详细信息：** 参阅 [Wiki: 系统要求](https://hakanismail.info/zarestia/rclone-manager/docs/Installation#%EF%B8%8F-dependencies) 了解完整的兼容性说明。

---

## 🛠️ 开发

要从源码构建（桌面版、无头版、Docker 或 Flatpak），请参阅 **[构建指南](https://hakanismail.info/zarestia/rclone-manager/docs/building)**。

### 代码规范与格式化

- 参阅 [**LINTING.md**](LINTING.md) 了解保持代码质量的说明。

---

## 🐞 故障排除

遇到问题了？

1.  查看 **[故障排除 Wiki](https://hakanismail.info/zarestia/rclone-manager/docs/troubleshooting)** 了解常见修复方法（挂载错误、权限、应用启动问题）。
2.  查阅 [**ISSUES.md**](ISSUES.md) 了解平台特定的已知限制。
3.  访问 [**GitHub 项目看板**](https://github.com/users/Zarestia-Dev/projects/2) 查看我们正在开发的内容。

---

## 🤝 贡献

欢迎贡献！以下是您可以提供帮助的方式：

- 🌍 **帮助翻译** – 查看[翻译指南](CONTRIBUTING.md#adding-translations)
- 🐛 **报告错误** – [提交错误报告](https://github.com/Zarestia-Dev/rclone-manager/issues/new?template=bug_report.md)
- 💡 **建议功能** – [分享您的想法](https://github.com/Zarestia-Dev/rclone-manager/issues/new?template=feature_request.md)
- 📖 **改进文档** – 帮助我们让[文档](https://hakanismail.info/zarestia/rclone-manager/docs)更加清晰
- 🔧 **提交 PR** – 查看 [CONTRIBUTING.md](CONTRIBUTING.md)
- 💬 **参与讨论** – 加入 [GitHub Discussions](https://github.com/Zarestia-Dev/rclone-manager/discussions)

---

## 📜 许可证

基于 **[GNU GPLv3](LICENSE)** 许可证 – 免费使用、修改和分发。

---

## ⭐ 支持项目

- 给仓库 **Star** 和 **Watch** 以获取最新发布通知
- 分享给朋友，让更多人知道！

---

<p align="center">
  由 Zarestia Dev 团队 ❤️ 开发<br>
  <sub>由 Rclone 提供支持 | 基于 Angular & Tauri 构建</sub>
</p>
