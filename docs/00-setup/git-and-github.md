# Git & GitHub Setup | Git 与 GitHub 配置

Goal: a working Git environment, a GitHub account linked by SSH key, and your first clone.

目标：装好 Git，注册 GitHub 账号并配好 SSH key，完成第一次 clone。

## 1. Install Git | 安装 Git

Download from [git-scm.com](https://git-scm.com/download/win). On Windows the installer includes **Git Bash** — use it for all commands in this repository. During setup, keep the default line-ending option (checkout Windows-style, commit Unix-style).

从 [git-scm.com](https://git-scm.com/download/win) 下载安装。Windows 安装包自带 **Git Bash**，本教程所有命令都在 Git Bash 里执行。换行符选项保持默认（检出为 Windows 风格，提交为 Unix 风格）。

```bash
git --version
# git version 2.4x.x  → 安装成功 / install OK
```

## 2. GitHub Account | 注册账号

Sign up at [github.com](https://github.com). Use a recognizable username — it will appear on every commit and PR in the org.

在 [github.com](https://github.com) 注册。用户名会出现在 org 的每次提交和 PR 上，取一个能被认出的名字。

## 3. SSH Key | 配置 SSH key

```bash
ssh-keygen -t ed25519 -C "you@example.com"   # press Enter to accept defaults / 一路回车
cat ~/.ssh/id_ed25519.pub                     # copy the whole line / 复制整行
```

GitHub → Settings → SSH and GPG keys → New SSH key, paste the public key. Then verify:

在 GitHub 的 Settings → SSH and GPG keys 中粘贴公钥，然后验证：

```bash
ssh -T git@github.com
# Hi <username>! You've successfully authenticated...  → OK
```

## 4. Clone, or Fork First | clone 与 fork

| Situation | 场景 | What to do |
| --- | --- | --- |
| You have write access to the repo | 有仓库写权限 | `git clone git@github.com:ORG/REPO.git`, then work on a branch |
| No write access (e.g. practice from outside) | 无写权限 | Click **Fork** on the repo page first, then clone your fork and open PRs from it |

## Windows Notes | Windows 注意点

- Run commands in **Git Bash**, not `cmd`/PowerShell — paths and quoting differ. / 命令统一在 Git Bash 里跑，路径和引号规则与 cmd 不同。
- If a clone fails with path-too-long errors: `git config --global core.longpaths true`. / 路径过长报错时执行此命令。
- Never edit code with Notepad; use VS Code (next doc). / 不要用记事本改代码，用 VS Code。
- Line-ending warnings (`LF will be replaced by CRLF`) are normal on Windows and can be ignored. / 换行符警告在 Windows 下属正常，可忽略。
- If `github.com` is unreachable from your network, configure your proxy in the shell before running git commands. / 网络直连不通时，先在 shell 里配置代理再执行 git 命令。

## Done When | 完成标志

- [ ] `git --version` prints a version / 输出版本号
- [ ] `ssh -T git@github.com` greets you by username / 返回你的用户名问候
- [ ] You cloned at least one org repository / 成功 clone 至少一个 org 仓库
- [ ] You know whether you should branch or fork / 清楚自己该开分支还是先 fork
