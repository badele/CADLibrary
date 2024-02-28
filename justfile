#!/usr/bin/env just -f

set positional-arguments

envname:=`basename $(pwd)`

# This help
@help:
    just -lu --list-heading=$'{{ file_name(justfile()) }} commands:\n'

# Setup pre-commit
@precommit-install:
    #!/usr/bin/env bash
    test ! -f .git/hooks/pre-commit && pre-commit install || true

# Update pre-commit
@precommit-update:
    pre-commit autoupdate

# Lint the project
@lint:
    pre-commit run --all-files

# Install a python environment
@python-install:
    rm -rf .mamba
    micromamba create -y -n "{{envname}}" -c conda-forge -f .requirements.txt

# Lock python environment
@python-lock:
    micromamba env export --explicit > .requirements.txt

# Execute tests
@test *args:
    scripts/tests.py "$@"

# Show installed packages
@packages:
    echo $PATH | tr ":" "\n" | grep -E "/nix/store" | sed -e "s/\/nix\/store\/[a-z0-9]\+\-//g" | sed -e "s/\/.*//g"
