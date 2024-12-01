# Project Name

This is a Python project with a development environment configured inside a Docker container. The project leverages `asyncio` for asynchronous programming and `invoke` for task management. It also includes a custom Docker environment with Zsh and Powerlevel10k theme for an enhanced development experience.

---

## Table of Contents

- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Development Environment](#development-environment)
- [Tasks](#tasks)
- [Docker](#docker)
- [VS Code Development Container](#vs-code-development-container)
- [Requirements](#requirements)
- [License](#license)

---

## Project Structure

```
├── .devcontainer
│   ├── Docker
│   ├── Dockerfile
│   ├── devcontainer.json
│   └── .p10k.zsh
├── src
│   └── main.py
├── tasks.py
├── requirements.txt
├── .gitignore
└── all_files_exported.txt
```

- `src/main.py`: The main Python script that contains an asynchronous `main` function.
- `tasks.py`: Defines tasks using the `invoke` task runner.
- `.devcontainer/`: Configuration files for VS Code's remote development container.
  - `Dockerfile`: Defines the Docker image used for the development environment.
  - `devcontainer.json`: Configures the development container for VS Code.
  - `.p10k.zsh`: Configuration for the Powerlevel10k Zsh theme.
- `requirements.txt`: Python dependencies required for the project.
- `.gitignore`: Specifies which files and directories Git should ignore.
- `all_files_exported.txt`: Placeholder for a file listing all exported files.

---

## Installation

To get started with this project, use the development container in VS Code.

### Using the Development Container

1. Clone the repository to your local machine.
2. Install [Visual Studio Code](https://code.visualstudio.com/) if you haven’t already.
3. Install the [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension in VS Code.
4. Open the project folder in VS Code.
5. VS Code will prompt you to reopen the project in the container. Click **Reopen in Container**.
6. Once the container is built, the development environment will be ready to use.

---

## Usage

### Running the Python Script

To run the main Python script, you can use the following command:

```bash
python src/main.py
```

This will execute the `main` function, which currently prints "Hello world!".

### Running with Invoke Tasks

To run the script via `invoke`, use the following command:

```bash
invoke run
```

This will call the `run` task defined in `tasks.py`, which executes the `main.py` script.

---

## Development Environment

The project includes a `.devcontainer` directory, which is configured to run inside a Docker container for a consistent development environment. This setup includes:

- **Zsh** as the default shell.
- **Powerlevel10k** as the Zsh theme for enhanced shell prompts.
- VS Code extensions for Python, Docker, Git, and more.

If you are using VS Code, this setup ensures that your environment is consistent across different developers and machines.

---

## Docker

The `Dockerfile` inside the `.devcontainer` directory builds a container with Python, Zsh, Powerlevel10k, and other necessary utilities:

1. The image is based on the latest Python Docker image.
2. It installs necessary dependencies, sets up Zsh as the default shell, and installs Oh My Zsh with Powerlevel10k.
3. It installs the `invoke` package to manage tasks.

To build the Docker container manually, you can use the following command:

```bash
docker build -t my-python-env -f .devcontainer/Dockerfile .
```

---

## VS Code Development Container

The `devcontainer.json` file configures the development environment for VS Code. When you open the project in VS Code and reopen it in a container, VS Code will:

- Use the Dockerfile to build the container.
- Set up a workspace inside the container.
- Install Python dependencies specified in `requirements.txt` using the `postCreateCommand`.

The setup also includes customizations for VS Code extensions to improve the development experience.

---

## Requirements

- Docker (for development container)
- Python 3.7 or higher
- `pip` (Python package installer)
- `invoke` (for running tasks)
- Zsh and Powerlevel10k for shell customization (included in the container)

---

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

