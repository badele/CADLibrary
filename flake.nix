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
        ##############################################################################
        inherit overlay overlays;
        devShell = (pkgs.buildFHSUserEnv {
          name = "CADLibrary";
          targetPkgs = with pkgs; pkgs:
            [
              # just
              just

              # Openscad
              openscad

              # Python
              python312
              micromamba

              # Lint
              pre-commit
              nodePackages.markdownlint-cli
            ];
          runScript = "./bootstrap.sh";
        }).env;
      });
  ##############################################################################
  #   devShells.default = with pkgs;
  #     mkShell {
  #       name = "Default developpement shell";
  #       packages = [
  #         cocogitto
  #         nixpkgs-fmt
  #         nodePackages.markdownlint-cli
  #         pre-commit
  #         just
  #
  #         openscad
  #
  #       ];
  #       shellHook = ''
  #         export PROJ="CADLibrary"
  #
  #         echo ""
  #         echo "⭐ Welcome to the $PROJ project ⭐"
  #         echo ""
  #       '';
  #     };
  # });
}
