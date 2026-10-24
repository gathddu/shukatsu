{
  description = "shukatsu";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
  };

  outputs = { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs {
        inherit system;
      };

      pythonEnv = pkgs.python3.withPackages (python-pkgs: [
        python-pkgs.google-api-python-client
        python-pkgs.google-auth-oauthlib
        python-pkgs.gspread
        python-pkgs.questionary
      ]);

      shukatsu = pkgs.writeShellApplication {
        name = "shukatsu";
        runtimeInputs = [ pythonEnv ];
        text = ''
          exec python ${./main.py} "$@"
        '';
      };
    in
    {
      packages.${system}.default = shukatsu;

      devShells.${system}.default = pkgs.mkShell {
        packages = [ pythonEnv ];
      };
    };
}
