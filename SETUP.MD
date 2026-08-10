# Setup Guide 🔧

Complete step-by-step guide to set up your Python learning environment.

## Table of Contents

- [System Requirements](#-system-requirements)
- [Python Installation](#-python-installation)
- [Repository Setup](#-repository-setup)
- [Virtual Environment](#-virtual-environment)
- [IDE Setup](#-ide-setup)
- [Verify Installation](#-verify-installation)
- [Troubleshooting](#-troubleshooting)

---

## 📋 System Requirements

### Minimum Requirements

- **OS:** Windows 10+, macOS 10.14+, or Linux
- **RAM:** 4 GB
- **Disk Space:** 500 MB
- **Internet:** For downloading packages

### Recommended

- **Python:** 3.10 or higher
- **VS Code** with Python extension
- **Jupyter** for interactive notebooks

---

## 🐍 Python Installation

### Windows

1. **Download Python**
   - Visit [python.org](https://www.python.org/downloads/)
   - Click "Download Python 3.x.x"
   - Choose the latest stable version

2. **Run Installer**
   - Open the downloaded `.exe` file
   - ✅ Check "Add Python to PATH" (important!)
   - Click "Install Now"

3. **Verify Installation**
   ```bash
   python --version
   pip --version
   ```

### macOS

**Option 1: Using Homebrew (Recommended)**

```bash
# Install Homebrew if not already installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python
brew install python3

# Verify
python3 --version
```

**Option 2: Direct Download**

- Visit [python.org](https://www.python.org/downloads/)
- Download macOS installer
- Run and follow installation

### Linux (Ubuntu/Debian)

```bash
# Update package manager
sudo apt update

# Install Python
sudo apt install python3 python3-pip python3-venv

# Verify
python3 --version
pip3 --version
```

### Linux (Fedora/RHEL)

```bash
# Install Python
sudo dnf install python3 python3-pip

# Verify
python3 --version
pip3 --version
```

---

## 📁 Repository Setup

### Step 1: Clone Repository

```bash
# Clone the repo
git clone https://github.com/vishal-kushwaha-9912/python-basics.git

# Navigate into directory
cd python-basics
```

**Don't have Git?** [Install Git](https://git-scm.com/)

### Step 2: Create Virtual Environment

A virtual environment isolates project dependencies.

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment

# Windows:
venv\Scripts\activate

# macOS/Linux:
source venv/bin/activate
```

**You should see `(venv)` prefix in terminal after activation**

### Step 3: Install Dependencies (Optional)

```bash
# Upgrade pip
pip install --upgrade pip

# Install Jupyter for notebooks
pip install jupyter

# Install common data science packages (for future use)
pip install numpy pandas matplotlib
```

---

## 🔐 Virtual Environment

### Why Virtual Environment?

- ✅ Isolates project dependencies
- ✅ Prevents version conflicts
- ✅ Makes projects portable
- ✅ Industry standard practice

### Common Commands

```bash
# Activate virtual environment
source venv/bin/activate          # macOS/Linux
venv\Scripts\activate             # Windows

# Deactivate virtual environment
deactivate

# Delete virtual environment (when done)
rm -rf venv                       # macOS/Linux
rmdir /s venv                     # Windows
```

### Check Virtual Environment Status

```bash
# Check if activated (should show venv path)
which python           # macOS/Linux
where python           # Windows
```

---

## 💻 IDE Setup

### Using VS Code (Recommended)

#### Step 1: Install VS Code

- Download from [code.visualstudio.com](https://code.visualstudio.com/)
- Install and open

#### Step 2: Install Python Extension

1. Open VS Code
2. Go to Extensions (Ctrl+Shift+X / Cmd+Shift+X)
3. Search "Python"
4. Install official Python extension by Microsoft

#### Step 3: Select Python Interpreter

1. Press Ctrl+Shift+P (Cmd+Shift+P on Mac)
2. Type "Python: Select Interpreter"
3. Choose the one in `./venv` folder

#### Step 4: Configure Settings

Create or update `.vscode/settings.json`:

```json
{
  "python.defaultInterpreterPath": "${workspaceFolder}/venv/bin/python",
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "python.formatting.provider": "black",
  "editor.formatOnSave": true,
  "editor.rulers": [88],
  "[python]": {
    "editor.defaultFormatter": "ms-python.python",
    "editor.formatOnSave": true
  }
}
```

### Using PyCharm

1. **Install PyCharm** — Download from [jetbrains.com](https://www.jetbrains.com/pycharm/)
2. **Create Project** — Point to `python-basics` folder
3. **Configure Interpreter** — Set to `./venv/bin/python`

### Using IDLE (Built-in)

```bash
# Launch IDLE
python -m idlelib.idle

# Open python file and run
```

---

## ✅ Verify Installation

### Check Python

```bash
python --version        # Should be 3.8+
python -c "import sys; print(sys.executable)"
```

### Check Pip

```bash
pip --version
pip list                # Shows installed packages
```

### Test Virtual Environment

```bash
# With virtual environment activated
which python           # Should show path inside venv
pip list               # Should show pip, setuptools, wheel
```

### Test File Execution

```bash
# Navigate to repo
cd python-basics

# Run a test file
python datatypes.py

# Output should show data type examples
```

### Test Jupyter (if installed)

```bash
# Start Jupyter
jupyter notebook

# Should open in browser at localhost:8888
# Navigate to forloop/forloop.ipynb and open it
```

---

## 🔧 Troubleshooting

### "Python: command not found"

**Problem:** Python not installed or not in PATH

**Solutions:**

```bash
# Try python3 instead
python3 --version

# Add Python to PATH (Windows)
# Reinstall Python and check "Add Python to PATH"

# Or manually add to PATH (macOS/Linux)
export PATH=$PATH:/usr/local/bin/python3
```

### "ModuleNotFoundError"

**Problem:** Missing package/module

**Solution:**

```bash
# Ensure virtual environment is activated
source venv/bin/activate

# Install missing package
pip install <package_name>

# Example:
pip install jupyter
```

### "Permission Denied"

**Problem:** Cannot write to directories

**Solutions:**

```bash
# Use --user flag
pip install --user jupyter

# Or use virtual environment (recommended)
source venv/bin/activate
pip install jupyter
```

### Virtual Environment Not Activating

**Problem:** Can't activate venv

**Solutions:**

```bash
# Check if venv exists
ls venv                   # macOS/Linux
dir venv                  # Windows

# Recreate if missing
python -m venv venv

# Use full path
source /full/path/to/venv/bin/activate

# Use Python directly (alternative)
/full/path/to/venv/bin/python script.py
```

### Jupyter Won't Start

**Problem:** Jupyter notebook command not working

**Solutions:**

```bash
# Reinstall Jupyter
pip uninstall jupyter
pip install jupyter --upgrade

# Use python module instead
python -m jupyter notebook

# Check installation
jupyter --version
```

### Port Already in Use

**Problem:** "Address already in use" when starting Jupyter

**Solution:**

```bash
# Use different port
jupyter notebook --port 8889

# Or kill process using port
# macOS/Linux:
lsof -ti:8888 | xargs kill -9
# Windows:
netstat -ano | findstr :8888
taskkill /PID <PID> /F
```

---

## 📝 Quick Reference

### Essential Commands

```bash
# Clone repo
git clone https://github.com/vishal-kushwaha-9912/python-basics.git
cd python-basics

# Setup
python -m venv venv
source venv/bin/activate              # macOS/Linux
venv\Scripts\activate                 # Windows

# Run Python files
python filename.py

# Install packages
pip install package_name

# Launch Jupyter
jupyter notebook

# Deactivate environment
deactivate
```

### File Structure After Setup

```
python-basics/
├── venv/                    # Virtual environment (created)
├── challenge/
├── forloop/
├── FUNCTIONS/
├── ... (other files/folders)
└── README.md
```

---

## 🎓 Next Steps

1. ✅ Verify your setup works (run `python datatypes.py`)
2. ✅ Open VS Code and explore the code
3. ✅ Read the main [README.md](README.md)
4. ✅ Start with [QUICK_START.md](QUICK_START.md)
5. ✅ Begin the 5-Day Challenge

---

## 💡 Tips

- **Use Virtual Environment Always** — Industry standard, prevents headaches
- **Keep it Updated** — `pip install --upgrade pip`
- **Check Python Version** — Some packages need specific versions
- **Read Error Messages** — They usually tell you the solution
- **Use VS Code** — Great Python support, free, widely used

---

**Setup Complete!** 🎉

Ready to learn Python? Head to [QUICK_START.md](QUICK_START.md)

---

_Last Updated: August 2026_
