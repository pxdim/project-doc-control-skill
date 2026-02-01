# Database Design

> Database schema and data models

## Data Models

```typescript
// User model example
interface User {
  id: string;
  name: string;
  email: string;
  role: 'admin' | 'user';
  createdAt: Date;
  updatedAt: Date;
}

interface [OtherModel] {
  // Define other data models
}
```

## Database Schema

| Table | Column | Type | Description | Index |
|-------|--------|------|-------------|--------|
| users | id | UUID | Primary Key | PK |
| users | name | VARCHAR(100) | User name | |
| users | email | VARCHAR(255) | Email address | UK |
| users | role | VARCHAR(50) | User role | IDX |
| users | created_at | TIMESTAMP | Creation time | IDX |
| users | updated_at | TIMESTAMP | Last update | |
| | | | | |

## Relationships

```
┌──────────┐
│  users   │
└────┬─────┘
     │
     │ 1:N
     │
┌────▼─────┐
│ [other]  │
└──────────┘
```

## Index Strategy

| Table | Index | Type | Columns | Purpose |
|-------|-------|------|---------|---------|
| users | idx_email | UNIQUE | email | Email lookup |
| users | idx_created_at | INDEX | created_at | Time-based queries |

---

**Last Updated**: YYYY-MM-DD HH:MM
**Updated By**: [Name]
