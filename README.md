# 🚀 PoC: FastAPI + Pydantic + PostgreSQL
This project is a Proof of Concept (PoC) dedicated to studying the Modern Python ecosystem, focusing on building robust, validated APIs integrated with relational databases.
## 🛠️ Core Technologies

* [FastAPI](https://fastapi.tiangolo.com/): High-performance web framework.
* [Pydantic](https://docs.pydantic.dev/): Data validation and settings management.
* [PostgreSQL](https://www.postgresql.org/): Relational database.
* [Docker & Compose](https://www.docker.com/): Infrastructure orchestration for the database.
* [Nix/NixOS](https://nixos.org/): Reproducible development environment management.

------------------------------
# ⚙️ Getting Started
## 1. Environment Setup
### Option A: Using Nix (Recommended)
If you are on Nix or NixOS, the environment (Python, Docker-Compose, and dependencies) is loaded automatically:
   ```bash
   nix develop
   ```

### Option B: Standard Python (No Nix)

#### 1. Create a virtual environment:

```bash 
python -m venv .venv
```

#### 2. Activate the environment:
* Linux/Mac: 
   ```bash 
   source .venv/bin/activate
   ```

* Windows:
   ```powershell
   .\venv\Scripts\activate
   ```

#### 3. Install dependencies:
*
   ```bash
   pip install -r requirements.txt
   ```

### 2. Database Setup

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Start the PostgreSQL container:
   ```bash
   docker-compose up -d
   ```
3. Run migrations:
   ```bash
   alembic upgrade head
   ```

   
### 3. Running the API
With the environment active and the database running, start the development server:
```bash
fastapi dev main.py
```

# Access the interactive documentation at: 127.0.0
## 📂 Project Structure

* app/: Application source code.
* docker-compose.yml: Local infrastructure definition (Postgres).
* flake.nix: Nix environment configuration.
* .env: Environment variables (git-ignored).

------------------------------
## 📝 Learning Objectives

* Implement a full CRUD.
* Validate input/output schemas with Pydantic.
* Manage asynchronous database connections.
* Apply database migrations with Alembic.

------------------------------
Developed for learning purposes. 🚀
------------------------------

