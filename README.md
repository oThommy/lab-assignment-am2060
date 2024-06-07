[![python-version](https://img.shields.io/badge/python-v3.12.3-blue)](https://www.python.org/downloads/release/python-3123/)
![license](https://img.shields.io/badge/license-MIT-green)
[![download](https://img.shields.io/badge/download-.zip-brightgreen)](https://github.com/oThommy/lab-assignment-am2060/archive/refs/heads/main.zip)
# Lab Assignment AM2060

# Python environement setup
Please ensure you have Python version 3.12.3 installed (the button above redirects to the official download page).

## Using a normal Python installation
### Using cmd
- Download the ZIP by using the button above and extract the directory.
- Open `cmd.exe` in the root of `lab-assignment-am2060-main` as administrator and run `python -m venv .venv && ".venv\Scripts\activate.bat" && pip install -r requirements.txt`.
- To activate virtual environment use `".venv\Scripts\activate.bat"`.
- To deactivate virtual environment use `deactivate`.

### Using Git Bash
- Download the repository by running `git clone https://github.com/oThommy/lab-assignment-am2060.git && cd lab-assignment-am2060` in your directory of choice.
- Open Git Bash in the root of `lab-assignment-am2060` as administrator and run `python -m venv .venv && source .venv/Scripts/activate && pip install -r requirements.txt`.
- To activate virtual environment use `source .venv/Scripts/activate`.
- To deactivate virtual environment use `deactivate`.

### Selecting Python interpreter in Visual Studio Code
- To select a the virtual environment, use the **Python: Select Interpreter** command from the **Command Palette** (<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd>) and enter `.\.venv\Scripts\python.exe`.

## Using an Anaconda installation
Replace `C:/ProgramData/Anaconda3/` with `your/path/to/Anaconda3` in the code below in case they do not match.
- Download the ZIP by using the button above and extract the directory.
- Open `cmd.exe` in the root of `lab-assignment-am2060-main` as administrator and run `"C:/ProgramData/Anaconda3/condabin/activate.bat" && conda env create -f environment.yml && conda activate lab-assignment-am2060-venv`.
- To activate virtual environment use `conda activate lab-assignment-am2060-venv`.
- To deactivate virtual environment use `conda deactivate`.

### Selecting Python interpreter in Anaconda
The interpreter is located at `C:\ProgramData\Anaconda3\envs\lab-assignment-am2060-venv\python.exe`.
- To use Spyder, either activate the virtual environment and run `conda install spyder` and run `spyder` or activate the virtual environment from the Spyder console.
- To use Jupyter Notebook, activate the virutal environment and run `jupyter notebook`. Once you have selected a file you can select the virtual environment from **Kernel** > **Change kernel** > **Python 3 (ipykernel)**.
