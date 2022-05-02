# Working environment setup

## Primary option: Jupyter Notebooks in Google Colab

Using Google Colab, you can open our class materials from Github directly and keep the whole process in the cloud. View the list of class notebooks that are available for running and editing by going to your Google Colab: https://colab.research.google.com/ and loading them using the "Open Notebook" window, which appears when you first log in. Choose the **GitHub** option (second option from the right) and enter the GitHub link of our course materials: https://github.com/bloemj/2022-coding-the-humanities 

Then you will see a list of the class notebooks. Click one to open it. When you choose to **save your changes**, Colab will ask you to save a copy to your Google Drive. This will be your own copy of the file that you will work on. You are now good to go!

If you wish to quit and continue later, you should **open your own copy** again from Google Drive when you come back. To do this, choose the **Google Drive** option in the initial opening screen, and you will see your copy that you saved earlier. If you instead open from GitHub again, you will have another fresh copy from us and you will **lose your changes**.

Of course, it is also possible to open a Jupyter Notebook file that you have on your own computer in Google Colab, and work on that. To do this, use the **Upload** option, the top right option in the initial opening screen.

Note that all of these things only work while you have an active internet connection. You will **not** be able to do anything in Google Colab without an internet connection. If you expect to be working offline without a connection, consider running Python on your own machine with Anaconda, as outlined below.

## Offline option: Anaconda and Jupyter Notebooks

Download data and code for each class. Go to [the repository](https://github.com/uvacreate/2021-coding-the-humanities) and click on download > zip (top right). Unzip locally somewhere you know (e.g., desktop). Keep in mind you will need to download again for each class, as new contents are added.

[Jupyter notebooks](https://jupyter.org/) allow you to code and type in your browser. This is included in the Anaconda distribution. 

#### Anaconda

1. Install conda using the [Anaconda distribution](https://www.anaconda.com/distribution/), remember to pick Python 3.8 and the OS you need. Get the graphical installer. You do not have to install the optional programs, such as the PyCharm editor. 
2. After installation, you will have an app called **Anaconda Navigator** installed. You can create and manage enviromnents and use jupyter notebooks from it, without using the terminal, mostly.
   1. If you now launch the 'Jupyter Notebook' it will open a browser window. Navigate to the place where you downloaded and extracted (!) the zip with the course notebooks from this repository. Click on a Notebook to open it.
3. If you use the terminal, remember to relaunch all your terminal windows after the installation of conda. Then refer to [this guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html). Most likely the Anaconda installer already created an environment for you. But, to have them at hand, the most basic commands are:
    - `conda create -n myenv python=3.8 anaconda` which will create an environment named `myenv` and install the libraries in the anaconda distribution into it (handy to have most of the popular stuff at the ready).
    - `conda activate myenv`.
    - `conda deactivate`.
    - `conda remove --name myenv --all` to remove an environment and all its packages.


## Offline and through an editor

### Spyder

[Spyder](https://www.spyder-ide.org/) is a nice programming GUI (graphical user interface) similar to R Studio, if you are familiar with it. You will need to:


1. Launch Anaconda Navigator. (**do this step only once**) On the left side pane, you will see Home and Enviroments. Click on Enviroments, and using base (root, the default one), click on Channels > Add... > `conda-forge`. This will add a new channel for some packages we will need. Install the package `spyder-notebook` from the forge.
2. Go to Home and launch Spyder.
3. At the bottom, you will see two options: Editor and Notebook. Click on Notebook. Right click on the Welcome page and open the notebooks you have downloaded at step 1.
4. Alternatively, skip steps 3-5 and launch **Jupyter Notebook** via the Anaconda Navigator. Go to the course contents folder and start the notebooks you need.
5. You are now good to go and can save locally too.

### Visual Studio Code
See also: https://code.visualstudio.com/docs/python/python-tutorial

1. Download and install [VSCode](https://code.visualstudio.com/).
2. Install the Python plugin(s)
3. Open one of the notebooks in VSCode. You'll see that the Notebook's contents are rendered in the editor!

## Fallback online option: Binder

[Binder](https://mybinder.org/) is another service that allows you to run notebooks in the cloud. Just click on launch Binder in the repo. Remember to download any file you edited and want to preserve.

## For pros

This set-up allows to control code and Python at a lower level. For the purpose of the course, this is not needed nor recommended. You will need:

1. A rudimentary understanding of the terminal. The **terminal** is just an interface to execute commands in an operating system (most often, your local one).
2. A rudimentary understanding of git and GitHub. **git** is a program to version code, i.e. it allows you to keep track of different versions of your code. See here for a [tutorial](https://git-scm.com/docs/gittutorial). **GitHub** is instead an online service provided by a company, now part of Microsoft, which allows you to have multiple code repositories and interact with them via git. 
3. **Conda**. Conda is a cross platform package and environment manager that installs and manages conda packages from the Anaconda repository as well as from the Anaconda Cloud. Which means you will be able to a) create Python environments and b) install packages into them. Some packages we will use might not be in the Anaconda Cloud, in that case you can rollback to using `pip install`. You can use your main Python installation if you like, but I recommend using conda to keep experiments separated from the OS.
4. **Jupyter notebooks**, a package which allows you to run a web server and have interactive notebooks in it.
5. A **text editor** to write code when not using notebooks. If you don't already have a preferred one, check [Sublime Text](https://www.sublimetext.com/) or [Atom](https://atom.io/).

### How to get there

#### Basic terminal

For Mac OS and Linux (mostly):

* `ls` list folder contents
* `cd PATH` move current working directory to the PATH location. `cd ~` for your home folder
* `cd ..` goes up one level in the folder structure
* `touch fun.py` creates an empty file named `fun.py`
* `mv fun.py stuff/` moves `fun/py` to the `stuff` folder, if it exists. If it doesn, `mkdir stuff`

For more, see [here](https://www.makeuseof.com/tag/mac-terminal-commands-cheat-sheet/).

For Windows, see [here](https://www.thomas-krenn.com/en/wiki/Cmd_commands_under_Windows).

#### Getting class code and working on your own

##### The best way

1. The first time, clone the repository locally using `git clone https://github.com/bloemj/2022-coding-the-humanities.git`.
2. Keep getting updates to the code before every seminar by going to your local repository directory (e.g., `cd PATH_TO_REPO`) and `git pull`. This will pull all remote changes to local, and update your repository.

##### The easy way - 1 

You might want to use the [GitHub Desktop app](https://desktop.github.com) to keep track of your repositories. If you have it installed, instead of cloning the repo you can use the Open in Desktop option.

##### The easy way - 2

Just download the repository code before every lab, by clicking on `Clone or download`, and then `Download ZIP`. You will then need to unzip the downloaded file.

**IMPORTANT**: Either way, this copy of the course repo will conflict with any change you made yourself to the files in there. This is especially the case for the former way: if you pull, then you edit, then I edit, then you pull again, there will likely be a conflict if we both changed the same files. I recommend to put your edited copies of the repository contents in a separate folder, so to keep your edits (ideally, you could do versioning on a repository of your own!).




