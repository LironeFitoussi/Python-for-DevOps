# create a virtual environment
python -m venv .venv 

# activate the virtual environment in windows
source .venv/Scripts/activate

# activate the virtual environment in UNIX based systems (macos and linu x)
source .venv/bin/activate

# create a new virtual environment
python -m venv .venv2

# activate the new virtual environment
source .venv2/bin/activate

# deactivate the virtual environment
deactivate

# list all virtual environments
ls -l .venv .venv2

# remove a virtual environment
rm -rf .venv .venv2

# get installed packages in a virtual environment
pip freeze > requirements.txt

# install packages from a requirements.txt file
pip install -r requirements.txt

# list installed packages in a virtual environment
pip list

# remove a package from a virtual environment
pip uninstall <package_name>