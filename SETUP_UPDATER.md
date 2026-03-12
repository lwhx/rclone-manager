# 设置 Tauri 自动更新功能

## 快速设置步骤

### 1. 安装 minisign

**Windows:**
```powershell
choco install minisign
```

**macOS:**
```bash
brew install minisign
```

**Linux:**
```bash
sudo apt-get install minisign  # Ubuntu/Debian
sudo pacman -S minisign        # Arch
```

### 2. 生成密钥对

在项目根目录运行：

```bash
# 生成密钥对
minisign -G

# 按提示输入密码（可选，建议设置）
# 会生成两个文件：
# - minisign.pub (公钥)
# - minisign.key (私钥)
```

### 3. 配置公钥

将 `minisign.pub` 文件内容复制到 `src-tauri/tauri.conf.json`：

```json
"plugins": {
  "updater": {
    "pubkey": "你的公钥内容"
  }
}
```

### 4. 配置 GitHub Secrets

1. 打开 GitHub 仓库 → Settings → Secrets and variables → Actions
2. 点击 **New repository secret**
3. 添加以下 secrets：

| Secret 名称 | 值 |
|------------|-----|
| `TAURI_SIGNING_PRIVATE_KEY` | minisign.key 文件的全部内容 |
| `TAURI_SIGNING_PRIVATE_KEY_PASSWORD` | 生成密钥时设置的密码（如果有） |

### 5. 提交更改

```bash
git add src-tauri/tauri.conf.json
git commit -m "feat: 启用自动更新功能"
git push origin master
```

### 6. 触发构建

在 GitHub Actions 中重新运行 **Release All** 工作流。

---

## 注意事项

⚠️ **安全提醒：**
- 私钥文件 (`minisign.key`) **绝对不能** 提交到仓库
- 建议将私钥备份到安全的地方
- 如果私钥泄露，需要重新生成密钥对并更新所有配置

📦 **更新发布：**
- 每次发布新版本时，GitHub Actions 会自动签名更新包
- 用户打开应用时会自动检查更新
- 更新包会上传到 GitHub Releases

---

## 故障排除

**构建失败："incorrect updater private key password"**
- 检查 GitHub Secrets 中的 `TAURI_SIGNING_PRIVATE_KEY_PASSWORD` 是否正确

**构建失败："Missing comment in secret key"**
- 确保私钥文件内容完整，包含所有行

**更新不工作：**
- 检查公钥是否正确配置在 tauri.conf.json 中
- 确保 GitHub Releases 中有对应的更新包
