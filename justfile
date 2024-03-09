#!/usr/bin/env just -f

set positional-arguments

envname:=`basename $(pwd)`

# This help
@help:
    just -lu --list-heading=$'{{ file_name(justfile()) }} commands:\n'

# Install requirements
requirements-install:
    #!/usr/bin/env bash
    if [ ! -d ~/.local/share/OpenSCAD/libraries/NopSCADlib ]; then
        echo "🔨 Download NopSCADlib Library"
        curl -sL -o /tmp/NopSCADlib.zip  https://github.com/nophead/NopSCADlib/archive/refs/heads/master.zip
        echo "🔨 Unzip NopSCADlib Library"
        unzip -qd ~/.local/share/OpenSCAD/libraries/ /tmp/NopSCADlib.zip
        mv ~/.local/share/OpenSCAD/libraries/NopSCADlib-master ~/.local/share/OpenSCAD/libraries/NopSCADlib
    fi

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

# Lock python environment
@env-lock:
    pip freeze > requirements.txt

# remove virtual env
env-clean:
    rm -rf .venv

# Execute tests
@inventories *args:
    rm ./libtest.png
    scripts/tests.py "$@"

# Execute tests
@projects *args:
    cd projects/screwdrivers_store && make_all.py

# Show installed packages
@packages:
    echo $PATH | tr ":" "\n" | grep -E "/nix/store" | sed -e "s/\/nix\/store\/[a-z0-9]\+\-//g" | sed -e "s/\/.*//g"
