# API Specification

> API endpoints and interfaces

## API Endpoints

| Endpoint | Method | Description | Parameters | Response | Status |
|----------|--------|-------------|------------|----------|--------|
| /api/users | GET | Get user list | page, limit | User[] | 🔴 Not Started |
| /api/users/:id | GET | Get single user | id | User | 🔴 Not Started |
| /api/users | POST | Create user | name, email, role | User | 🔴 Not Started |
| /api/users/:id | PUT | Update user | id, name, email, role | User | 🔴 Not Started |
| /api/users/:id | DELETE | Delete user | id | void | 🔴 Not Started |
| | | | | | |

## API Endpoint Template

```markdown
| /api/xxx | GET/POST/PUT/DELETE | [Description] | [Parameters] | [Response Type] | 🔴 Not Started |
```

## Authentication

| Type | Description | Implementation |
|------|-------------|----------------|
| [JWT / OAuth 2.0 / API Key] | [Description] | [To be implemented] |

## Error Codes

| Code | Description |
|------|-------------|
| 200 | Success |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 500 | Internal Server Error |

---

**Last Updated**: YYYY-MM-DD HH:MM
**Updated By**: [Name]
