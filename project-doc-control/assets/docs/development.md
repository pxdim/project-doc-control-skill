# Development Guidelines

> Coding standards, Git workflow, and code review

## Code Standards

| Item | Standard | Tool | Status |
|------|----------|-------|--------|
| Code Style | [Airbnb / Standard / Google] | ESLint / Prettier | 🔴 To Setup |
| Naming Convention | camelCase / PascalCase | | 🔴 To Setup |
| Git Convention | Conventional Commits | commitlint | 🔴 To Setup |

## Git Workflow

### Branch Naming

```bash
feature/xxx  # New feature
fix/xxx      # Bug fix
hotfix/xxx   # Emergency fix
release/xxx  # Release branch
```

### Commit Convention

```
feat: New feature
fix: Bug fix
docs: Documentation update
style: Format adjustment
refactor: Refactoring
test: Test related
chore: Build/tooling related
```

### Example Commits

```bash
feat: add user authentication
fix: resolve login timeout issue
docs: update API documentation
style: format code with prettier
refactor: extract user service
test: add unit tests for auth
chore: update dependencies
```

## Code Review Process

| Step | Description | Owner |
|------|-------------|-------|
| 1 | Developer creates PR | Developer |
| 2 | At least one reviewer reviews | Reviewer |
| 3 | All CI checks pass | System |
| 4 | Reviewer approves | Reviewer |
| 5 | Merge to main branch | Developer |

## Code Review Checklist

- [ ] Code follows project style guide
- [ ] Tests are included/updated
- [ ] Documentation is updated
- [ ] No console.log or debug code
- [ ] Error handling is proper
- [ ] Security issues are addressed

---

**Last Updated**: YYYY-MM-DD HH:MM
**Updated By**: [Name]
