#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
创建中文语言翻译文件
此脚本会读取英文翻译文件并创建中文翻译
"""

import json
import os

def load_json(file_path):
    """加载 JSON 文件"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(file_path, data):
    """保存 JSON 文件"""
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def create_zh_translation():
    """创建中文翻译"""
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    en_dir = os.path.join(project_root, 'resources', 'i18n', 'en-US')
    zh_dir = os.path.join(project_root, 'resources', 'i18n', 'zh-CN')
    
    # 确保中文目录存在
    os.makedirs(zh_dir, exist_ok=True)
    
    # 翻译映射 - 完整的翻译字典
    translations = {
        "common": {
            "cancel": "取消",
            "save": "保存",
            "ok": "确定",
            "close": "关闭",
            "nextStep": "下一步",
            "back": "返回",
            "continue": "继续",
            "yes": "是",
            "no": "否",
            "loading": "加载中...",
            "error": "错误",
            "success": "成功",
            "refresh": "刷新",
            "browse": "浏览",
            "delete": "删除",
            "edit": "编辑",
            "copy": "复制",
            "move": "移动",
            "retry": "重试",
            "default": "默认",
            "copyErrorFailed": "复制错误失败",
            "errorCopied": "错误已复制到剪贴板",
            "required": "此字段为必填项"
        },
        "validators": {
            "integer": "必须是有效的整数",
            "float": "必须是有效的十进制数",
            "duration": "无效的持续时间格式。使用: 1h30m45s, 5m, 1h",
            "sizeSuffix": "无效的大小格式。使用: 100Ki, 16Mi, 1Gi, 或 \"off\"",
            "tristate": "值必须为 true、false 或未设置",
            "time": "无效的日期时间格式。使用 ISO 8601: YYYY-MM-DDTHH:mm:ssZ",
            "spaceSepList": "列表不能只包含空白字符",
            "bwTimetable": "无效的带宽格式",
            "fileMode": "必须是八进制格式 (3-4 位数字,每个 0-7)。示例: 755",
            "enum": "必须是以下之一: {{values}}",
            "invalidPath": "路径必须是绝对路径",
            "urlArray": "所有 URL 必须有效且以 http:// 或 https:// 开头",
            "bandwidth": "无效的带宽格式。使用: 10M, 1G, 100K 或组合格式",
            "passwordMismatch": "密码不匹配",
            "remoteName": {
                "invalidChars": "远程名称包含无效字符",
                "invalidStart": "远程名称不能以连字符或空格开头",
                "invalidEnd": "远程名称不能以空格结尾",
                "nameTaken": "此远程名称已被使用"
            },
            "password": {
                "minLength": "密码至少需要 3 个字符",
                "invalidChars": "密码不能包含引号"
            }
        },
        "mount": {
            "notMounted": "未挂载",
            "mounted": "已挂载",
            "mountedWithProfile": "已挂载: {{profile}}",
            "mountedMultiple": "已挂载 ({{count}}): {{profiles}}",
            "mountedSummary": "已挂载 ({{count}})",
            "toggleAction": "切换挂载为快速操作",
            "successMount": "成功挂载 {{remote}} ({{profile}})",
            "failedMount": "挂载 {{remote}} 失败: {{error}}",
            "successUnmount": "成功卸载 {{remote}}",
            "failedUnmount": "卸载 {{remote}} 失败: {{error}}"
        },
        "sync": {
            "available": "可用的同步操作",
            "syncing": "同步中",
            "copying": "复制中",
            "moving": "移动中",
            "bisyncActive": "双向同步活跃",
            "syncSummary": "同步中 ({{count}})",
            "syncWithProfile": "同步: {{profiles}}",
            "copyWithProfile": "复制: {{profiles}}",
            "moveWithProfile": "移动: {{profiles}}",
            "bisyncWithProfile": "双向同步: {{profiles}}",
            "toggleSync": "切换同步为快速操作",
            "toggleCopy": "切换复制为快速操作",
            "toggleMove": "切换移动为快速操作",
            "toggleBisync": "切换双向同步为快速操作"
        },
        "serve": {
            "noActive": "无活跃服务",
            "serving": "服务中",
            "servingWithProfile": "服务中 ({{profile}}): {{type}} 在 {{addr}}",
            "servingMultiple": "服务中 ({{count}}): {{profiles}}",
            "serveSummary": "服务中 ({{count}})",
            "profileInfo": "{{profile}} ({{type}})",
            "toggleAction": "切换服务为快速操作",
            "successStart": "成功启动 {{remote}} 的服务 ({{profile}}) 在 {{addr}}",
            "failedStart": "启动 {{remote}} 的服务失败: {{error}}",
            "successStop": "成功停止服务 {{id}}",
            "failedStop": "停止服务 {{id}} 失败: {{error}}",
            "successStopAll": "成功停止所有服务",
            "failedStopAll": "停止所有服务失败: {{error}}"
        },
        "task": {
            "status": {
                "enabled": "已启用",
                "disabled": "已禁用",
                "running": "运行中",
                "failed": "失败",
                "stopping": "正在停止"
            },
            "toggle": {
                "enable": "启用任务",
                "disable": "禁用任务",
                "stopping": "任务正在停止..."
            },
            "nextRun": {
                "disabled": "任务已禁用",
                "stopping": "在当前运行后禁用",
                "notScheduled": "未计划"
            },
            "lastRun": {
                "never": "从不"
            }
        },
        "actions": {
            "mount": "挂载",
            "sync": "同步",
            "copy": "复制",
            "move": "移动",
            "bisync": "双向同步",
            "serve": "服务",
            "start": "开始",
            "stop": "停止"
        },
        "sidebar": {
            "toggleSearch": "切换搜索栏",
            "remotes": "远程存储",
            "searchPlaceholder": "搜索远程存储...",
            "searchAriaLabel": "搜索远程存储",
            "noRemotesFound": "未找到匹配 \"{{term}}\" 的远程存储",
            "noRemotesConfigured": "未配置远程存储",
            "aria": {
                "mountStatus": "挂载状态",
                "syncStatus": "同步操作状态",
                "serveStatus": "服务状态"
            }
        },
        "detailShared": {
            "jobInfo": {
                "title": "任务信息",
                "type": "任务类型",
                "id": "任务 ID",
                "started": "开始时间",
                "lastOperation": "上次操作",
                "emptyTitle": "无活跃任务",
                "emptyMessage": "操作开始时任务详情将显示在此处"
            },
            "diskUsage": {
                "title": "磁盘使用情况",
                "notSupported": "不支持",
                "unknown": "未知",
                "total": "总计: {{value}}",
                "used": "已使用: {{value}}",
                "free": "可用: {{value}}",
                "errorLoading": "加载磁盘使用情况时出错"
            },
            "status": {
                "mounted": "已挂载",
                "notMounted": "未挂载",
                "syncing": "同步中",
                "bisyncing": "双向同步中",
                "moving": "移动中",
                "copying": "复制中",
                "serving": "服务中",
                "stopped": "已停止"
            },
            "stats": {
                "emptyTitle": "无可用统计信息",
                "emptyMessage": "运行操作时将显示统计信息"
            },
            "pathDisplay": {
                "source": "源",
                "destination": "目标",
                "openInExplorer": "在文件资源管理器中打开"
            },
            "jobs": {
                "activeJobs": "活跃任务",
                "columns": {
                    "type": "类型",
                    "profile": "配置",
                    "status": "状态",
                    "progress": "进度",
                    "started": "开始时间",
                    "actions": "操作"
                },
                "status": {
                    "running": "运行中",
                    "completed": "已完成",
                    "failed": "失败",
                    "stopped": "已停止",
                    "unknown": "未知"
                },
                "actions": {
                    "stop": "停止任务",
                    "delete": "删除任务"
                },
                "empty": "无活跃任务"
            },
            "settings": {
                "metrics": "{{count}} 个设置",
                "notConfigured": "未配置",
                "noData": "无可用配置数据",
                "edit": "编辑设置",
                "restricted": "受限",
                "invalidJson": "[无效的 JSON]"
            }
        },
        "rcloneUpdate": {
            "success": "Rclone 更新成功 ({{channel}} 频道)",
            "failed": "更新失败",
            "channelChanged": "Rclone 更新频道已更改为 {{channel}}",
            "channelSaveFailed": "保存 Rclone 更新频道失败",
            "skipped": "Rclone 版本 {{version}} 已跳过",
            "skipFailed": "跳过 Rclone 更新失败",
            "restored": "Rclone 版本 {{version}} 已恢复",
            "restoreFailed": "恢复 Rclone 更新失败",
            "autoCheckEnabled": "Rclone 自动检查更新已启用",
            "autoCheckDisabled": "Rclone 自动检查更新已禁用",
            "settingsSaveFailed": "保存 Rclone 更新设置失败"
        },
        "settings": {
            "resetToDefault": "重置为默认值",
            "resetAll": {
                "title": "重置设置",
                "message": "确定要重置所有应用设置吗?此操作无法撤销。"
            },
            "resetSuccess": "设置重置成功",
            "resetFailed": "将 {{key}} 重置为默认值失败。",
            "loadFailed": "无法加载应用设置。",
            "remoteResetSuccess": "{{remote}} 的设置重置成功",
            "general": {
                "tray_enabled": {
                    "label": "启用托盘图标",
                    "description": "在系统托盘中显示图标。同时也启用后台服务。"
                },
                "language": {
                    "label": "语言",
                    "description": "用户界面使用的语言。默认使用系统语言。"
                },
                "start_on_startup": {
                    "label": "开机自启",
                    "description": "系统启动时自动启动应用。"
                },
                "notifications": {
                    "label": "启用通知",
                    "description": "显示挂载事件的通知。"
                },
                "restrict": {
                    "label": "限制值",
                    "description": "出于安全目的限制某些特定值(例如 Token、Client ID 等)"
                }
            },
            "core": {
                "max_tray_items": {
                    "label": "托盘项目最大数量",
                    "description": "托盘中显示的最大项目数 (1-40)。"
                },
                "connection_check_urls": {
                    "label": "连接检查 URL",
                    "description": "用于验证互联网连接的 URL 列表。应用会定期检查这些 URL。"
                },
                "rclone_path": {
                    "label": "Rclone 二进制文件路径",
                    "description": "Rclone 二进制文件或目录的路径。留空以自动检测。"
                },
                "rclone_flags": {
                    "label": "额外的 Rclone 参数",
                    "description": "为 rclone 进程添加额外的参数(例如 --cache-dir=/path/to/cache)。某些参数是保留的。"
                },
                "bandwidth_limit": {
                    "label": "带宽限制",
                    "description": "限制 Rclone 传输使用的带宽。格式: '上传:下载'",
                    "placeholder": "例如: 10M:5M 或 1G"
                },
                "completed_onboarding": {
                    "label": "已完成入门",
                    "description": "表示入门流程是否已完成。"
                }
            },
            "developer": {
                "log_level": {
                    "label": "日志级别",
                    "description": "控制记录哪些日志消息。级别越高,详细信息越多。",
                    "options": {
                        "error": "仅错误",
                        "warn": "警告和错误",
                        "info": "信息(推荐)",
                        "debug": "调试(详细)",
                        "trace": "跟踪(全部,包括库日志)"
                    }
                },
                "destroy_window_on_close": {
                    "label": "内存优化",
                    "description": "关闭时销毁窗口 UI 以释放 RAM。实验性功能。"
                }
            },
            "runtime": {
                "theme": {
                    "label": "应用主题",
                    "options": {
                        "system": "系统",
                        "light": "浅色",
                        "dark": "深色"
                    }
                },
                "app_auto_check_updates": {
                    "label": "自动检查应用更新",
                    "description": "自动检查应用更新。"
                },
                "app_skipped_updates": {
                    "label": "跳过的应用更新",
                    "description": "已跳过的应用版本列表。"
                },
                "app_update_channel": {
                    "label": "应用更新频道",
                    "options": {
                        "stable": "稳定版",
                        "beta": "测试版"
                    }
                },
                "rclone_auto_check_updates": {
                    "label": "自动检查 Rclone 更新",
                    "description": "自动检查 Rclone 更新。"
                },
                "rclone_skipped_updates": {
                    "label": "跳过的 Rclone 更新",
                    "description": "已跳过的 Rclone 版本列表。"
                },
                "rclone_update_channel": {
                    "label": "Rclone 更新频道",
                    "options": {
                        "stable": "稳定版",
                        "beta": "测试版"
                    }
                },
                "flatpak_warn": {
                    "label": "已显示 Flatpak 警告"
                },
                "dashboard_layout": {
                    "label": "仪表板布局",
                    "description": "仪表板的自定义布局配置。"
                }
            },
            "nautilus": {
                "default_layout": {
                    "label": "默认布局",
                    "description": "文件浏览器的默认视图布局。",
                    "options": {
                        "grid": "网格",
                        "list": "列表"
                    }
                },
                "grid_icon_size": {
                    "label": "网格图标大小",
                    "description": "首选网格图标大小(像素)。"
                },
                "list_icon_size": {
                    "label": "列表图标大小",
                    "description": "首选列表图标大小(像素)。"
                },
                "show_hidden_items": {
                    "label": "显示隐藏文件",
                    "description": "在文件浏览器中默认显示以点开头的文件。"
                },
                "sort_key": {
                    "label": "默认排序顺序",
                    "options": {
                        "name-asc": "名称 (A-Z)",
                        "name-desc": "名称 (Z-A)",
                        "size-asc": "大小 (小-大)",
                        "size-desc": "大小 (大-小)",
                        "date-asc": "日期 (旧-新)",
                        "date-desc": "日期 (新-旧)"
                    }
                },
                "starred": {
                    "label": "收藏项",
                    "description": "文件浏览器中的收藏文件和文件夹列表。"
                },
                "bookmarks": {
                    "label": "书签",
                    "description": "快速访问的收藏位置列表。"
                }
            }
        },
        "banners": {
            "development": {
                "title": "开发版本",
                "subtitle": "功能可能不稳定 • 可能导致数据丢失 • 不适用于生产环境"
            },
            "flatpak": {
                "title": "Flatpak 说明",
                "subtitle": "某些功能可能需要手动调整权限。",
                "learnMore": "了解更多",
                "dismissTooltip": "不再显示"
            },
            "metered": {
                "message": "您使用的是计量连接。某些功能可能会使用额外数据。"
            },
            "engine": {
                "password": {
                    "title": "需要 Rclone 配置密码",
                    "subtitle": "请解锁配置以启动引擎"
                },
                "path": {
                    "title": "未找到 Rclone 二进制文件",
                    "subtitle": "请检查设置中的 rclone 安装路径"
                },
                "generic": {
                    "title": "引擎启动失败",
                    "subtitle": "请检查日志以获取更多详细信息"
                }
            }
        },
        "tabs": {
            "general": "常规",
            "mount": "挂载",
            "sync": "同步",
            "serve": "服务"
        },
        "titlebar": {
            "addRemoteMenu": "添加远程菜单",
            "home": "主页",
            "internetStatus": "互联网连接状态",
            "appMenu": "应用菜单",
            "minimize": "最小化窗口",
            "maximize": "最大化窗口",
            "close": "关闭窗口",
            "connection": {
                "checking": "检查互联网连接...",
                "online": "您的互联网连接正常工作。",
                "offline": "无法连接到: {{services}}。某些功能可能无法正常工作。点击重试。"
            },
            "updates": {
                "all": "应用和 Rclone 更新可用",
                "app": "应用更新可用",
                "rclone": "Rclone 更新可用",
                "restart": "需要重启以完成更新"
            },
            "menu": {
                "theme": "主题选择",
                "system": "系统主题",
                "light": "浅色主题",
                "dark": "深色主题",
                "import": "导入",
                "export": "导出",
                "preferences": "首选项",
                "configuration": "配置",
                "fileBrowser": "文件浏览器",
                "shortcuts": "键盘快捷键",
                "about": "关于 RClone Manager",
                "quickRemote": "快速远程",
                "detailedRemote": "详细远程"
            }
        },
        "onboarding": {
            "loadingTitle": "正在初始化 RClone Manager",
            "loadingMessage": "正在检查系统配置...",
            "cards": {
                "welcome": {
                    "title": "欢迎使用 RClone Manager",
                    "content": "您的现代化云存储管理解决方案。RClone Manager 提供直观的界面,可轻松同步、挂载和管理所有云远程存储。"
                },
                "features": {
                    "title": "强大功能",
                    "content": "无缝同步文件、将云存储挂载为本地驱动器、管理多个远程存储、监控传输操作 - 所有功能都在一个精美的界面中完成。"
                },
                "installRclone": {
                    "title": "安装 RClone",
                    "content": "RClone 是云存储操作所必需的。选择您偏好的安装位置或二进制文件位置,我们将自动处理设置。"
                },
                "installPlugin": {
                    "title": "安装挂载插件",
                    "content": "挂载插件可让您将云存储挂载为本地驱动器。此可选组件可增强您的 RClone 体验。"
                },
                "selectConfig": {
                    "title": "选择 RClone 配置",
                    "content": "选择要使用的 RClone 配置文件:默认位置或自定义配置文件。"
                },
                "passwordRequired": {
                    "title": "需要配置密码",
                    "content": "您的 rclone 配置已加密。请输入密码以解锁此会话。"
                },
                "ready": {
                    "title": "准备就绪!",
                    "content": "一切设置完成并准备好使用。RClone Manager 将帮助您轻松管理云存储。点击\"开始使用\"开始您的旅程。"
                }
            },
            "installButton": {
                "configuring": "配置中...",
                "installing": "安装中...",
                "selectPath": "请先选择路径",
                "selectBinary": "请先选择二进制文件",
                "invalidBinary": "无效的二进制文件",
                "testingBinary": "正在测试二进制文件...",
                "useBinary": "使用此二进制文件",
                "testBinary": "请先测试二进制文件",
                "install": "安装 RClone"
            },
            "options": {
                "recommended": "推荐",
                "custom": "自定义",
                "existing": "现有",
                "default": "默认"
            },
            "actions": {
                "back": "返回",
                "next": "下一步",
                "installPlugin": "安装插件",
                "installingPlugin": "安装中...",
                "unlock": "解锁",
                "getStarted": "开始使用"
            },
            "validation": {
                "completeInstallation": "请完成上述安装选项",
                "selectConfig": "请先选择或提供有效的配置选项",
                "wrongPassword": "密码错误。请重试。"
            }
        },
        "shared": {
            "search": {
                "toggle": "切换搜索",
                "placeholder": "搜索...",
                "ariaLabel": "搜索",
                "title": "未找到结果",
                "description": "没有选项匹配您的搜索",
                "action": "清除搜索",
                "hideSearch": "隐藏搜索",
                "showSearch": "显示搜索",
                "hide": "隐藏搜索",
                "show": "显示搜索"
            },
            "installationOptions": {
                "tabs": {
                    "quickFix": "推荐",
                    "custom": "自定义",
                    "existing": "现有"
                },
                "browse": "浏览",
                "testingAction": "正在测试...",
                "test": "测试",
                "existingBinaryPlaceholder": "/path/to/rclone",
                "status": {
                    "untested": "未测试",
                    "testing": "正在测试...",
                    "valid": "有效的二进制文件",
                    "invalid": "无效的二进制文件"
                },
                "errors": {
                    "invalidPath": "请输入有效的绝对路径",
                    "required": "此字段为必填项"
                },
                "modes": {
                    "install": {
                        "default": {
                            "description": "使用标准安装位置。",
                            "recommendation": "推荐给大多数用户。"
                        },
                        "custom": {
                            "description": "选择自定义安装路径。",
                            "label": "安装路径",
                            "placeholder": "/path/to/install"
                        },
                        "existing": {
                            "description": "使用现有的 rclone 二进制文件。",
                            "label": "二进制文件路径"
                        }
                    },
                    "config": {
                        "default": {
                            "description": "使用默认的 rclone 配置文件位置。",
                            "recommendation": "如果您没有自定义配置,请选择此项。"
                        },
                        "custom": {
                            "description": "选择自定义 rclone 配置文件。",
                            "label": "配置文件",
                            "placeholder": "/path/to/rclone.conf"
                        },
                        "existing": {
                            "description": "使用现有的 rclone 二进制文件(可选)。",
                            "label": "二进制文件路径"
                        }
                    }
                }
            },
            "transferActivity": {
                "title": "传输活动",
                "active": "活跃:",
                "recent": "最近:",
                "resetStats": "重置统计信息",
                "tabs": {
                    "active": "活跃 ({{count}})",
                    "recent": "最近 ({{count}})"
                },
                "table": {
                    "type": "类型",
                    "name": "名称",
                    "remote": "远程",
                    "status": "状态",
                    "progress": "进度",
                    "speed": "速度",
                    "eta": "预计时间",
                    "transferred": "已传输",
                    "size": "大小",
                    "errors": "错误",
                    "checks": "检查",
                    "deletes": "删除",
                    "renames": "重命名",
                    "serverCopies": "服务器复制",
                    "serverMoves": "服务器移动",
                    "lastError": "最后错误",
                    "actions": "操作",
                    "stop": "停止",
                    "view": "查看"
                },
                "empty": {
                    "active": "无活跃传输",
                    "recent": "无最近传输"
                }
            },
            "nautilus": {
                "title": "文件浏览器",
                "back": "返回",
                "forward": "前进",
                "up": "向上",
                "refresh": "刷新",
                "search": "搜索",
                "path": "路径",
                "location": "位置",
                "files": "文件",
                "folders": "文件夹",
                "size": "大小",
                "modified": "修改时间",
                "type": "类型",
                "actions": {
                    "newFolder": "新建文件夹",
                    "rename": "重命名",
                    "delete": "删除",
                    "copy": "复制",
                    "cut": "剪切",
                    "paste": "粘贴",
                    "selectAll": "全选",
                    "properties": "属性",
                    "open": "打开",
                    "openWith": "打开方式",
                    "copyPath": "复制路径",
                    "copyLocation": "复制位置",
                    "addToBookmarks": "添加到书签",
                    "removeBookmark": "移除书签",
                    "emptyTrash": "清空回收站",
                    "removeEmptyDirs": "删除空文件夹"
                },
                "notifications": {
                    "deleteStarted": "正在删除 {{count}} 个项目...",
                    "deleteComplete": "删除成功",
                    "copyStarted": "正在复制...",
                    "copyComplete": "复制完成",
                    "moveStarted": "正在移动...",
                    "moveComplete": "移动完成",
                    "renameStarted": "正在重命名...",
                    "renameComplete": "重命名完成",
                    "createFolderStarted": "正在创建文件夹...",
                    "createFolderComplete": "文件夹创建完成",
                    "emptyTrashStarted": "正在清空回收站...",
                    "emptyTrashComplete": "回收站已清空",
                    "undo": "撤销",
                    "redo": "重做",
                    "undoComplete": "撤销成功",
                    "redoComplete": "重做成功",
                    "locationCopied": "位置已复制到剪贴板",
                    "trashEmptied": "清理操作完成"
                },
                "errors": {
                    "connectionFailed": "连接失败",
                    "remoteNotFound": "未找到远程 \"{{remote}}\"",
                    "bookmarkRemoteNotFound": "书签的远程 \"{{remote}}\" 未找到",
                    "loadFailed": "加载目录失败",
                    "deleteFailed": "删除 {{count}} 个项目失败",
                    "copyFailed": "复制 {{count}} 个项目失败",
                    "moveFailed": "移动 {{count}} 个项目失败",
                    "undoFailed": "{{count}} 个项目撤销失败",
                    "redoFailed": "{{count}} 个项目重做失败",
                    "rmdirsFailed": "删除 \"{{name}}\" 中的空文件夹失败: {{error}}",
                    "createFolderFailed": "创建文件夹 \"{{name}}\" 失败: {{error}}",
                    "renameFailed": "重命名 \"{{name}}\" 失败: {{error}}",
                    "emptyTrashFailed": "清空 {{remote}} 的回收站失败: {{error}}",
                    "openFileFailed": "无法打开文件: 缺少远程服务器上下文",
                    "minSelection": "请至少选择 {{min}} 个项目。"
                },
                "modals": {
                    "delete": {
                        "title": "删除项目",
                        "messageSingle": "确定要删除 \"{{name}}\" 吗?",
                        "messageMultiple": "确定要删除 {{count}} 个项目吗?"
                    },
                    "newFolder": {
                        "title": "新建文件夹",
                        "label": "文件夹名称",
                        "placeholder": "输入文件夹名称"
                    },
                    "rename": {
                        "title": "重命名",
                        "label": "新名称",
                        "placeholder": "输入新名称",
                        "confirm": "重命名"
                    },
                    "emptyTrash": {
                        "title": "清空回收站",
                        "message": "确定要删除 {{remote}} 中的已删除项目吗?"
                    },
                    "rmdirs": {
                        "title": "删除空文件夹",
                        "message": "确定要删除 \"{{name}}\" 中的所有空文件夹吗?",
                        "confirm": "删除"
                    }
                },
                "selection": {
                    "selected": "已选择",
                    "folder": "文件夹",
                    "folders": "文件夹",
                    "item": "项目",
                    "items": "项目",
                    "otherItems": "其他项目"
                },
                "columns": {
                    "name": "名称",
                    "size": "大小",
                    "modified": "修改时间"
                },
                "empty": {
                    "noStarred": "无收藏文件",
                    "folderEmpty": "文件夹为空"
                },
                "bookmarks": {
                    "emptyHint": "无书签"
                },
                "sort": {
                    "az": "A-Z",
                    "za": "Z-A",
                    "lastModified": "最后修改",
                    "firstModified": "首次修改",
                    "sizeLargest": "大小 (从大到小)",
                    "sizeSmallest": "大小 (从小到大)",
                    "label": "排序"
                },
                "view": {
                    "iconSize": "图标大小",
                    "showHidden": "显示隐藏文件"
                },
                "notifications": {
                    "undo": "撤销",
                    "trashEmptied": "清理操作完成",
                    "locationCopied": "位置已复制到剪贴板",
                    "rmdirsStarted": "正在删除 \"{{name}}\" 中的空文件夹...",
                    "deleteStarted": "正在删除 {{count}} 个项目...",
                    "pasteComplete": "粘贴操作完成",
                    "renameStarted": "重命名操作开始",
                    "undoComplete": "撤销成功",
                    "redoComplete": "重做成功"
                }
            }
        },
        "overview": {
            "manageBackends": "管理后端",
            "resetLayout": "重置布局",
            "copyError": "点击复制错误"
        },
        "config": {
            "clearSchedule": "清除计划",
            "mountDestinationError": "挂载目标必须是本地文件夹。"
        },
        "home": {
            "emptyState": {
                "title": "RClone Manager",
                "description": "轻松管理您的 RClone 远程存储。如果您是 RClone 新手,请使用\"添加快速远程\"进行快速简单的设置。",
                "addQuickRemote": "添加快速远程",
                "addDetailedRemote": "添加详细远程"
            },
            "options": {
                "showInTray": "在托盘菜单中显示",
                "viewLogs": "查看日志",
                "cloneRemote": "克隆远程",
                "exportConfig": "导出配置",
                "resetSettings": "重置设置",
                "deleteRemote": "删除远程"
            },
            "deleteRemote": {
                "title": "删除确认",
                "message": "确定要删除 \"{{name}}\" 吗?此操作无法撤销。"
            },
            "resetRemote": {
                "title": "重置远程设置",
                "message": "确定要重置 {{name}} 的所有设置吗?"
            },
            "notifications": {
                "jobDeleted": "任务 {{id}} 删除成功。",
                "settingsReset": "{{name}} 的设置已重置。",
                "deleteRemoteSuccess": "远程 {{name}} 删除成功。"
            },
            "errors": {
                "configFailed": "配置组件失败",
                "initFailed": "初始化组件失败",
                "initialLoadFailed": "初始数据加载失败",
                "loadRemotesFailed": "加载远程存储失败",
                "updateActionsFailed": "更新快速操作失败",
                "unmountFailed": "卸载 {{name}} 失败",
                "openFailed": "打开 {{name}} 失败",
                "deleteRemoteFailed": "删除远程 {{name}} 失败",
                "startJobFailed": "为 {{name}} 启动 {{type}} 失败",
                "stopJobFailed": "为 {{name}} 停止 {{type}} 失败",
                "deleteJobFailed": "删除任务 {{id}} 失败",
                "resetSettingsFailed": "重置远程设置失败"
            }
        },
        "banner": {
            "dontShowAgain": "不再显示"
        },
        "serveCard": {
            "copyUrl": "点击复制 URL",
            "stopServe": "停止此服务"
        },
        "pathDisplay": {
            "openExplorer": "在文件资源管理器中打开"
        },
        "transfer": {
            "error": "传输错误",
            "completed": "传输完成"
        },
        "generalOverview": {
            "panels": {
                "remotes": "快速远程访问",
                "bandwidth": "带宽限制",
                "system": "系统信息",
                "jobs": "任务信息",
                "tasks": "计划任务",
                "serves": "运行中的服务"
            },
            "layout": {
                "visible": "可见",
                "hidden": "隐藏",
                "edit": "编辑布局",
                "save": "保存布局",
                "reset": "重置布局",
                "resetSuccess": "布局已重置为默认",
                "toggleTaskFailed": "切换计划任务失败"
            },
            "bandwidth": {
                "aria": {
                    "loading": "正在加载带宽信息"
                },
                "loading": "正在加载带宽信息...",
                "error": "加载带宽信息时出错",
                "retry": "重试加载带宽",
                "upload": "上传:",
                "download": "下载:",
                "total": "总计:"
            },
            "system": {
                "aria": {
                    "loading": "正在加载系统信息"
                },
                "loading": "正在加载系统信息...",
                "status": "RClone 状态:",
                "totalRemotes": "远程总数:",
                "activeJobs": "活跃任务:",
                "memoryUsage": "内存使用:",
                "uptime": "运行时间:",
                "active": "活跃",
                "inactive": "非活跃",
                "error": "错误"
            },
            "jobs": {
                "activeCount": "{{count}} 个活跃任务",
                "noActive": "无活跃任务",
                "loading": "正在加载任务信息...",
                "aria": {
                    "loading": "正在加载任务信息"
                },
                "progress": "进度:",
                "of": "共",
                "eta": "预计时间:",
                "speed": "传输速度:",
                "transfers": "传输:",
                "checks": "检查:",
                "errors": "错误:",
                "deletes": "删除:",
                "renames": "重命名:",
                "serverCopies": "服务器复制:",
                "serverMoves": "服务器移动:",
                "lastError": "最后错误:",
                "copyError": "点击复制错误",
                "noRunning": "当前无活跃任务正在运行。"
            },
            "tasks": {
                "activeCount": "{{active}} 个活跃 / {{total}} 个总计",
                "noScheduled": "无计划任务",
                "loading": "正在加载计划任务...",
                "aria": {
                    "loading": "正在加载计划任务"
                },
                "noConfigured": "未配置计划任务。使用 cron 表达式配置自动启动操作以创建计划任务。",
                "ariaLabel": "{{remote}} 的 {{type}} 计划任务。状态: {{status}}",
                "nextRun": "下次运行:",
                "lastRun": "上次运行:",
                "running": "运行中",
                "stats": {
                    "success": "成功次数",
                    "failure": "失败次数",
                    "total": "总运行次数"
                }
            },
            "serves": {
                "activeCount": "{{count}} 个活跃服务",
                "noActive": "无活跃服务",
                "loading": "正在加载运行中的服务...",
                "aria": {
                    "loading": "正在加载运行中的服务"
                },
                "noRunning": "无活跃服务正在运行。启动远程服务以通过网络协议(如 HTTP、WebDAV、FTP 或 SFTP)访问。"
            }
        },
        "appOverview": {
            "titles": {
                "mount": "挂载概览",
                "sync": "同步操作概览",
                "serve": "服务概览",
                "remotes": "远程存储概览"
            },
            "labels": {
                "mount": "挂载",
                "startSync": "开始同步",
                "startServe": "开始服务",
                "start": "开始"
            },
            "panelTitles": {
                "mountedRemotes": "已挂载的远程",
                "activeSync": "活跃同步操作",
                "activeServes": "活跃服务",
                "activeRemotes": "活跃远程",
                "unmountedRemotes": "未挂载的远程",
                "inactiveRemotes": "非活跃远程",
                "availableRemotes": "可用远程"
            }
        },
        "backendErrors": {
            "mount": {
                "pointEmpty": "挂载点不能为空",
                "alreadyMounted": "{{remote}} 已挂载到 {{mountPoint}}",
                "alreadyInUse": "挂载点 {{mountPoint}} 已被远程 {{remote}} 使用",
                "configIncomplete": "配置不完整,配置文件 \"{{profile}}\"",
                "failed": "挂载 {{remote}} 失败: {{error}}"
            },
            "sync": {
                "configIncomplete": "配置不完整,配置文件 \"{{profile}}\"",
                "sourceEmpty": "源路径不能为空",
                "destEmpty": "目标路径不能为空",
                "failed": "同步失败: {{error}}"
            },
            "serve": {
                "failed": "{{operation}} 失败: {{error}}",
                "parseFailed": "解析响应失败: {{error}}",
                "stopSuccess": "成功停止服务 {{serverId}}",
                "remoteEmpty": "远程名称不能为空",
                "typeRequired": "必须指定服务类型",
                "portInUse": "端口 {{port}} 已被使用"
            },
            "unmount": {
                "failed": "卸载 {{mountPoint}} 失败"
            },
            "request": {
                "failed": "请求失败: {{error}}"
            },
            "http": {
                "error": "HTTP {{status}}: {{body}}"
            },
            "file": {
                "driveRoot": "不能选择驱动器根目录(例如 D:\\)作为挂载点。请选择或创建一个子文件夹。",
                "folderNotEmpty": "所选文件夹不为空",
                "pickerUnavailable": "此平台不可用文件夹选择器",
                "invalidPath": "无效路径: 路径不能为空。",
                "filePickerUnavailable": "此平台不可用文件选择器"
            },
            "rclone": {
                "unsupportedPlatform": "不支持的平台",
                "downloadError": "下载 Rclone 时发生未知错误",
                "configEncrypted": "配置已加密且未提供密码",
                "unsupportedOS": "不支持的操作系统。",
                "binaryNotFound": "未找到 Rclone 二进制文件。",
                "unknownProcessType": "未知进程类型: {{type}}",
                "versionCheckFailed": "获取当前 rclone 版本失败: {{error}}",
                "restartFailed": "更新后重启引擎失败: {{error}}",
                "selfupdateFailed": "rclone selfupdate --check 失败: {{error}}",
                "unsupportedChannel": "不支持的更新频道: {{channel}}",
                "downloadFailed": "3 次尝试后下载失败: {{error}}",
                "mountHelperError": "挂载辅助程序错误: {{error}}",
                "configEncryptedLong": "Rclone 配置已加密。请先解锁。",
                "executionFailed": "执行 rclone 失败: {{error}}",
                "notFound": "未在 {{path}} 找到 Rclone 二进制文件"
            },
            "security": {
                "passwordEmpty": "密码不能为空",
                "credentialStorageUnavailable": "此平台不可用凭据存储",
                "noPasswordStored": "未存储密码",
                "encryptionUnavailable": "此平台不可用加密",
                "decryptionUnavailable": "此平台不可用解密",
                "passwordChangeUnavailable": "此平台不可用密码更改",
                "incorrectPassword": "rclone 配置密码不正确",
                "storeFailed": "存储密码失败: {{error}}",
                "encryptFailed": "加密配置失败: {{error}}",
                "decryptFailed": "解密配置失败: {{error}}",
                "changeFailed": "更改密码失败: {{error}}",
                "rcloneError": "Rclone 错误: {{error}}"
            },
            "backup": {
                "unknownFormat": "未知备份格式",
                "integrityFailed": "完整性检查失败!备份可能已损坏。",
                "encryptedPasswordRequired": "此备份已加密。需要密码。",
                "unsupportedArchive": "不支持的归档类型。必须是 .rcman 文件",
                "unsupportedCompression": "不支持的压缩: {{ext}}",
                "unknownFile": "未知文件: {{fileName}}"
            },
            "backend": {
                "nameEmpty": "后端名称不能为空",
                "cannotAddLocal": "不能添加名为 'Local' 的后端",
                "cannotRemoveLocal": "不能删除 'Local' 后端",
                "cannotRemoveActive": "不能删除活跃后端",
                "connectionFailed": "无法连接到 \"{{name}}\": {{error}}"
            },
            "job": {
                "notFound": "未找到 JobInfo",
                "monitoringFailed": "监控任务时出错过多: {{error}}",
                "executionFailed": "任务执行失败: {{error}}"
            },
            "cache": {
                "fetchRemotesFailed": "获取远程存储失败",
                "fetchConfigFailed": "获取远程存储配置失败",
                "refreshMountsFailed": "刷新已挂载的远程存储失败",
                "refreshServesFailed": "刷新服务失败"
            },
            "scheduler": {
                "taskNotEnabled": "任务未启用",
                "taskCannotRun": "任务无法运行(状态: {{status}})",
                "executionFailed": "任务执行失败: {{error}}",
                "initFailed": "初始化调度器失败: {{error}}",
                "startFailed": "启动调度器失败: {{error}}",
                "stopFailed": "停止调度器失败: {{error}}",
                "invalidCron": "无效的 cron 表达式: {{error}}",
                "taskNotFound": "未找到任务",
                "invalidTaskArgs": "任务无效: {{error}}"
            },
            "system": {
                "settingsUnavailable": "设置管理器不可用",
                "oauthNotConfigured": "OAuth 未配置",
                "unlockFailed": "解锁失败: {{error}}",
                "killFailed": "终止进程失败: {{error}}",
                "quitFailed": "退出 rclone 引擎失败: {{error}}"
            },
            "remote": {
                "httpError": "HTTP {{status}}: {{body}}",
                "configFailed": "配置远程失败: {{error}}",
                "deleteFailed": "删除远程失败: {{error}}"
            },
            "filesystem": {
                "httpError": "HTTP {{status}}: {{body}}",
                "notFound": "未找到文件"
            },
            "updater": {
                "noPending": "无待处理的更新",
                "invalidUrl": "无效 URL: {{error}}",
                "github": "GitHub API 错误: {{error}}",
                "mutex": "内部错误: {{error}}",
                "updateFailed": "更新失败: {{error}}"
            },
            "settings": {
                "loadFailed": "加载设置失败: {{error}}",
                "saveFailed": "保存设置失败: {{error}}",
                "resetFailed": "重置设置失败: {{error}}",
                "resetAllFailed": "重置所有设置失败: {{error}}",
                "eventEmitFailed": "发出设置事件失败: {{error}}",
                "subSettingsFailed": "获取子设置失败: {{error}}",
                "notFound": "未找到 \"{{name}}\" 的设置",
                "deleteFailed": "删除远程设置失败: {{error}}"
            }
        },
        "backendSuccess": {
            "mount": {
                "completed": "成功挂载 {{remote}}",
                "unmounted": "成功卸载 {{mountPoint}}",
                "allUnmounted": "所有远程存储已成功卸载"
            },
            "serve": {
                "started": "服务已在端口 {{port}} 启动",
                "stopped": "服务已停止"
            },
            "sync": {
                "completed": "同步成功完成",
                "stopped": "同步已停止"
            },
            "remote": {
                "created": "远程 {{name}} 创建成功",
                "updated": "远程 {{name}} 更新成功",
                "deleted": "远程 {{name}} 删除成功"
            },
            "backend": {
                "added": "后端 {{name}} 添加成功",
                "removed": "后端 {{name}} 移除成功",
                "updated": "后端 {{name}} 更新成功",
                "switched": "已切换到后端 {{name}}"
            },
            "backup": {
                "created": "备份创建成功",
                "restored": "备份恢复成功"
            },
            "rclone": {
                "updated": "Rclone 更新成功 ({{channel}} 频道)",
                "channelChanged": "Rclone 更新频道已更改为 {{channel}}",
                "versionSkipped": "Rclone 版本 {{version}} 已跳过",
                "versionRestored": "Rclone 版本 {{version}} 已恢复"
            },
            "job": {
                "stopped": "任务已成功停止",
                "deleted": "任务已成功删除"
            },
            "system": {
                "processKilled": "进程 {{pid}} 已成功终止",
                "shutdownInitiated": "已启动关闭",
                "servesChecked": "服务检查成功",
                "logsCleared": "远程日志已成功清除",
                "updateInstalled": "应用更新安装成功",
                "oauthQuit": "Rclone OAuth 进程已成功退出"
            },
            "settings": {
                "saved": "设置保存成功",
                "reset": "设置重置成功",
                "remoteSaved": "远程设置保存成功",
                "remoteDeleted": "远程设置删除成功",
                "optionsSaved": "RClone 后端选项保存成功",
                "optionsReset": "RClone 后端选项重置成功"
            },
            "scheduler": {
                "reloaded": "计划任务已成功重新加载",
                "cleared": "所有计划任务已成功清除"
            },
            "security": {
                "passwordRemoved": "密码已成功移除",
                "passwordValidated": "密码验证成功",
                "passwordStored": "密码存储成功",
                "unencrypted": "配置已成功解密",
                "encrypted": "配置已成功加密",
                "envSet": "配置密码环境变量设置成功",
                "passwordChanged": "配置密码已成功更改"
            }
        },
        "overviews": {
            "headers": {
                "mount": "挂载概览",
                "sync": "同步概览",
                "serve": "服务概览",
                "general": "RClone Manager",
                "default": "远程存储概览"
            },
            "status": {
                "titles": {
                    "mount": "挂载状态",
                    "sync": "同步状态",
                    "serve": "服务状态",
                    "general": "系统状态"
                },
                "labels": {
                    "unmounted": "未挂载",
                    "mounted": "已挂载",
                    "syncing": "同步中",
                    "offSync": "未同步",
                    "active": "活跃",
                    "inactive": "非活跃",
                    "off": "关闭",
                    "unknown": "未知",
                    "error": "错误"
                },
                "actions": {
                    "mount": "挂载",
                    "unmount": "卸载",
                    "start": "开始",
                    "stop": "停止"
                }
            },
            "empty": {
                "mount": "无挂载",
                "sync": "无同步操作",
                "serve": "无服务",
                "general": "无数据"
            }
        },
        "tray": {
            "showApp": "显示应用",
            "hideApp": "隐藏应用",
            "quit": "退出",
            "mountCount": "{{count}} 个挂载",
            "syncCount": "{{count}} 个同步",
            "serveCount": "{{count}} 个服务",
            "noRemotes": "无远程存储",
            "openConfig": "打开配置",
            "refresh": "刷新",
            "settings": "设置",
            "about": "关于",
            "openLogs": "打开日志",
            "stopAll": "全部停止",
            "stopAllServes": "停止所有服务",
            "stopAllMounts": "卸载所有",
            "stopAllSync": "停止所有同步",
            "quickActions": "快速操作",
            "profile": "{{profile}}",
            "status": {
                "mount": "挂载",
                "sync": "同步",
                "serve": "服务",
                "bisync": "双向同步"
            },
            "actions": {
                "mount": "挂载",
                "unmount": "卸载",
                "sync": "同步",
                "copy": "复制",
                "move": "移动",
                "bisync": "双向同步",
                "serve": "服务",
                "stop": "停止",
                "start": "开始"
            },
            "menu": {
                "remotes": "远程存储",
                "quickActions": "快速操作",
                "view": "查看",
                "tools": "工具",
                "help": "帮助"
            },
            "notification": {
                "mountSuccess": "挂载成功",
                "mountFailed": "挂载失败",
                "syncSuccess": "同步成功",
                "syncFailed": "同步失败",
                "serveSuccess": "服务启动成功",
                "serveFailed": "服务启动失败",
                "unmountSuccess": "卸载成功",
                "unmountFailed": "卸载失败"
            }
        },
        "notification": {
            "title": {
                "alreadyRunning": "应用已在运行",
                "updateAvailable": "更新可用",
                "rcloneUpdateAvailable": "Rclone 更新可用",
                "mountSuccess": "挂载成功",
                "mountFailed": "挂载失败",
                "syncSuccess": "同步成功",
                "syncFailed": "同步失败",
                "serveSuccess": "服务启动成功",
                "serveFailed": "服务启动失败",
                "unmountSuccess": "卸载成功",
                "unmountFailed": "卸载失败",
                "backupCreated": "备份创建成功",
                "backupRestored": "备份恢复成功",
                "settingsSaved": "设置保存成功",
                "error": "错误",
                "success": "成功"
            },
            "body": {
                "alreadyRunning": "应用已在运行,请使用现有实例。",
                "updateReady": "应用更新已下载,请重启以安装。",
                "rcloneUpdateReady": "Rclone 更新已下载,请重启以安装。",
                "mountSuccess": "{{remote}} 已挂载到 {{mountPoint}}",
                "mountFailed": "挂载 {{remote}} 失败: {{error}}",
                "syncSuccess": "同步任务已完成",
                "syncFailed": "同步任务失败: {{error}}",
                "serveSuccess": "服务已在 {{addr}} 启动",
                "serveFailed": "启动服务失败: {{error}}",
                "unmountSuccess": "{{mountPoint}} 已卸载",
                "unmountFailed": "卸载 {{mountPoint}} 失败: {{error}}",
                "backupCreated": "备份已创建: {{path}}",
                "backupRestored": "备份已恢复",
                "settingsSaved": "设置已保存",
                "error": "{{error}}",
                "success": "{{message}}"
            },
            "actions": {
                "restart": "重启",
                "update": "更新",
                "view": "查看",
                "close": "关闭"
            }
        },
        "developerTools": {
            "refreshUi": "刷新 UI",
            "clearCache": "清除缓存",
            "openDevTools": "打开开发者工具",
            "clearing": "正在清除数据...",
            "cleared": "数据已清除"
        }
    }
    
    # 读取英文文件以获取完整结构
    en_main = load_json(os.path.join(en_dir, 'main.json'))
    
    # 创建完整的中文翻译
    zh_main = {}
    
    # 添加已翻译的部分
    for key, value in translations.items():
        zh_main[key] = value
    
    # 为未翻译的部分使用英文作为占位符
    for key, value in en_main.items():
        if key not in zh_main:
            print(f"警告: 未翻译的键 '{key}' 将使用英文")
            zh_main[key] = value
    
    # 保存中文文件
    save_json(os.path.join(zh_dir, 'main.json'), zh_main)
    print(f"已创建 {zh_dir}\\main.json")
    
    # 翻译 rclone.json
    en_rclone = load_json(os.path.join(en_dir, 'rclone.json'))
    zh_rclone = {}
    
    # 简单翻译 rclone.json 的 key
    for key, value in en_rclone.items():
        # 这里可以添加具体的翻译逻辑
        if isinstance(value, dict) and 'title' in value and 'help' in value:
            zh_rclone[key] = {
                "title": value['title'],  # 保持英文,可以后续翻译
                "help": value['help']     # 保持英文,可以后续翻译
            }
        else:
            zh_rclone[key] = value
    
    save_json(os.path.join(zh_dir, 'rclone.json'), zh_rclone)
    print(f"已创建 {zh_dir}\\rclone.json")
    
    # 翻译 rclone-providers.json
    en_providers = load_json(os.path.join(en_dir, 'rclone-providers.json'))
    zh_providers = {}
    
    # 简单翻译 rclone-providers.json
    if 'providers' in en_providers:
        zh_providers['providers'] = {}
        for provider_name, provider_data in en_providers['providers'].items():
            zh_providers['providers'][provider_name] = {}
            for opt_name, opt_data in provider_data.items():
                if isinstance(opt_data, dict) and 'title' in opt_data and 'help' in opt_data:
                    zh_providers['providers'][provider_name][opt_name] = {
                        "title": opt_data['title'],
                        "help": opt_data['help']
                    }
                else:
                    zh_providers['providers'][provider_name][opt_name] = opt_data
    
    save_json(os.path.join(zh_dir, 'rclone-providers.json'), zh_providers)
    print(f"已创建 {zh_dir}\\rclone-providers.json")
    
    print("\n中文翻译文件创建完成!")
    print("注意: rclone.json 和 rclone-providers.json 保持英文,因为它们包含大量技术术语。")
    print("您可以后续手动翻译这些文件。")

if __name__ == '__main__':
    create_zh_translation()
