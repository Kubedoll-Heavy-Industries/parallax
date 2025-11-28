
## Installation

### Prerequisites
- Python>=3.11,<3.15
- Ubuntu-24.04 for Blackwell GPUs

Below are installation methods for different operating systems.

|  Operating System  |  Windows App  |  From Source | Docker |
|:-------------|:----------------------------:|:----------------------------:|:----------------------------:|
|Windows       | ✅️ | Not recommended | Not recommended |
|Linux | ❌️ | ✅️ | ✅️ |
|macOS | ❌️ | ✅️ | ❌️ |

### From Source

Parallax uses [uv](https://docs.astral.sh/uv/) for fast, reliable dependency management.

**Install uv:**

```sh
# macOS
brew install uv

# Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Clone and install:**

```sh
git clone https://github.com/GradientHQ/parallax.git
cd parallax

# macOS (MLX dependencies install automatically)
uv sync

# Linux with SGLang backend
uv sync --extra sglang

# Linux with vLLM backend
uv sync --extra vllm
```

> [!NOTE]
> If you are using DGX Spark, please refer to the Docker installation section.

**Install the CLI globally (optional):**

```sh
uv tool install .
# To use: uvx parallax
```

#### Legacy pip installation

If you prefer pip, the following still works:

```sh
# macOS
pip install -e .

# Linux with SGLang
pip install -e ".[sglang]"

# Linux with vLLM
pip install -e ".[vllm]"
```

### Windows Application
[Click here](https://github.com/GradientHQ/parallax_win_cli/releases/latest/download/Parallax_Win_Setup.exe) to get latest Windows installer.

After installing .exe, right click Windows start button and click ```Windows Terminal(Admin)``` to start a Powershell console as administrator.

❗ Make sure you open your terminal with administrator privileges.
<details>
<summary>Ways to run Windows Terminal as administrator</summary>

- Start menu: Right‑click Start and choose "Windows Terminal (Admin)", or search "Windows Terminal", right‑click the result, and select "Run as administrator".
- Run dialog: Press Win+R → type `wt` → press Ctrl+Shift+Enter.
- Task Manager: Press Ctrl+Shift+Esc → File → Run new task → enter `wt` → check "Create this task with administrator privileges".
- File Explorer: Open the target folder → hold Ctrl+Shift → right‑click in the folder → select "Open in Terminal".
</details>
<br>

Start Windows dependencies installation by simply typing this command in console:
```sh
parallax install
```

Installation process may take around 30 minutes.

To see a description of all Parallax Windows configurations you can do:
```sh
parallax --help
```

### Docker
For Linux+GPU devices, Parallax provides a docker environment for quick setup. Choose the docker image according to the device's GPU architechture.

|  GPU Architecture  |  GPU Series  | Image Pull Command |
|:-------------|:----------------------------|:----------------------------|
|Blackwell/Ampere/Hopper| RTX50 series/RTX40 series/B100/B200/A100/H100... |```docker pull gradientservice/parallax:latest```|
|DGX Spark | GB10 |```docker pull gradientservice/parallax:latest-spark```|

Run a docker container as below. Please note that generally the argument ```--gpus all``` is necessary for the docker to run on GPUs.
```sh
# For Blackwell/Ampere/Hopper
docker run -it --gpus all --network host gradientservice/parallax:latest bash
# For DGX Spark
docker run -it --gpus all --network host gradientservice/parallax:latest-spark bash
```
The container starts under parallax workspace and you should be able to run parallax directly.

### Uninstalling Parallax

For macOS or Linux:

```sh
# If installed using uv tool
uv tool uninstall parallax

# If installed using pip
pip uninstall parallax

# Remove local environment
rm -rf .venv
```

For Docker installations, remove Parallax images and containers using standard Docker commands:

```sh
docker ps -a               # List running containers
docker stop <container_id> # Stop running containers
docker rm <container_id>   # Remove stopped containers
docker images              # List Docker images
docker rmi <image_id>      # Remove Parallax images
```

For Windows, simply go to Control Panel → Programs → Uninstall a program, find "Gradient" in the list, and uninstall it.
