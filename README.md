# my-first-repo

> 我的第一个 GitHub 仓库 —— 用来练习 Git / GitHub 基本操作。

## 简介

这个仓库用于记录学习过程、存放笔记和练习代码。
所有内容以 Markdown 为主，方便在手机和电脑上查看。

## 目录结构

```
.
├── README.md        # 本文件，项目说明
├── LICENSE          # MIT 许可证
├── .gitignore       # Git 忽略规则
├── docs/            # 笔记、文档
│   └── notes.md     # 学习笔记
└── src/             # 代码
    └── hello.py     # 示例脚本
```

## 快速开始

```bash
git clone https://github.com/yyi847907/my-first-repo.git
cd my-first-repo
python3 src/hello.py
```

## 常用 Git 命令

| 目的 | 命令 |
| --- | --- |
| 查看状态 | `git status` |
| 暂存全部改动 | `git add .` |
| 提交 | `git commit -m "说明"` |
| 推送 | `git push` |
| 拉取 | `git pull` |

## 在手机上操作

- 改文件：仓库页点文件 → 右上角铅笔 ✏️ → 提交
- 传文件：`Add file ▾` → `Upload files`
- 建文件：`Add file ▾` → `Create new file`（文件名写 `docs/a.md` 会自动建目录）

## 许可

[MIT](LICENSE)
