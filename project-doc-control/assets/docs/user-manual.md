# User Manual

> Quick start and FAQ for users

## Quick Start

### Installation

```bash
# Install dependencies
npm install

# Copy environment variables
cp .env.example .env

# Edit .env with your configuration
# vim .env
```

### Start Development Server

```bash
# Start development server
npm run dev

# Open browser to http://localhost:3000
```

### Build for Production

```bash
# Build production bundle
npm run build

# Preview production build
npm run preview
```

## Common Commands

```bash
npm run dev      # Start development server
npm run build    # Build for production
npm run test      # Run tests
npm run lint      # Run linter
npm run format    # Format code
```

## FAQ

<details>
<summary><b>Q: How do I install the project?</b></summary>

Run `npm install` to install all dependencies.
</details>

<details>
<summary><b>Q: How do I start the development server?</b></summary>

Run `npm run dev` to start the development server.
</details>

<details>
<summary><b>Q: How do I build for production?</b></summary>

Run `npm run build` to create an optimized production build.
</details>

<details>
<summary><b>Q: Where do I configure environment variables?</b></summary>

Create a `.env` file from `.env.example` and configure your variables there.
</details>

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Port already in use | Change port in `.env` or kill the process using the port |
| Module not found | Run `npm install` to install dependencies |
| Build fails | Check Node.js version (require >= 18.0.0) |

---

**Last Updated**: YYYY-MM-DD HH:MM
**Updated By**: [Name]
