# [Zensical][a]
Project documentation with Zensical.

## Setup
An [auto configured environment](#auto-configured-environment) direnv is highly
recommended.

``` bash
# Recommended.
uv init
uv add --dev zensical
uv run zensical serve
```

### Auto Configured environment
Preferred as entering docs directory will automatically setup virtual
environment and activate.

[Install direnv](../app/cli/direnv.md#setup) and [create initial venv](#setup).

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

!!! example "github ➔ Settings ➔ Environments ➔ github-pages"
    * Deployment branches and tags:
        * branch: **master**

    Create new environment if needed. This seems to be hardcoded in Zensical
    currently.

!!! abstract ".github/workflows/docs.yml"
    0644 {USER}:{USER}

    ``` yaml
    ---
    name: 'Documentation'
    on:
      push:
        tags:
          - '*'  # Trigger workflow on tag creation.
    permissions:
      contents: 'read'
      pages: 'write'
      id-token: 'write'
    jobs:
      deploy:
        # Only run when tagged and on master branch.
        if: github.ref == 'refs/heads/master'
        environment:
          name: 'github-pages'  # Environment to use.
          url: ${{ steps.deployment.outputs.page_url }}
        runs-on: 'ubuntu-latest'
        steps:
          - uses: 'actions/configure-pages@v5'
          - uses: 'actions/checkout@v5'
          - uses: 'actions/setup-python@v5'
            with:
              python-version: '3.x'
          - run: 'pip install zensical'
          - run: 'zensical build --clean'
          - uses: 'actions/upload-pages-artifact@v4'
            with:
              path: 'site'
          - uses: 'actions/deploy-pages@v4'
            id: 'deployment'
    ```

## Local Live Testing
Changes will automatically be detected and re-rendered for local browser
testing.

``` bash
uv run zensical serve
```

## Publish
Generate and push new Zensical site base on current repository.

!!! tip "All warnings and errors must be resolved before committing."

``` bash
# Create a tagged commit and push.
git commit
git push && git push --tags

# Rebase branch with current master; pushing will automatically run workflow.
git checkout master
git pull origin master
git checkout gh-pages
git rebase master
git push origin gh-pages
```

## Material Theme
Use Zensical with material theme using minimal extensions to maintain as close
to vanilla markdown as possible. Other Zensical vanilla formats may be used if
material-specific options are removed.

Config below provides a drop-in replacement for a standard MKDocs Material
configuration.

!!! abstract "_extra/init.js"
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

!!! abstract "_extra/widescreen.css"
    0644 {USER}:{USER}

    ``` css
    /* Enable width adjustments to window width. */
    .md-grid {
      max-width: initial;
    }
    ```

!!! abstract "zensical.toml"
    0644 {USER}:{USER}

    ``` yaml
    [project]
    # Manually generate nav for explicit heading format/casing.
    nav = ["README.md"]

    site_name = "Docs: A Collection of Notes"
    site_url = "https://github.com/{USER}/{REPO}"
    repo_url = "https://github.com/{USER}/{REPO}"
    site_author = "{USER}"
    copyright = "©2026"
    docs_dir = "docs"
    site_dir = "site"
    use_directory_urls = true
    dev_addr = "localhost:8000"

    # Material Code Highlighting.
    #
    # Material uses Python Pygments - highlight.js provides better highlights
    # for non-python code.
    #
    # Disable Python Pygments and use highlight.js. Code highlight theme is set
    # with extra_css, not integrated hljs.* options.
    #
    # Reference:
    # * https://squidfunk.github.io/mkdocs-material/setup/extensions/python-markdown-extensions/#highlight-mkdocsyml
    # * https://github.com/squidfunk/mkdocs-material/issues/1004
    # * https://github.com/highlightjs/highlight.js/tree/main/src/styles
    # * https://highlightjs.org/demo
    extra_css = [
      "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.11.1/styles/vs2015.min.css",
      "_extra/widescreen.css",
    ]
    extra_javascript = [
      "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.11.1/highlight.min.js",
      "https://unpkg.com/tablesort@5.3.0/dist/tablesort.min.js",
      "_extra/init.js",
    ]

    [project.theme]
    variant = "classic"  # "modern" is updated look for zensical.
    language = "en"
    features = [
      "header.autohide",
      "content.action.edit",
      "content.footnote.tooltips",
      "navigation.instant",
      "navigation.instant.prefetch",
      "navigation.instant.progress",
      "navigation.tracking",
      "navigation.path",
      "navigation.indexes",
      "navigation.top",
      "toc.follow",
      "search.highlight",
    ]
    icon.annotation = "material/chevron-right-circle"
    navigation_depth = 5

    [[project.theme.palette]]
    media = "(prefers-color-scheme)"
    toggle.icon = "lucide/sun-moon"
    toggle.name = "Switch to light mode"

    [[project.theme.palette]]
    media = "(prefers-color-scheme: dark)"
    scheme = "slate"
    primary = "black"
    accent = "indigo"
    toggle.icon = "lucide/sun"
    toggle.name = "Switch to light mode"

    [[project.theme.palette]]
    media = "(prefers-color-scheme: light)"
    scheme = "default"
    primary = "indigo"
    accent = "indigo"
    toggle.icon = "lucide/moon"
    toggle.name = "Switch to dark mode"

    [[project.extra.social]]
    icon = "fontawesome/brands/github"
    link = "https://github.com/r-pufky"

    [[project.extra.social]]
    icon = "simple/gnuprivacyguard"
    link = "https://keys.openpgp.org/vks/v1/by-fingerprint/466EEC2B67516C7117C85CE3A0BC35D16698BAB9"

    [project.markdown_extensions.admonition]
    [project.markdown_extensions.attr_list]
    [project.markdown_extensions.def_list]
    [project.markdown_extensions.footnotes]
    [project.markdown_extensions.md_in_html]
    [project.markdown_extensions.pymdownx.arithmatex]
    generic = true

    [project.markdown_extensions.pymdownx.betterem]
    [project.markdown_extensions.pymdownx.caret]
    [project.markdown_extensions.pymdownx.details]
    [project.markdown_extensions.pymdownx.emoji]
    emoji_generator = "zensical.extensions.emoji.to_svg"
    emoji_index = "zensical.extensions.emoji.twemoji"

    [project.markdown_extensions.pymdownx.highlight]
    anchor_linenums = true
    line_spans = "__span"
    use_pygments = false  # Disable for highlight.js.

    [project.markdown_extensions.pymdownx.inlinehilite]
    [project.markdown_extensions.pymdownx.magiclink]
    [project.markdown_extensions.pymdownx.superfences]
    [project.markdown_extensions.pymdownx.tabbed]
    alternate_style = true
    slugify = { object = "pymdownx.slugs.slugify", kwds = { case = "lower" } }

    [project.markdown_extensions.pymdownx.tasklist]
    custom_checkbox = true

    [project.markdown_extensions.pymdownx.tilde]
    [project.markdown_extensions.pymdownx.mark]
    [project.markdown_extensions.tables]
    [project.markdown_extensions.zensical.extensions.glightbox]
    auto = true
    auto_themed = true
    auto_caption = true
    caption_position = "bottom"
    width = "auto"
    height = "auto"

    # TODO(zensical): Currently being implemented.
    #     plugins:
    #       - git-revision-date-localized:
    #           enable_creation_date: true
    #
    #     https://github.com/zensical/backlog/issues/18

    # TODO(zensical): Currently being migrated and therefore disabled.
    # Use with: zensical build --strict
    # [project.validation]
    # invalid_links = true
    # invalid_link_anchors = true
    # unresolved_references = false
    # unresolved_footnotes = false
    # unused_definitions = false
    # unused_footnotes = false
    # shadowed_definitions = false
    # shadowed_footnotes = false
    ```


Site will now render with Material theme using
[local live testing](#local-live-testing) and [publishing](#publish).

Reference[^1][^2]
[^1]: https://zensical.org/docs/setup/extensions/about/#zensical-extensions
[^2]: https://zensical.org/docs/setup/extensions/python-markdown-extensions

[a]: https://zensical.org/docs/get-started