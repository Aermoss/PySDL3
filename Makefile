sourceDir := docs
buildDir := docs/_build

help:
	@sphinx-build -M help "$(sourceDir)" "$(buildDir)"

.PHONY: help Makefile

%: Makefile
	@sphinx-build -M $@ "$(sourceDir)" "$(buildDir)"