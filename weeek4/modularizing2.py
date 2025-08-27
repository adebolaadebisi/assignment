# python packages
# what a package is (a folder with init.py)
# installing and using thyird-party packages (pip install request, import requests)
# organizing multiple modules into a package

#what is a package?
# A package in python is a way to organize related modules together into a folder.
# inside this folder, there must be a special file called _init_.py(can be empty). this file tells python that the folder should be treated as a package.
# let think of a package as a standard mechanic workshop, and each module is a different toolbox inside the workshop. the iNiT.py file is like the label on the workshop telling passerbys that this is a mechanic workshop.
# Third-party packages
# python comes with some built-in modules, but you can also install extra packages created by others.
# these packages are stored in the python package index(pypi).
# we install them using pip(python's package manager)or conda a

#how to install python packages
#1.Using pip
# this is the most common method.
# it installs packages from pypi. it is the python's central package repository.
# to work with it, you have to use it in your terminal
# pip install requests                 # install latest version
# pip install requests==2.28           # install specific version
# pip install --upgrade requests       # upgrade existing package
# pip uninstall request                # remove packages

#2. Using UV
# this is the mordern , super-fast package and project manager
# it is a RUST-based that unifies package installation, virtual environment and python version management into one fast, modern CLI.
# To use uv
# run this command on your terminal depending on your OS
# Recommended method: standalone installer
# macOS/Linux
# curl -LsSF https://astral.sh/uv/install.sh | sh
# or
# windows
#powershell -ExecutionPolicy Bypass -c "irm https://astral.sh/uv/install.ps1| iex"
# After installation, verify version.
#**2. Using `uv`**

# - Thisi is the modern, super-fast package and project manager
# - IT is a RUST-based that unifies package installation, virtual environment and pyton version management into one fast, modern CLI.

# - To use uv

# ```
# Run this command on your terminal depending on your OS

# Recommended method: standalone installer
 # macOS/Linux

#-LsSf https://astral.sh/uv/install.sh | sh

# or

# Windows

# powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"  


# - After installation, verify version.


# uv --version


# - Using uv to install packages
# - But before it works you must have a workin `virtual environment` 


# uv add requests              # Install package and update project files

# uv pip install flask         # Works like pip but much faster

# uv remove requests           # Uninstall

# uv venv                      # Create a virtual environment automatically

# uv run script.py             # Run scripts in the managed environment
# - Other package managers that you should try exploring

# | Method                            | Description                     | Best For                                 |
# | --------------------------------- | ------------------------------- | ---------------------------------------- |
# | `pip install ...`                 | Standard installation from PyPI | Most common and simple use case          |
# | `pip install -r requirements.txt` | Batch install from file         | Reproducible projects                    |
# | Virtualenv + `pip`                | Isolated environments           | Independent project setups               |
# | `conda install ...`               | Data science ecosystem          | Scientific and system-level dependencies |
# | Clone + `pip install .`           | Custom or non-PyPI packages     | Local development and experiments        |
# | `.whl install`                    | Prebuilt package install        | Faster installations                     |
# | `pip install -e .`                | Editable (development) install  | Active package development               |
# | `uv ...`                          | All-in-one modern manager       | Speed, simplicity, and full workflow     |

# - What is a Virtual Environment?
# - A virtual environment (venv) is an isolated workspace where you can install and manage Python packages without affecting the global/system Python installation.

# - Each project can have its own dependencies, even if they conflict with other projects.

# - Why should you form the habit of always creating a Venv before starting a project?

#  - It keeps project dependencies separate.
#  - It prevents version conflicts.
#  - It makes collaboration easier (everyone uses the same environment).
#  - It is required in many production setups.
