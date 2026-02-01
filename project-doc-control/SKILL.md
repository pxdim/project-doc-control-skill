---
name: project-doc-control
description: "Project documentation control system - Ensures every project has complete progress and requirements tracking with automatic Git sync. Use for creating docs folder structure on project startup, checking and updating documentation before any task, auto-recording work logs with timestamps, tracking requirements and user stories and schedule and milestones changes, auto commit and push to Git after tasks. Any project development, feature implementation, or requirement change task should use this skill."
---

# Project Documentation Control

## Core Principles

**Documentation First, Code Later.** Every project must maintain a `docs/` folder with complete documentation as the Single Source of Truth.

**Git Auto Sync.** Ask user if they want to commit & push to Git after each documentation update.

**Unified Structure.** Every project uses the same documentation structure for consistency.

## Workflow

### 1. Project Startup

When user starts a new project or enters a project directory:

1. Check if `docs/` folder exists
2. If not, create the complete `docs/` structure from templates
3. Check if `README.md` exists
4. If not, create from [README.md template](assets/README.md)
5. Guide user to fill in basic information

### 2. Before Task Execution

Before starting any development task:

1. Read relevant documentation from `docs/`
2. Confirm related requirements/user stories
3. Update [progress.md](assets/docs/progress.md) status
4. If task involves new requirements, update [requirements.md](assets/docs/requirements.md) first

### 3. After Task Execution

After completing any development task:

1. **Immediately update work-log.md** - Record:
   - Date time (format: YYYY-MM-DD HH:MM)
   - Task executed
   - Completed content
   - Modified files
2. Update related progress status
3. If requirements/specs changed, sync updates
4. Ask user if they want to commit & push to Git

### 4. When Requirements Change

When user requests to modify or add requirements:

1. Mark changes in requirements list
2. Update [changelog.md](assets/docs/changelog.md)
3. Assess impact and update [schedule.md](assets/docs/schedule.md) if needed
4. Record change reason in work log

### 5. Git Sync

**After each documentation update** (including work log, requirement status, milestones):

1. Check if it's a Git repo
2. If not, ask user if they want to initialize:
   ```bash
   git init
   git add docs/ README.md
   git commit -m "docs: initialize project documentation"
   ```
3. If repo exists, run push flow:
   - Ask user: `Do you want to commit & push documentation updates to Git?`
   - If yes, ask for commit message
   - Execute:
     ```bash
     git add docs/ README.md
     git commit -m "[user's message]"
     git push
     ```
4. If push fails (no remote), ask user if they want to set up:
   ```bash
   git remote add origin [repo URL]
   git push -u origin main
   ```

**After completing important tasks** (features, milestones):

1. Commit code along with documentation
2. Ask user for commit message
3. Run full push flow

## Documentation Structure

### Required Project Files

Every project should include:

| File | Purpose | Template |
|------|---------|----------|
| README.md | Project intro, quick start | [README.md](assets/README.md) |
| docs/ | Complete project documentation (18 files) | See below |

### docs/ Folder Structure (18 Files)

```
docs/
├── project-info.md      # Project overview, scope, status
├── requirements.md       # Functional/non-functional requirements
├── user-stories.md       # User stories with acceptance criteria
├── spec/                 # Technical specifications
│   ├── architecture.md   # System architecture, tech stack
│   ├── api.md            # API endpoints
│   └── database.md       # Database schema
├── testing.md            # Test strategy, test cases, reports
├── deployment.md         # Deployment environments, CI/CD, monitoring
├── development.md        # Code standards, Git workflow, code review
├── design.md             # UI/UX design system
├── user-manual.md        # Quick start guide, FAQ
├── milestones.md         # Project phases, deliverables
├── schedule.md           # Work timeline, time tracking
├── progress.md           # Current progress status
├── work-log.md           # Daily work log (timestamped)
├── changelog.md          # Version history
├── risks.md              # Risk register, issues
├── licenses.md           # License info, third-party packages
├── security.md           # Security checklist
└── meetings.md           # Meeting notes, action items
```

### File Descriptions

| # | File | Content |
|---|------|---------|
| 1 | project-info.md | Name, goal, scope, owner, status |
| 2 | requirements.md | Functional/non-functional requirements, priorities |
| 3 | user-stories.md | User story format, acceptance criteria |
| 4 | spec/architecture.md | Tech stack, system architecture |
| 5 | spec/api.md | API endpoints, methods, responses |
| 6 | spec/database.md | Data models, database schema |
| 7 | testing.md | Test strategy, test cases, test reports |
| 8 | deployment.md | Environments, env vars, CI/CD, monitoring |
| 9 | development.md | Code standards, Git workflow, code review |
| 10 | design.md | Design system, colors, typography |
| 11 | user-manual.md | Quick start, FAQ |
| 12 | milestones.md | Phases, deliverables |
| 13 | schedule.md | Work timeline, estimated/actual hours |
| 14 | progress.md | Overall progress, status by area |
| 15 | work-log.md | Timestamped work records |
| 16 | changelog.md | Version history |
| 17 | risks.md | Risk identification, mitigation |
| 18 | licenses.md | License info, package list |
| 19 | security.md | Security checklist |
| 20 | meetings.md | Meeting notes, action items |

## Usage

### Create New Project Documentation

```bash
# Copy the entire docs/ folder structure
cp -r assets/docs/ docs/

# Copy README template
cp assets/README.md README.md

# Edit basic information
# Fill in project name, goal, scope, etc.
```

### Check Documentation Exists

```bash
# Before starting tasks, check
ls docs/ README.md
```

### Update Work Log

Append entry to [work-log.md](docs/work-log.md):

```markdown
### 2026-02-01 14:30
- **Task**: Implement user login
- **Completed**:
  - JWT token validation
  - Login API endpoint `/api/auth/login`
  - Unit tests
- **Files Modified**: `src/auth/login.js`, `tests/auth.test.js`
- **Status**: ✅ Completed
```

### Update Requirements Status

Status labels in requirements:
- `🔴 Not Started`
- `🟡 In Progress`
- `🟢 Completed`
- `⚪ Cancelled`
- `🔵 Needs Discussion`

## Quick Reference

| File | Description |
|------|-------------|
| [README.md](assets/README.md) | Project README template |
| [docs/project-info.md](assets/docs/project-info.md) | Project info template |
| [docs/requirements.md](assets/docs/requirements.md) | Requirements template |
| [docs/user-stories.md](assets/docs/user-stories.md) | User stories template |
| [docs/spec/architecture.md](assets/docs/spec/architecture.md) | Architecture template |
| [docs/spec/api.md](assets/docs/spec/api.md) | API spec template |
| [docs/spec/database.md](assets/docs/spec/database.md) | Database template |
| [docs/testing.md](assets/docs/testing.md) | Test plan template |
| [docs/deployment.md](assets/docs/deployment.md) | Deployment template |
| [docs/development.md](assets/docs/development.md) | Development guidelines template |
| [docs/design.md](assets/docs/design.md) | Design system template |
| [docs/user-manual.md](assets/docs/user-manual.md) | User manual template |
| [docs/milestones.md](assets/docs/milestones.md) | Milestones template |
| [docs/schedule.md](assets/docs/schedule.md) | Schedule template |
| [docs/progress.md](assets/docs/progress.md) | Progress tracking template |
| [docs/work-log.md](assets/docs/work-log.md) | Work log template |
| [docs/changelog.md](assets/docs/changelog.md) | Changelog template |
| [docs/risks.md](assets/docs/risks.md) | Risks template |
| [docs/licenses.md](assets/docs/licenses.md) | Licenses template |
| [docs/security.md](assets/docs/security.md) | Security template |
| [docs/meetings.md](assets/docs/meetings.md) | Meeting notes template |

## Git Operations Guide

### Using Git Sync Script

Use the built-in Git helper script:

```bash
# Check Git status
python3 scripts/git_sync.py --check

# Initialize new repo
python3 scripts/git_sync.py --init

# Push updates
python3 scripts/git_sync.py --push "your commit message"

# Set up remote
python3 scripts/git_sync.py --remote
```

### Manual Git Commands

```bash
# Check if git repo
git status

# Initialize new repo
git init
git add docs/ README.md
git commit -m "docs: initialize project documentation"

# Set remote
git remote add origin https://github.com/username/repo.git
git push -u origin main

# Daily updates
git add docs/ README.md
git commit -m "docs: update progress [YYYY-MM-DD]"
git push
```

## Project File Structure Overview

```
project/
├── README.md              # Project intro (use template)
├── docs/                  # Complete project docs (use template)
│   ├── project-info.md
│   ├── requirements.md
│   ├── user-stories.md
│   ├── spec/
│   │   ├── architecture.md
│   │   ├── api.md
│   │   └── database.md
│   ├── testing.md
│   ├── deployment.md
│   ├── development.md
│   ├── design.md
│   ├── user-manual.md
│   ├── milestones.md
│   ├── schedule.md
│   ├── progress.md
│   ├── work-log.md
│   ├── changelog.md
│   ├── risks.md
│   ├── licenses.md
│   ├── security.md
│   └── meetings.md
├── src/                   # Source code
├── tests/                 # Test files
├── .git/                  # Git repo
└── .env.example           # Environment variables template
```
