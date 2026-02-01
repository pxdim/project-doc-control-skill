# Project Doc Control Skill

[English](#english) | [繁體中文](#繁體中文)

---

## 繁體中文

### 📖 簡介

**Project Doc Control** 是一個專案文檔控制系統，確保每個專案都有完整的進度與需求追蹤，並自動同步到 Git。

### ✨ 主要功能

| 功能 | 說明 |
|------|------|
| 📁 **自動建立文檔結構** | 專案啟動時自動建立 `docs/` 資料夾，包含 20 個文檔模板 |
| 📝 **需求追蹤** | 功能需求、使用者故事、規格書完整記錄 |
| 📅 **時程管理** | 里程碑、交付物、工時追蹤 |
| 📊 **進度追蹤** | 實時更新專案進度狀態 |
| 📜 **工作日誌** | 自動記錄每次工作（含時間戳 YYYY-MM-DD HH:MM） |
| 🔄 **Git 自動同步** | 每次更新文檔後詢問是否 commit & push |
| ⚠️ **風險管理** | 風險登記、問題追蹤 |
| 🛡️ **安全合規** | 安全檢查清單 |

### 📁 文檔結構

使用此 skill 會自動建立以下文檔結構：

```
project/
├── README.md              # 專案介紹
├── docs/                  # 完整專案文檔
│   ├── project-info.md    # 專案基本資訊
│   ├── requirements.md     # 需求清單
│   ├── user-stories.md     # 使用者故事
│   ├── spec/              # 技術規格
│   │   ├── architecture.md # 系統架構
│   │   ├── api.md          # API 規格
│   │   └── database.md     # 資料庫設計
│   ├── testing.md         # 測試計畫
│   ├── deployment.md      # 部署與運維
│   ├── development.md     # 開發規範
│   ├── design.md          # UI/UX 設計
│   ├── user-manual.md     # 使用者手冊
│   ├── milestones.md      # 里程碑與交付物
│   ├── schedule.md        # 時程規劃
│   ├── progress.md        # 目前進度
│   ├── work-log.md        # 工作日誌
│   ├── changelog.md       # 版本記錄
│   ├── risks.md           # 風險與問題
│   ├── licenses.md        # 授權與套件
│   ├── security.md        # 安全合規
│   └── meetings.md        # 會議記錄
```

### 🚀 快速安裝

#### 方式一：一鍵安裝（推薦）

```bash
curl -L https://github.com/pxdim/project-doc-control-skill/raw/main/project-doc-control.skill -o ~/.claude/skills/project-doc-control.skill
```

安裝後**重啟 Claude Code**。

#### 方式二：手動安裝

1. 下載 `project-doc-control.skill` 檔案
2. 複製到 `~/.claude/skills/` 目錄
3. 重啟 Claude Code

#### 方式三：完整版（含原始碼）

```bash
git clone https://github.com/pxdim/project-doc-control-skill.git ~/.claude/skills/project-doc-control
```

### 📍 Skills 目錄位置

| 作業系統 | 位置 |
|----------|------|
| macOS / Linux | `~/.claude/skills/` |
| Windows | `%USERPROFILE%\.claude\skills\` |

### 🎯 使用方式

安裝後，當你開始新專案或執行開發任務時，skill 會自動觸發：

1. **專案啟動時**：檢查 `docs/` 是否存在，若不存在則自動建立
2. **執行任務前**：讀取相關文檔，確認需求
3. **執行任務後**：自動更新工作日誌，詢問是否 commit & push

### 🔧 使用範例

```
你：幫我建立一個使用者登入功能

Claude：我會先更新文檔...
      - 更新 requirements.md（新增登入功能需求）
      - 更新 work-log.md（記錄本次工作）
      - 詢問：是否要 commit & push 到 Git？
```

### 📚 更多資訊

- [GitHub Repo](https://github.com/pxdim/project-doc-control-skill)
- [問題回報](https://github.com/pxdim/project-doc-control-skill/issues)

### 📄 授權

MIT License

---

## English

### 📖 Overview

**Project Doc Control** is a project documentation control system that ensures every project has complete progress and requirements tracking with automatic Git sync.

### ✨ Features

| Feature | Description |
|---------|-------------|
| 📁 **Auto Doc Structure** | Automatically creates `docs/` folder with 20 template files on project startup |
| 📝 **Requirements Tracking** | Functional requirements, user stories, specifications |
| 📅 **Schedule Management** | Milestones, deliverables, time tracking |
| 📊 **Progress Tracking** | Real-time project progress status |
| 📜 **Work Log** | Auto-record every work session with timestamps (YYYY-MM-DD HH:MM) |
| 🔄 **Git Auto Sync** | Ask to commit & push after each documentation update |
| ⚠️ **Risk Management** | Risk register, issue tracking |
| 🛡️ **Security Compliance** | Security checklist |

### 📁 Documentation Structure

This skill automatically creates the following structure:

```
project/
├── README.md              # Project introduction
├── docs/                  # Complete project documentation
│   ├── project-info.md    # Project overview
│   ├── requirements.md     # Requirements list
│   ├── user-stories.md     # User stories
│   ├── spec/              # Technical specifications
│   │   ├── architecture.md # System architecture
│   │   ├── api.md          # API specs
│   │   └── database.md     # Database design
│   ├── testing.md         # Test plan
│   ├── deployment.md      # Deployment & operations
│   ├── development.md     # Development guidelines
│   ├── design.md          # UI/UX design
│   ├── user-manual.md     # User manual
│   ├── milestones.md      # Milestones & deliverables
│   ├── schedule.md        # Timeline
│   ├── progress.md        # Current progress
│   ├── work-log.md        # Work log
│   ├── changelog.md       # Version history
│   ├── risks.md           # Risks & issues
│   ├── licenses.md        # Licenses & packages
│   ├── security.md        # Security checklist
│   └── meetings.md        # Meeting notes
```

### 🚀 Quick Install

#### Option 1: One-Line Install (Recommended)

```bash
curl -L https://github.com/pxdim/project-doc-control-skill/raw/main/project-doc-control.skill -o ~/.claude/skills/project-doc-control.skill
```

**Restart Claude Code** after installation.

#### Option 2: Manual Install

1. Download `project-doc-control.skill` file
2. Copy to `~/.claude/skills/` directory
3. Restart Claude Code

#### Option 3: Full Version (with source code)

```bash
git clone https://github.com/pxdim/project-doc-control-skill.git ~/.claude/skills/project-doc-control
```

### 📍 Skills Directory Location

| OS | Location |
|----|----------|
| macOS / Linux | `~/.claude/skills/` |
| Windows | `%USERPROFILE%\.claude\skills\` |

### 🎯 How It Works

After installation, the skill automatically triggers when:

1. **Starting a project**: Checks if `docs/` exists, creates if not
2. **Before tasks**: Reads relevant docs, confirms requirements
3. **After tasks**: Updates work log, asks to commit & push

### 🔧 Usage Example

```
You: Help me build a user login feature

Claude: I'll update the documentation first...
      - Update requirements.md (add login feature)
      - Update work-log.md (record this session)
      - Ask: Do you want to commit & push to Git?
```

### 📚 More Information

- [GitHub Repo](https://github.com/pxdim/project-doc-control-skill)
- [Report Issues](https://github.com/pxdim/project-doc-control-skill/issues)

### 📄 License

MIT License
