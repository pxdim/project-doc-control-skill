# Installation Guide

安裝指南 / 安裝指南

---

## 繁體中文

### 系統需求

- Claude Code 已安裝
- 終端機存取權限

### 安裝步驟

#### 方式一：一鍵安裝（推薦）

在終端機執行以下指令：

```bash
curl -L https://github.com/pxdim/project-doc-control-skill/raw/main/project-doc-control.skill -o ~/.claude/skills/project-doc-control.skill
```

#### 方式二：手動下載

1. 前往 [Releases](https://github.com/pxdim/project-doc-control-skill/releases) 頁面
2. 下載 `project-doc-control.skill` 檔案
3. 將檔案複製到 `~/.claude/skills/` 目錄：

```bash
cp ~/Downloads/project-doc-control.skill ~/.claude/skills/
```

#### 方式三：從原始碼安裝

```bash
# Clone 到 skills 目錄
git clone https://github.com/pxdim/project-doc-control-skill.git ~/.claude/skills/project-doc-control

# 或下載 zip 檔
curl -L https://github.com/pxdim/project-doc-control-skill/archive/refs/heads/main.zip -o /tmp/pdc.zip
unzip -o /tmp/pdc.zip -d ~/.claude/skills/
mv ~/.claude/skills/project-doc-control-skill ~/.claude/skills/project-doc-control
```

### 驗證安裝

1. 重啟 Claude Code
2. 開啟新對話
3. 輸入：`我有哪些 skills？`
4. 確認 `project-doc-control` 在列表中

### Skills 目錄位置

| 作業系統 | 位置 | 指令 |
|----------|------|------|
| macOS / Linux | `~/.claude/skills/` | `ls ~/.claude/skills/` |
| Windows | `%USERPROFILE%\.claude\skills\` | `dir %USERPROFILE%\.claude\skills\` |

### 如何使用

安裝完成後，當你：

- ✅ 開始新專案時 → 自動建立 `docs/` 結構
- ✅ 執行開發任務前 → 自動檢查並更新文檔
- ✅ 完成任務後 → 自動記錄工作日誌
- ✅ 文檔更新後 → 詢問是否 commit & push

### 故障排除

**Q: 安裝後 skill 沒有出現？**
- 確認檔案在正確位置：`~/.claude/skills/project-doc-control.skill`
- 完全重啟 Claude Code（不只是重新載入視窗）

**Q: macOS 提示「無法驗證開發者」？**
- 在「系統偏好設定」→「安全性與隱私」允許執行
- 或使用：`xattr -d com.apple.quarantine ~/.claude/skills/project-doc-control.skill`

**Q: Windows 上 skills 目錄不存在？**
- 手動建立：`mkdir %USERPROFILE%\.claude\skills`

---

## English

### Requirements

- Claude Code installed
- Terminal access

### Installation Steps

#### Option 1: One-Line Install (Recommended)

Run this command in your terminal:

```bash
curl -L https://github.com/pxdim/project-doc-control-skill/raw/main/project-doc-control.skill -o ~/.claude/skills/project-doc-control.skill
```

#### Option 2: Manual Download

1. Go to [Releases](https://github.com/pxdim/project-doc-control-skill/releases) page
2. Download `project-doc-control.skill` file
3. Copy to `~/.claude/skills/` directory:

```bash
cp ~/Downloads/project-doc-control.skill ~/.claude/skills/
```

#### Option 3: Install from Source

```bash
# Clone to skills directory
git clone https://github.com/pxdim/project-doc-control-skill.git ~/.claude/skills/project-doc-control

# Or download zip file
curl -L https://github.com/pxdim/project-doc-control-skill/archive/refs/heads/main.zip -o /tmp/pdc.zip
unzip -o /tmp/pdc.zip -d ~/.claude/skills/
mv ~/.claude/skills/project-doc-control-skill ~/.claude/skills/project-doc-control
```

### Verify Installation

1. Restart Claude Code
2. Start a new conversation
3. Type: `What skills do I have?`
4. Confirm `project-doc-control` is in the list

### Skills Directory Location

| OS | Location | Command |
|----|----------|---------|
| macOS / Linux | `~/.claude/skills/` | `ls ~/.claude/skills/` |
| Windows | `%USERPROFILE%\.claude\skills\` | `dir %USERPROFILE%\.claude\skills\` |

### How It Works

After installation, when you:

- ✅ Start a new project → Auto-creates `docs/` structure
- ✅ Before development tasks → Auto-checks and updates docs
- ✅ After completing tasks → Auto-records work log
- ✅ After doc updates → Asks to commit & push

### Troubleshooting

**Q: Skill doesn't appear after installation?**
- Verify file is in correct location: `~/.claude/skills/project-doc-control.skill`
- Fully restart Claude Code (not just reload window)

**Q: macOS says "cannot verify developer"?**
- Allow in "System Preferences" → "Security & Privacy"
- Or run: `xattr -d com.apple.quarantine ~/.claude/skills/project-doc-control.skill`

**Q: Skills directory doesn't exist on Windows?**
- Create manually: `mkdir %USERPROFILE%\.claude\skills`
