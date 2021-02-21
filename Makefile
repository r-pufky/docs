# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
CONFDIR       = sphinx
VENVDIR       = $(CONFDIR)/.sphinx
VENV          = $(VENVDIR)/bin/activate
BUILDDIR      = /tmp/docs
TARGETDIR     = docs

# Put it first so that "make" without argument is like "make help".
help:
	@echo "USAGE:"
	@echo "  make docs"
	@echo "        Build site documentation in $(BUILDDIR), trim extraneous"
	@echo "        output and copy to $(TARGETDIR)."
	@echo
	@echo "  make html"
	@echo "        Build site documentation in $(BUILDDIR)."
	@echo
	@echo "  make clean"
	@echo "        Removes all build artifacts on filesystem."
	@echo
	@echo "  make head"
	@echo "        Reverts ALL changes to head in generated documentation: $(TARGETDIR)."
	@echo
	@echo "  make linkcheck"
	@echo "        Verifies documentation links resolve properly."
	@echo
	@echo "REQUIREMENTS:"
	@echo "  python3-pip, python3-venv"

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
#%: Makefile copy
#	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

docs: html copy

clean:
	@rm -rfv "$(TARGETDIR)"/*
	@rm -rfv "$(VENVDIR)"
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" -c "$(CONFDIR)" $(SPHINXOPTS) $(O)

head:
	@git checkout -- $(TARGETDIR)
	@git clean -fd $(TARGETDIR)

sphinx-venv-setup:
	@echo 'Setting up sphinx python virtual environment ...'
	@test -d $(VENVDIR) || python3 -m venv $(VENVDIR)
	@. $(VENV); python3 -m pip install --quiet --requirement $(CONFDIR)/requirements.txt
	@echo 'Done.'

html: sphinx-venv-setup
	@. $(VENV); $(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" -c "$(CONFDIR)" $(SPHINXOPTS) $(O)

linkcheck: sphinx-venv-setup
	@. $(VENV); $(SPHINXBUILD) -M linkcheck "$(SOURCEDIR)" "$(BUILDDIR)" -c "$(CONFDIR)" $(SPHINXOPTS) $(O)

copy:
	@mkdir -p $(TARGETDIR)
	@touch $(TARGETDIR)/.nojekyll
	@cp -av $(BUILDDIR)/html/* "$(TARGETDIR)"
	@rm -v "$(TARGETDIR)/objects.inv"
	@rm -v "$(TARGETDIR)/genindex.html"
	@rm -rfv "$(TARGETDIR)/_sources"
