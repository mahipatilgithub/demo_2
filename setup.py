from setuptools import setup, find_packages
# setuptools is a package used by many other packages to handle their installation from source code (and tasks related to it).
HYPEN_E_DOT = '-e.'
# -e. is storing in HYPEN_E_DOT


def get_requirements(file_path): # receiving "requirement.txt" in "file_path"
    requirements = [] # creating empty list
    with open(file_path) as file_obj: # reading/opening file with alias "file_obj"
        requirements = file_obj.readlines() # The readlines() method returns a list containing each line in the file as a list item.
        requirements = [req.replace("\n", "") for req in requirements] # removing new line while adding items in "requirements" list using list compression

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT) # removing "-e." while installing packages/library in list,bcz we don't want to install "-e."

setup(
    name = "demo_2",
    version = "0.0.1",
    author = "Mahi",
    author_email="mahipatilgithub@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
    )