<div align="center">

# Website for Team Copper

[![Deploy to Production](https://github.com/GradPace/GradPace-informational-site/actions/workflows/deploy.yml/badge.svg)](https://github.com/GradPace/GradPace-informational-site/actions/workflows/deploy.yml)
[![Build and Push to GHCR](https://github.com/GradPace/GradPace-informational-site/actions/workflows/build-and-push.yml/badge.svg)](https://github.com/GradPace/GradPace-informational-site/actions/workflows/build-and-push.yml)
[![Dependabot Updates](https://github.com/GradPace/GradPace-informational-site/actions/workflows/dependabot/dependabot-updates/badge.svg)](https://github.com/GradPace/GradPace-informational-site/actions/workflows/dependabot/dependabot-updates)

Flask web application with automatic Docker builds to GitHub Container Registry and nginx-proxy for production deployment.
</div>

## Features

- **Flask + Gunicorn** - Production-ready WSGI server
- **uv** - Fast Python package management
- **nginx-proxy** - Automatic HTTPS reverse proxy
- **GHCR** - Automated Docker image builds
- **Multi-architecture** - Supports AMD64, ARM64
- **Makefile** - Simple command interface for all operations

## Quick Start

### Local Development (Recommended: Docker)

```bash
# Run development server with Docker
make dev-docker
```

Visit http://localhost:5001

**Or run without Docker:**

*Requires [uv](https://docs.astral.sh/uv/) to be installed*

```bash
# Install dependencies
make install

# Run development server
make dev
```

Visit http://localhost:5001

**Documentation:**
- [DEVELOPMENT.md](DEVELOPMENT.md) - Development guide
- [MAKEFILE.md](MAKEFILE.md) - All available commands

## Project Structure

```
.
├── website/                      # Flask application
│   ├── main.py                  # Flask app entry point
│   ├── site_blueprints.py       # Route definitions
│   ├── templates/               # Jinja2 templates
│   ├── static/                  # CSS, JS, images
│   ├── Dockerfile               # Production Docker image
│   └── pyproject.toml           # Python dependencies (uv)
├── .github/workflows/
│   ├── build-and-push.yml       # Auto-build to GHCR on push
│   └── deploy.yml               # Auto-deploy to production server
├── docker-compose.development.yml       # Development environment
├── docker-compose.production.ghcr.yml   # Production (GHCR image)
├── Makefile                             # Command shortcuts
├── MAKEFILE.md                          # Makefile documentation
├── DEVELOPMENT.md                       # Development guide
└── .env.production                      # Production environment config
```

## Production Deployment

### First Time Setup
```bash
# Create environment file
cp .env.production.example .env.production
# Edit .env.production with your GitHub repository info:
# GITHUB_REPOSITORY=yourusername/yourrepo
```

### Deploy
```bash
make deploy
```

Pulls latest image from GHCR, updates containers, and cleans up old images.

## Configuration

### Environment Files

- `.env.production` - GitHub repository info for GHCR
  ```bash
  GITHUB_REPOSITORY=yourusername/yourrepo
  ```

### Domain Configuration

The Flask app is configured to run at `copper.steyaert.xyz` through nginx-proxy using the `VIRTUAL_HOST` environment variable in [docker-compose.production.ghcr.yml](docker-compose.production.ghcr.yml).

## Workflow

**Development:** `make dev-docker` → edit code → Flask auto-reloads (via volume mount) → refresh browser

**Deployment:** Push to GitHub → GitHub Actions builds → `make deploy` on server (or auto-deploy)

See [DEVELOPMENT.md](DEVELOPMENT.md) and [MAKEFILE.md](MAKEFILE.md) for detailed workflows and all available commands.

## Security

- **Docker Secrets**: Encrypted storage for sensitive data (e.g., Flask secret key)
- **Automatic HTTPS**: Managed by nginx-proxy with Let's Encrypt
- **Production mode**: Debug mode disabled in production
- **Environment isolation**: Separate development and production configurations

## Access

- **Production**: https://gradpace.steyaert.xyz
- **Local Dev**: http://localhost:5001

## Troubleshooting

- **View logs**: `make logs`
- **Check builds**: Repository → Actions tab
- **Port in use**: `lsof -ti:5001 | xargs kill`
- **Force redeploy**: `make compose-down && make deploy`

See [MAKEFILE.md](MAKEFILE.md) for all commands and [DEVELOPMENT.md](DEVELOPMENT.md) for development troubleshooting.
