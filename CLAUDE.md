# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Jekyll-based static site blog focused on SRE/DevOps topics. The site uses the Minima theme and is hosted via GitHub Pages at `eckslopez/xavierlopez.me`.

## Development Commands

### Local Development

```bash
bundle exec jekyll serve
```

This starts a local development server with auto-regeneration on file changes. The server will be available at `http://localhost:4000`.

### Install Dependencies

```bash
bundle install
```

Run this after cloning or when Gemfile changes.

### Build Site

```bash
bundle exec jekyll build
```

Generates the static site in the `_site` directory.

## Content Structure

### Blog Posts

- All blog posts are located in `_posts/`
- Posts must follow the naming convention: `YYYY-MM-DD-title.md`
- Each post requires YAML front matter with at minimum:
  - `layout: post`
  - `title: "Post Title"`
  - `date: YYYY-MM-DD HH:MM:SS +0000`
  - `categories: category-name`

### Pages

- Static pages (like `about.md`) live in the root directory
- Pages use `layout: page` in front matter
- The `permalink` front matter field controls the URL path

### Site Configuration

- All site-wide settings are in `_config.yml`
- Changes to `_config.yml` require restarting the Jekyll server
- Key settings: `title`, `email`, `description`, `baseurl`, `url`

## Architecture Notes

- This is a standard Jekyll site using the Minima theme with minimal customization
- The theme provides default layouts (`home`, `page`, `post`) without custom overrides
- No custom `_layouts/`, `_includes/`, or `_sass/` directories exist - all styling comes from the Minima gem
- Jekyll Feed plugin is enabled for RSS generation
- Posts are organized by date-prefixed filenames, with categories specified in front matter
