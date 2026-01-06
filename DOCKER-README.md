# Jekyll Docker Development Setup

Run your Jekyll site locally without installing Ruby, Bundler, or any dependencies on your machine!

## Prerequisites

Only Docker and Docker Compose are required:
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Quick Start

### 1. Build the Docker image

```bash
docker-compose build
```

This will:
- Create a Ruby 3.1 environment
- Install all gems from your Gemfile
- Set up Jekyll

### 2. Start the development server

```bash
docker-compose up
```

Your site will be available at:

- **Site**: http://localhost:4000
- **LiveReload**: Enabled automatically (changes refresh the browser)

### 3. Stop the server

Press `Ctrl+C` or in another terminal:

```bash
docker-compose down
```

## Using the Makefile (Optional)

For convenience, use the Makefile commands:

```bash
make build      # Build the Docker image
make up         # Start the server
make down       # Stop the server
make restart    # Restart the server
make logs       # View server logs
make shell      # Open a bash shell in the container
make clean      # Clean up all Docker resources
make rebuild    # Clean, rebuild, and start
make help       # Show all available commands
```

## Common Workflows

### First Time Setup

```bash
make build
make up
```

### Daily Development

```bash
make up
# Edit your files...
# Browser auto-refreshes on save
# Press Ctrl+C when done
```

### After Updating Gemfile

```bash
make rebuild
```

### Debugging

```bash
make logs       # View live logs
make shell      # Get a shell inside the container
```

## How It Works

- **Dockerfile**: Defines the Ruby/Jekyll environment
- **docker-compose.yml**: Orchestrates the container
- Your project files are mounted into the container (changes reflect immediately)
- Gems are cached in a Docker volume for faster rebuilds

## Troubleshooting

### Port 4000 already in use

```bash
# Find what's using port 4000
lsof -i :4000

# Or change the port in docker-compose.yml:
ports:
  - "4001:4000"  # Use 4001 instead
```

### Gem installation fails

```bash
make clean
make build
```

### Site not updating

- Make sure `--force_polling` is in the command (it is by default)
- Try rebuilding: `make rebuild`

### Permission issues

```bash
# If you get permission errors on _site directory:
sudo chown -R $USER:$USER _site .jekyll-cache .sass-cache
```

## Benefits of This Setup

- No Ruby/Bundler installation needed on your machine  
- Consistent environment across all machines  
- Easy to clean up (just delete the Docker image)  
- LiveReload works out of the box  
- Fast startup after initial build  
- Isolated from your system  

## What's Mounted

The current directory (`.`) is mounted to `/srv/jekyll` in the container, so:

- Edit files on your machine with your favorite editor
- Changes are immediately visible in the container
- Jekyll rebuilds automatically
- Browser refreshes automatically (LiveReload)

## Cleaning Up

To completely remove everything:

```bash
make clean                    # Clean project files
docker-compose down -v        # Remove containers and volumes
docker rmi jotspot-jekyll     # Remove the image
```

## Advanced Usage

### Run a one-off command

```bash
docker-compose run --rm jekyll bundle update
```

### Build for production

```bash
docker-compose run --rm jekyll bundle exec jekyll build --config _config.yml
```

### Check gems

```bash
docker-compose run --rm jekyll bundle list
```

## Files in This Setup

- `Dockerfile` - Defines the Jekyll environment
- `docker-compose.yml` - Orchestrates the container and mounts
- `.dockerignore` - Excludes files from Docker context
- `Makefile` - Convenient command shortcuts (optional)
- This README

Enjoy hassle-free Jekyll development! 🚀
