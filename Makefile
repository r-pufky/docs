# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
CONFDIR       = sphinx
BUILDDIR      = /tmp/docs
TARGETDIR     = docs

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" -c "$(CONFDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
#%: Makefile copy
#	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

docs: html copy

clean:
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" -c "$(CONFDIR)" $(SPHINXOPTS) $(O)
	@rm -rfv "$(TARGETDIR)"/*

html:
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" -c "$(CONFDIR)" $(SPHINXOPTS) $(O)

copy:
	@mkdir -p $(TARGETDIR)
	@touch $(TARGETDIR)/.nojekyll
	@cp -av $(BUILDDIR)/html/* "$(TARGETDIR)"
	@rm -v "$(TARGETDIR)/objects.inv"
	@rm -v "$(TARGETDIR)/genindex.html"
	@rm -rfv "$(TARGETDIR)/_sources"

