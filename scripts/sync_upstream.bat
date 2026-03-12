@echo off
chcp 65001 >nul
echo ========================================
echo  同步上游仓库更新
echo ========================================
echo.

echo [1/5] 获取上游更新...
git fetch upstream
if errorlevel 1 (
    echo 错误: 获取上游更新失败
    pause
    exit /b 1
)

echo.
echo [2/5] 合并上游更新到本地...
git merge upstream/master --no-edit
if errorlevel 1 (
    echo.
    echo 警告: 合并出现冲突，请手动解决
    echo 解决冲突后运行: git add -A ^&^& git commit -m "sync: merge upstream updates"
    pause
    exit /b 1
)

echo.
echo [3/5] 更新中文翻译文件...
python "%~dp0create_zh_translation.py"
if errorlevel 1 (
    echo 警告: 翻译脚本执行失败，继续推送...
)

echo.
echo [4/5] 提交更改...
git add -A
git diff --cached --quiet
if errorlevel 1 (
    git commit -m "sync: merge upstream updates and refresh translations"
    echo 更改已提交
) else (
    echo 没有需要提交的更改
)

echo.
echo [5/5] 推送到你的 fork...
git push origin master
if errorlevel 1 (
    echo 错误: 推送失败
    pause
    exit /b 1
)

echo.
echo ========================================
echo  同步完成！
echo ========================================
pause
