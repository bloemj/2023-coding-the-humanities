# UvA Coding the Humanities 2020

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Giovanni1085/UvA_CDH_2020/master)

## Contents

* [Hello World](notebooks/0_HelloWorld.ipynb): a first notebook to check if everything is working.

## Set-up

### Editor

You really will need an **editor** to write code and edit files. If you don't have a preferred one yet, check [Sublime Text](https://www.sublimetext.com/) or [Atom](https://atom.io/).

### Working with Jupyter Notebooks

* Option 0: Use [Binder](https://mybinder.org) (link above). Keep in mind you need to download your notebooks to save them locally.

* Option 1: Download [the repository contents](https://github.com/Giovanni1085/UvA_CDH_2020) and use [Spyder](https://www.spyder-ide.org/).

* Option 2:
1. Clone (or just download) the repository locally: `git clone https://github.com/Giovanni1085/UvA_CDH_2020.git`
2. Get updates (from time to time): `git pull`
3. Create a conda environemnt: `conda create -n myenv python=3.7 anaconda` (where `myenv` is the envirnoment name)
4. Activate it: `conda activate myenv`
5. Install packages (see the `requirements.txt` file), e.g. `conda install pandas`
6. Launch a Jupyter notebook: `jupyter notebook`

### Further reading

* [More on conda enviroments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
* [Conda cheatsheet](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf)
* [Getting started with Jupyter notebooks](https://medium.com/codingthesmartway-com-blog/getting-started-with-jupyter-notebook-for-python-4e7082bd5d46)
* [On using git and GitHub for version control](https://alan-turing-institute.github.io/rsd-engineeringcourse/ch02git)

**A more detailed [guide to setup your environment](setup.md), with multiple options.**
