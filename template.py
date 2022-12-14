from importlib.resources import path
import  os
from pathlib import Path
import  logging
logging.basicConfig(level="INFO", format="[%(asctime)s]: %(message)s:")

package_name = "deepClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/utils/__init__.py",
    f"src/{package_name}/config/__init__.py",
    f"src/{package_name}/pipeline/__init__.py",
    f"src/{package_name}/entity/__init__.py",
    f"src/{package_name}/constants/__init__.py",
    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "configs/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "researsh/tirals.ipynb",
]
# creating directories
for file in list_of_files:
    filepath  = Path(file)

    file_dir, file_name = os.path.split(filepath) 
    if file_dir != "":
        os.makedirs(file_dir,exist_ok=True)#creating directories
        logging.info(f"creating directory: {file_dir} for file: {file_name}")

    # creating files
    if  (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # creating empty file
            logging.info(f"Creating empty file:{filepath}")

    else:
        logging.info(f"{file_name} already exists")

