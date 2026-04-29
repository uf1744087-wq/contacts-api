# Project Setup Guide - Python Version Management

## Problem Solved

This project is configured to use **Python 3.12** to avoid compatibility issues with packages like PyIceberg that require C extensions. Python 3.14 and newer versions don't yet have pre-built wheels for many packages on Windows.

## For Future Projects - Permanent Solution

### Option 1: Using pyenv (Recommended for Windows)

1. **Install pyenv-win**: <https://github.com/pyenv-win/pyenv-win>

   ```powershell
   # Using Chocolatey
   choco install pyenv-win
   ```

2. **Install Python 3.12**:

   ```powershell
   pyenv install 3.12.0
   ```

3. **Auto-select Python version**:

   The `.python-version` file in this project automatically selects Python 3.12 when you navigate to the project directory (if pyenv is installed).

### Option 2: Using uv (Modern Python Package Manager)

1. **Install uv**: <https://docs.astral.sh/uv/getting-started/>

   ```powershell
   # Windows installers available at https://github.com/astral-sh/uv/releases
   # Or with pip:
   pip install uv
   ```

2. **Create venv with uv**:

   ```powershell
   uv venv --python 3.12
   .venv\Scripts\Activate.ps1
   ```

3. **Install dependencies**:

   ```powershell
   uv pip install -e .
   # Or for pyiceberg specifically:
   uv pip install pyiceberg
   ```

### Option 3: Manual Python 3.12 Installation

1. **Download Python 3.12**: <https://www.python.org/downloads/>

2. **Create venv**:

   ```powershell
   "C:\path\to\python3.12\python.exe" -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

3. **Install dependencies**:

   ```powershell
   pip install -e .
   ```

## For This Project

### Current Setup

- **Python Version**: 3.12 (specified in `.python-version` and `pyproject.toml`)
- **Environment**: Virtual environment in `.venv`

### First Time Setup

```powershell
cd d:\contacts-api

# If using pyenv (Windows):
pyenv install 3.12.0
pyenv local 3.12.0

# Or download Python 3.12 manually and create venv:
"C:\Program Files\Python312\python.exe" -m venv .venv
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -e .
pip install pyiceberg
```

### Activate Environment

```powershell
.\venv\Scripts\Activate.ps1
```

## Why Python 3.12?

- PyIceberg requires C/C++ extensions to be compiled
- Many packages on Windows lack pre-built wheels for Python 3.14+
- Python 3.12 has excellent pre-built wheel support
- Python 3.12 is stable and production-ready

## Configuration Files

- `.python-version` - Specifies Python 3.12 for pyenv/asdf
- `pyproject.toml` - `requires-python = ">=3.12,<3.14"` constraint
- `.venv/` - Local virtual environment (gitignored)

## Troubleshooting

### Build Tools Error (MSVC 14.0 not found)

If you see: "error: Microsoft Visual C++ 14.0 or greater is required"

- Download: <https://visualstudio.microsoft.com/visual-cpp-build-tools/>
- Install "Desktop development with C++"

### Python 3.12 Not Found

- Use `pyenv` to manage Python versions (recommended approach)
- Or download from <https://www.python.org/downloads/>

### uv Command Not Working

- Restart your terminal after installing uv
- Or install/upgrade: `pip install --upgrade uv`
