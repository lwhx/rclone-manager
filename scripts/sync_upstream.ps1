#Requires -Version 5.1
<#
.SYNOPSIS
    同步上游仓库更新并刷新中文翻译
.DESCRIPTION
    从上游仓库拉取更新，合并到本地，更新中文翻译，并推送到你的 fork
#>

[CmdletBinding()]
param()

$ErrorActionPreference = "Stop"

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  同步上游仓库更新" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

try {
    # 步骤 1: 获取上游更新
    Write-Host "[1/5] 获取上游更新..." -ForegroundColor Yellow
    git fetch upstream
    if ($LASTEXITCODE -ne 0) {
        throw "获取上游更新失败"
    }

    # 步骤 2: 合并上游更新
    Write-Host ""
    Write-Host "[2/5] 合并上游更新到本地..." -ForegroundColor Yellow
    git merge upstream/master --no-edit
    if ($LASTEXITCODE -ne 0) {
        Write-Host ""
        Write-Host "警告: 合并出现冲突，请手动解决" -ForegroundColor Red
        Write-Host "解决冲突后运行: git add -A; git commit -m 'sync: merge upstream updates'" -ForegroundColor Yellow
        Read-Host "按 Enter 键退出"
        exit 1
    }

    # 步骤 3: 更新中文翻译
    Write-Host ""
    Write-Host "[3/5] 更新中文翻译文件..." -ForegroundColor Yellow
    $scriptPath = Join-Path $PSScriptRoot "create_zh_translation.py"
    python $scriptPath
    if ($LASTEXITCODE -ne 0) {
        Write-Host "警告: 翻译脚本执行失败，继续推送..." -ForegroundColor Yellow
    }

    # 步骤 4: 提交更改
    Write-Host ""
    Write-Host "[4/5] 提交更改..." -ForegroundColor Yellow
    git add -A
    $hasChanges = git diff --cached --quiet
    if ($LASTEXITCODE -ne 0) {
        git commit -m "sync: merge upstream updates and refresh translations"
        Write-Host "更改已提交" -ForegroundColor Green
    } else {
        Write-Host "没有需要提交的更改" -ForegroundColor Gray
    }

    # 步骤 5: 推送到 fork
    Write-Host ""
    Write-Host "[5/5] 推送到你的 fork..." -ForegroundColor Yellow
    git push origin master
    if ($LASTEXITCODE -ne 0) {
        throw "推送失败"
    }

    Write-Host ""
    Write-Host "========================================" -ForegroundColor Green
    Write-Host "  同步完成！" -ForegroundColor Green
    Write-Host "========================================" -ForegroundColor Green
}
catch {
    Write-Host ""
    Write-Host "错误: $_" -ForegroundColor Red
    Read-Host "按 Enter 键退出"
    exit 1
}

Read-Host "按 Enter 键退出"
