# MkDocs
Project documentation with Markdown.

!!! warning "MkDocs 2.0 [Introduces Breaking Changes][b]"
    Continue with 1.x until [zeniscal is a suitable replacement][c].


## Setup
An [auto configured environment](#auto-configured-environment) direnv is highly
recommended.

!!! warning "Pin click==8.2.1 until resolved"
    Click 8.2.2 breaks all URL's resulting in 404 errors.

    Always pin to **8.2.1** [until bug is resolved][d].

### Manual
=== "uv"

    ``` bash
    # Recommended.
    uv init
    uv add mkdocs mkdocs-material mkdocs-glightbox
    uv add mkdocs-git-revision-date-localized-plugin
    uv pip install click==8.2.1
    uv run mkdocs serve --livereload
    ```

=== "venv"

    ``` bash
    # Not recommended.
    python3 -m venv /var/venv/docs
    source /var/venv/docs/bin/activate
    pip install --upgrade pip
    pip install mkdocs mkdocs-material mkdocs-glightbox
    pip install mkdocs-git-revision-date-localized-plugin
    pip install click==8.2.1
    mkdocs serve --livereload
    ```

=== "zensical testing"

    ``` bash
    uv init
    uv add zensical
    uv run zensical serve
    ```

### Auto Configured environment
Preferred as entering docs directory will automatically setup virtual
environment and activate.

[Install direnv](../app/direnv.md#setup) and [create initial venv](#manual).

!!! abstract ".envrc"
    0644 {USER}:{USER}

    ``` bash
    # Create environment file to automatically setup virtual environment.
    # direnv executes .envrc in bash and exports back to current shell.

    # Create venv if needed and activate.
    uv sync --all-extras && source .venv/bin/activate
    ```

!!! abstract ".gitignore"
    0644 {USER}:{USER}

    ``` bash
    # Ignore user-generate UV environments in repository commits.
    .venv/
    .python-version
    main.py
    ```

``` bash
# Enable auto parsing of environment on entering directory.
direnv allow
```

Add environment files to repository

* uv.lock
* .envrc
* pyproject.toml

### Configure Release Publishing
One-time configuration per repository.

!!! example "github ➔ Settings ➔ Pages"
    * Source: Deploy from branch
    * Branch: gh-pages ➔ / (root)


## Local Live Testing
Changes will automatically be detected and re-rendered for local browser
testing.

``` bash
uv run mkdocs serve --livereload
```

## Publish
Generate and push new MkDoc site base on current repository.

!!! tip "All warnings and errors must be resolved before committing."

``` bash
# Create a tagged commit and push.
git commit
git push && git push --tags

# Deploy docs to live site.
uv run mkdocs gh-deploy
```


## Material Theme
Use MkDocs with material theme using minimal extensions to maintain as close to
vanilla markdown as possible. Other MKDoc vanilla formats may be used if
material-specific options are removed.

!!! abstract "_material/init.js"
    0644 {USER}:{USER}

    ``` js
    // Syntax highlighting with highlight.js.
    document$.subscribe(() => {
      hljs.highlightAll()
    })
    // Table sorting.
    document$.subscribe(function() {
      var tables = document.querySelectorAll("article table:not([class])")
      tables.forEach(function(table) {
        new Tablesort(table)
      })
    })
    ```

TODO - add theme refs.
!!! abstract "mkdocs.yml"
    0644 {USER}:{USER}

    ``` yaml
    # Page Configuration.
    site_name: '{NAME}'
    repo_url: 'https://github.com/{USER}/{REPO}'
    site_url: 'https://github.com/{USER}/{REPO}'
    edit_uri: 'edit/main/docs'
    site_author: '{USER}'
    copyright: '©2026'
    remote_branch: 'gh-pages'
    remote_name: 'origin'

    # Theme Configuration.
    # * https://squidfunk.github.io/mkdocs-material
    # * https://squidfunk.github.io/mkdocs-material/reference
    theme:
      name: 'material'
      palette:  # Material theme (auto, light, dark).
        - media: '(prefers-color-scheme)'
          toggle:
            icon: 'material/link'
            name: 'Switch to light mode'
        - media: '(prefers-color-scheme: light)'
          scheme: 'default'
          primary: 'indigo'
          accent: 'indigo'
          toggle:
            icon: 'material/toggle-switch'
            name: 'Switch to dark mode'
        - media: '(prefers-color-scheme: dark)'
          scheme: 'slate'
          primary: 'black'
          accent: 'indigo'
          toggle:
            icon: 'material/toggle-switch-off'
            name: 'Switch to system preference'
      icon:
        annotation: 'material/chevron-right-circle'
      features:
        - 'navigation.instant'  # Requires site_url.
        - 'navigation.instant.prefetch'
        - 'navigation.instant.progress'
        - 'navigation.tracking'  # URL shows anchor tags.
        - 'navigation.path'
        - 'navigation.indexes'
        - 'navigation.top'
        - 'search.suggest'
        - 'search.highlight'
        - 'toc.follow'
        - 'header.autohide'
        - 'content.action.edit'  # Requires edit_uri.
        - 'content.footnote.tooltips'
      navigation_depth: 5
      locale: 'en'
      language: 'en'

    markdown_extensions:
      - 'attr_list'  # HTML Attribute lists.
      - 'def_list'  # HTML Definition lists.
      - 'footnotes':  # Footnotes.
      - 'md_in_html'  # Markdown in HTML.
      - 'tables'  # Sortable tables (theme/init.js).
      - 'pymdownx.betterem'  # Github flavored emphasis handling.
      - 'pymdownx.magiclink'  # Autolink URI's.
      - 'pymdownx.superfences'  # HTML block nesting.

      # Admonitions.
      - 'admonition'
      - 'pymdownx.details'

      # Emoji
      - pymdownx.emoji:
          emoji_index: !!python/name:material.extensions.emoji.twemoji
          emoji_generator: !!python/name:material.extensions.emoji.to_svg

      # Linkable tabbed blocks.
      - pymdownx.tabbed:
          alternate_style: true
          slugify: !!python/object/apply:pymdownx.slugs.slugify
            kwds:
              case: 'lower'

      # Github flavored checklists.
      - pymdownx.tasklist:
          custom_checkbox: true

      # Syntax Highlighting.
      - pymdownx.highlight:
          use_pygments: false  # Use highlight.js for Material.
      - 'pymdownx.inlinehilite'

    plugins:
      - 'glightbox' # Inline images.

      # Created, last update footers.
      - git-revision-date-localized:
          enable_creation_date: true

      - 'search'  # Search

        # Site navigation side panel.
        nav:
          - 'README.md'
          # Note: ':' is required for expanding sections.
          - 'Applications':
              - 'app/bash.md'

    # Material Code Highlighting.
    #
    # Material use Python Pygments - highlight.js provides better highlights for
    # non-python code.
    #
    # Disable Python Pygments and use highlight.js. Code highlight theme is set
    # with extra_css, not integrated hljs.* options.
    #
    # Reference:
    # * https://squidfunk.github.io/mkdocs-material/setup/extensions/python-markdown-extensions/#highlight-mkdocsyml
    # * https://github.com/squidfunk/mkdocs-material/issues/1004
    # * https://github.com/highlightjs/highlight.js/tree/main/src/styles
    # * https://highlightjs.org/demo

    extra_javascript:
      - 'https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.11.1/highlight.min.js'
      - 'https://unpkg.com/tablesort@5.3.0/dist/tablesort.min.js'
      - '_material/init.js'

    extra_css:
      - 'https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.11.1/styles/vs2015.min.css'

    # Enable social icons and links.
    extra:
      social:
        - icon: 'fontawesome/brands/github'
          link: 'https://github.com/r-pufky'
        - icon: 'simple/gnuprivacyguard'
          link: 'https://keys.openpgp.org/vks/v1/by-fingerprint/466EEC2B67516C7117C85CE3A0BC35D16698BAB9'
    ```

Site will now render with Material theme using
[local live testing](#local-live-testing) and [publishing](#publish).

[a]: https://www.mkdocs.org/Project
[b]: https://squidfunk.github.io/mkdocs-material/blog/2026/02/18/mkdocs-2.0
[c]: https://zensical.org/docs/get-started/
[d]: https://github.com/mkdocs/mkdocs/issues/4014
