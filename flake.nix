{
  description = "Ambiente de desenvolvimento Backend FastAPI + Postgres";

  inputs = {
    # Usando o canal instável ou específico da 25.11 para garantir as versões mais recentes das bibliotecas
    nixpkgs.url = "github:nixos/nixpkgs/nixos-25.11";
  };

  outputs = { self, nixpkgs }:
    let
      system = "x86_64-linux"; # Isso define o sistema para o qual o ambiente será construído.
      pkgs = import nixpkgs { inherit system; };
    in
    {
      devShells.${system}.default = pkgs.mkShell {
        buildInputs = [
          # Interpretador Python 3 com as bibliotecas necessárias para FastAPI e PostgreSQL
          (pkgs.python3.withPackages (ps: with ps; [
            pip          # Gerenciador de pacotes Python para instalar dependências adicionais (para quem não usa o Nix para tudo)
            fastapi
            fastapi-cli
            pydantic
            uvicorn      # Necessário para rodar o FastAPI
            psycopg2     # Driver para PostgreSQL
            sqlalchemy   # Comum em stacks FastAPI + Postgres
          ]))
          
          # Ferramentas adicionais
          pkgs.postgresql_16  # Banco de dados PostgreSQL
          pkgs.httpie         # Ferramenta para testar APIs
        ];

        # Comandos que rodam automaticamente ao entrar na pasta
        shellHook = ''
          echo "Ambiente Backend Pronto!"
          python --version
          fastapi --version
        '';
      };
    };
}
