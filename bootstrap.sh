#!/usr/bin/env bash

ENVNAME="$(basename $(pwd))"

eval "$(micromamba shell hook --shell=zsh)"

export MAMBA_ROOT_PREFIX=$PWD/.mamba

if [ ! -e .mamba ]; then
	just python-install
fi

micromamba activate "$ENVNAME"

echo ""
echo "⭐ Welcome to the $ENVNAME project ⭐"
echo ""

just

$SHELL
