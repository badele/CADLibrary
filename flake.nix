{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };
  outputs = { nixpkgs, flake-utils, ... }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs {
          inherit system overlays;
          config = { allowUnfree = true; };
        };

        overlay = (final: prev: { });
        overlays = [ overlay ];
      in
      rec
      {
        devShells.default = with pkgs;
          mkShell {
            name = "Default developpement shell";
            packages = [
              cocogitto
              nixpkgs-fmt
              nodePackages.markdownlint-cli
              pre-commit
              just

              git
              unzip

              openscad

              # python environment
              python3
              stdenv.cc.cc
              zlib # for numpy

            ];
            shellHook = ''
                export PROJ="CADLibrary"
                export LD_LIBRARY_PATH=${pkgs.stdenv.cc.cc.lib}/lib
                export LD_LIBRARY_PATH=${pkgs.zlib}/lib:$LD_LIBRARY_PATH
                export PATH=~/.local/share/OpenSCAD/libraries/NopSCADlib/scripts:$PATH

                # Clone NopSCADlib Library
                just requirements-install

                # Install virtualenv
                if [ ! -e .venv ]; then
                    echo "🔨 Init python environment"
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip install -r requirements.txt
                    deactivate
                fi

              # Enable the virtual environment
              . .venv/bin/activate

                echo ""
                echo "⭐ Welcome to the $PROJ project ⭐"
                echo ""

                just
            '';
          };
      });
}
