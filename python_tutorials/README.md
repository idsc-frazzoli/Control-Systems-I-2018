# Overleaf link
You can contribute to the tutorial using Overleaf at the following link:
https://v2.overleaf.com/1853683626rdmfgtjgcyxk. A preview of the current guide is 
reported in the following.

# PYTHON TUTORIAL

## What is Python?

Python is a high level, object oriented, interpreted language:
- __high level__: the programmer does not have to care about low-level implementation
 details such as registers, memory addresses but handles variables, arrays, 
 objects, logic constructors, loops.
 - __object oriented__ : programming is based on the concept of objects 
 which can contain data in form of fields known as _attributes_ and functions
 known as _methods_.
 - __interpreted__ : the original program is translated in something (_bytecode_) 
 that a virtual machine, called _interpreter_ can understand and execute. 
 
 ## Why Python?
 
 Python is:
 - __Easy to learn__ : few basic features and _self-explanatory_ syntax. Would you guess 
 what does the following code return? 
 ```python
if 3 in [1,2,3]: 
    print("Hello!")
```
- __Support__ :  the majority of libraries are open source with a big 
development and support community. If you are in trouble google your problem, in the
99 \% of the cases the answer is out there.

- __Object oriented__: in Python everything is an object. Thinking in a object
oriented way helps to better organize the code and facilitate the transition to 
more complex programming languages as C/C++.

## What Python is used for?

- __Data Science and Machine Learning__: Python is one of the most used 
programming language as high-level interface for machine learning and numerical algorithms 
libraries. During this course, we will make use of some of them: _numpy_,
_scipy_, _signal_ just to name a few.
- __Glue code__: it means that Python can interface and interoperate multiple
pieces of code together.
- __Web browsers and applications' GUI__.

### Which version?

Python 3.x is a newer version and as such supports newer features. On the other 
hand, python 2.7 will only receive updates until 2020 
[[1]](https://www.python.org/dev/peps/pep-0373/#id2), and is used for
facing compatibility issues. The tutorials and the course programming 
exercises will use python 3.x. If your PC already has another version, 
follow the provided installation instructions.

# IDEs

How do we write code? Theoretically the  minimum setup is given by any 
text editor and a python interpreter. This solution would work but is not 
the best for fast development and troubleshooting. IDEs are  programs designed
for making our lives easier.

IDE stands for Integrated Development Environment and is a program dedicated to 
software development. IDEs generally supports useful features such as:
- save and reload code files
- run code within the IDE
- built-in debugger
- syntax highlighting and auto-completion
- automatic code formatting: this is  an important features since python is a "indention based" programming 
language, meaning that 
 ```python
for i in range(2):
   print(1)
   print(2) 
```
and 
 ```python
for i in range(2):
    print(1)
print(2)
``` 
give different results, respectively:  
 ```python
>> 1
>> 1
>> 2
>> 2
``` 
and

```python
>> 1
>> 1
>> 2
```
A good editor will highlight code blocks and indentation errors, making debugging easier. 

## What is a Jupyter Notebook?

The Jupyter Notebook is an open-source web-based application that allow you to create and show 
documents that contain live code, equations, visualizations and narrative text. It is used for numerical 
simulations, modeling, data visualization, etc [[2]](http://jupyter.org/).

The Jupyter Notebook App can be executed on a local desktop and in addition to displaying/editing/running notebooks
documents, has a "dashboard", a "control panel" showing local files and able to run and close active kernels.

In the following sections, we will guide you through the installation instructions of PyCharm, one of the most used 
python IDE and the Jupyter Notebook. The first will be used for development and main tool for coding. The second will
be a useful tool for reports, data visualization and the coming python tutorials.
     
     
## Installation instructions (Windows/Linux)

### 1. Setup Python 

#### Using Anaconda
A convenient way to install python 3.x together with the  Jupyter application is to use
the Anaconda distribution. The advantage is that you have access to over 720 
scientific packages. The system requirement is around 3 Gb of free space on disk.

- **Linux**
    
    1. Go to <https://www.anaconda.com/download/>, select and save _Python 3.6 version_
    2. Open a terminal, go to the download folder and change the script mode to executable. 
    Then execute the script: 
        ```bash
        ~$ cd {installation folder path}
        ~{installation-folder-path}$ chmod +x Ananconda3-5.2.0-linux-x86_64.sh
        ~{installation-folder-path}$ ./Ananconda3-5.2.0-linux-x86_64.sh
        ``` 
    3. Follow the installations instructions in the terminal and when asked to install 
    Visual Studio Code, prompt _no_.
    4. Add Anaconda path to the system PATH. Open with your favourite editor the bash file `.bashrc`. E.g, using `gedit`:   
        ```bash
        ~$ gedit .bashrc
        ```
        and append the line
        ```
        export PATH={anaconda3-install-directory}/bin:$PATH
        ```
        Save and exit. In the terminal type `~$ source ./bashrc`. You can verify the installation typing:
        ```
        ~$ conda
        ``` 
    the _conda_ command manual will show in the terminal. **conda** is a tool for managing and deploying applications, environments and packages. For installing a new package you can simply type `conda install <package_name>` in a terminal console. 

- **Windows**
    1. Go to <https://www.anaconda.com/download/>, select and save _Python 3.6 version_
    2. Click on the downloaded executable and follow the default installation instructions. Do not install Visual Studio. 
    3. Add Anaconda path to the system PATH.
    - open a windows terminal by typing `cmd` in the search window. Click  on `Command Prompt`.
    - type `set PATH=%PATH%;<absolute\path\to\anaconda\installation>;<absolute\path\to\anaconda\installation>/Scripts`        
    In my case it was:
        `C:\Users\giuseppe>> set PATH=%PATH%;C:\Users\giuseppe\Anaconda3;C:\Users\giuseppe\Anaconda3\Scripts`

#### Using `apt-get` and `pip` (recommended for Linux)
Ubuntu 16.04, and other versions of Debian Linux ship with both Python 3 and Python 2 pre-installed. 
To make sure that our versions are up-to-date, let’s update and upgrade the system with apt-get:
```
~$ sudo apt-get update
~$ sudo apt-get -y upgrade
```
The `-y` flag will confirm that we are agreeing for all items to be installed, but depending on your version
 of Linux, you may need to confirm additional prompts as your system updates and upgrades.
Once the process is complete, we can check the version of Python 3 that is installed in the system by typing:
```
~$ python3 -V
```
You’ll receive output in the terminal window that will let you know the version number. 
The version number may vary depending on whether you are on Ubuntu 16.04, or another version of Linux,
 but it will look similar to this:
```
Python 3.5.2
```
To manage software packages for Python, let’s install pip:
```
~$ sudo apt-get install -y python3-pip
```
A tool for use with Python, pip installs and manages programming packages we may want to use in our development projects. You can install missing Python packages typing:
```
~$ pip3 install --user {package_name}
```
Here, _package_name_ can refer to any Python package or library.
So if you would like to install NumPy, you can do so with the command pip3 --user install numpy.
The option user is to make sure that installation is local and not system-wide. 
There are a few more packages and development tools to install to ensure that we have a robust set-up
for our programming environment:
```
~$ sudo apt-get install build-essential libssl-dev libffi-dev python3-dev
```
#### 1.2 Installing Jupyter

**With Anaconda** : Anaconda already comes with Jupyter Notebook app. 

- **Linux**

    You need to add Anaconda's bin folder to the PATH environment variable in order to find the Jupyter Notebook application
    (if you still did not do it in the previous steps).
    - Modify the `.bashrc` file. You can use any text editor, in the example we use gedit:
     ` ~$ gedit .bashrc`
    - Append the following line ` ~$ export PATH={anaconda3-install-directory}/bin:$PATH`.
    - Save and exit.
    - In the terminal type `~$ source ./bashrc`
    - Now you can open the Jupyter web server typing the command `~$ jupyter notebook` 
- **Windows**
    - In your Start menu, after Anaconda installation, you'll have a bunch of neat new tools, including an entry for Jupyter Notebook. 
Click to start it up and it will launch in the background and open up your browser to the notebook console.

**With pip3 (Linux)**

First, ensure that you have the latest pip: older versions may have trouble with some dependencies:

```
~$ python3 -m pip install --user --upgrade pip
```
Then install the Jupyter Notebook using:

```
~$ python3 -m pip install --user jupyter
```
You can now start using Jupyter Notebook typing `jupyter notebook` in a open terminal. 
 

### 2. PyCharm

PyCharm is the _standard de facto_ IDE for professional development of Python applications.
As a student, you are eligible for the free professional version. 

1. Go to <https://www.jetbrains.com/shop/eform/students>, fill the form with your
details and follow the registration instructions. 
2. You can now login with your new credentials at <http://www.jetbrains.com> and access 
to all tools available for downlads with student license.
3. Under the tab _download_ select _PyCharm 2018.2.2_ and download the Linux or Windows distribution.
    
    **Linux**
    
     - Extract the content of the tar archive in your favourite directory
     - Open a console and cd into the PyCharm folder:
        ```bash
        ~$ cd ~/{pycharm-dir}/bin
        ~/{pycharm-dir}/bin$ ./pycharm.sh
        ``` 
     - Activate the program using your jetbrains credentials.
     - Follow the installation instructions and immediately start PyCharm creating the 
first untitled project. We require this step for creating a icon from which we
can easily start PyCharm. In the IDE window, click _Tools_ first and then select 
_Create Desktop Entry_, press _Ok_.   
     - You can now close the IDE and open it from the launcher icon. 
    
    **Windows**
    
    - Follow the Graphical installer instructions. 
    - Check 32-bit launcher or 64-bit launcher according to your platform and `associate .py extension` so that Windows will authomatically use Pycharm as default program for opening python scripts. 
    - Activate the program using your jetbrains credentials.
   
#### 2.1 Using Jupyter Notebook in PyCharm

Any python script (program) belongs to a _project_. Create a new folder 
called _test_, this will contain all projects files. You can create a project by 
opening your brand new PyCharm and selecting _New Project_. This will open the
_Create Project_ window. 
Specify as location the _test_ folder by clicking on the three dots and 
navigating through the dialog window. Do not click on _Create_  yet. 
 

Before starting with coding , we need to select the proper interpreter.
Linux comes with a preinstalled python 2.7 and Python 3. You can either chose Python 3 interpreter
shipped with native Ubuntu or in case you want to use additional packages provided by Anaconda 
we need to change it to the Anaconda interpreter. After we add this 
new entry, it will not be necessary to repeat these steps for future projects.
1. In the _Create Project_ window click on _Project Interpreter: Python x.x_.
2. After selecting _Existing Interpreter_ specify the Anaconda interpreter if you previously installed it. 
For Windows users, after clicking _Existing Interpreter_, just select _System interpreter_ on the 
left and PyCharm will authomatically select the Anaconda interpreter. In case you did not install Anaconda, just
select the default python 3.x interpreter. 
Again, click on the three dots and navigate to the Anaconda installation folder.   
3. Finally, click on _Create_.

The apparently scary PyCharm IDE window will appear. Do not panic. We will not 
need all of its features and you will learn more by practising
this great tool. The created project is empty, but not for long! 
In the leftmost column (the _Project Explorer_) right click onto the 
project folder (_test_), then _New_ -> _Python File_. Call it _hello_.
Repeat the same procedure but now create a Jupyter Notebook file by selecting
the corresponding entry in the scroll-down menu. Now your project will contain 2 files:
- test
    - hello.ipynb
    - hello.py

### My first Python program

Double click on _hello.py_. In the editor window, start writing
your first Python program by typing: 
 ```python
print("Hello world!")    
``` 
In order to run the code you can go to _Run_ -> _Run 'hello'_. The output
will likely be similar to the following:
 ```bash
/home/username/anaconda3/bin/python /home/username/test/hello.py
Hello world!
Process finished with exit code 0
``` 
Congratulations! You have successfully run your first python program. 

### My first Jupyter Notebook 

- **First method (recommended)**

If you are a Linux user open a terminal and type `jupyter notebook`. If you are a Windows user just open the Jupyter client from the Start Menu. Jupyter dashboard will appear, showing the content of the local  directory. Navigate to the folder where you want your first notebook to be saved. Than click on `New`->`Python3`. A new notebook named `Untitled` will open. Clik on `Untitled` and give it a new name, like `FirstNotebook`. Alternatively you can navigate to the new notebook created in the `test` project. Jupyter notebooks have 2 types of line:
- _code line_:  where you can write normal Python code
- _markdown line_: where you can write explanatory text in **Markdown**. You can 
find a Markdown cheat sheet [here](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#code).

Click on the first line and type `print("Hello world!")`
Click on the plus sign, this will add a new line. Generally the newly added line will be a code line. To change its mode to Markdown, select Markdown from the scroll-down menu. 
Copy past the following text: 
> The command \`print(string)\` \_prints\_ to screen \*\*string\*\*.

Now select the first code line and click on the play button. This will run the code contained inside the cell. For any code cell, Jupyter associate a pair of square brackets. 
An astericks appears inside if the cell is running, after the cell is run they instead 
contain an execution number. 
You can understand in which order the code cells where executed looking at the cell 
numbers. Although a notebook should be designed to run all code cells in a sequential 
order, you are free to run any cell at any time. 
Note that the cell will access to the variables known to the interpreter up to the previously executed cells only. 
Now the following Markdown cell will be authomatically selected. 
You can run it and visualize the highlighted text. 
As you see, Markdown uses **underscores**, **asterisks**, **dashes** 
and **indentation** to provide test highlighting and nested lists. 
Title of different sizes can be obtained using multiple **hashtags** 
(for more, see this [guide](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#code)). 

That's it! Now you can open, run, edit all notebooks contained in the downloadable tutorial folder. Have fun!

- **Second method**: editing notebooks with Pycharm

Double click on _hello.ipynb_. In the Pycharm editor window,  you will see a code line.
 ```python
print("Hello world!")    
``` 
Add one line using the plus icon. Change its mode to _Markdown_ and copy past the following text: 
> The command \`print(string)\` \_prints\_ to screen \*\*string\*\*.

Now it is time to run the Jupyter Notebook. Click on the _Run_ icon and
in the next window cancel its content and then click _Ok_. A dialogue window
will appear saying _Cannot connect to Jupyter Notebook. Run Jupyter Notebook_. 
Click on _Run Jupyter Notebook_ and then _Run_ on the settings window. 
This will start a Jupyter Notebook in the browser. You can connect to the server
clicking on the url address which will appear in the PyCharm run window.
You will visualize the "Dashboard" with all the files contained in your local folder _test_. Open _hello.ipynb_ 
and select _Cell_ -> _Run all_.

All cells are run in increasing line number order. Right after any code cell you can see the corresponding
output (if the code actually generated any output) while any Markdown cell is converted to highlighted text.
If you followed correctly all instructions you will see something similar to
   >```python
   >ln[1] : print("Hello world!")
   >``` 
   >Hello world! <br/>
   > The command `print(string)` _prints_ to screen **string**.

Now any change you apply on the web server can be saved to the local machine and viceversa. 
Congratulations! You have successfully run your first Jupyter Notebook. 
Note that the second procedure is a bit more complicated and Pycharm support for Jupyter notebooks is pretty poor.
We suggest you to follow the previous instructions and avoid Pycharm, except rare cases, for editing a Jupyter notebook. 

## What's next?

We will use Jupyter notebooks for give you a basic python introduction. You can walk through the tutorials, 
running each line sequentially. We strongly encourage you to interact with the notebook and try to change the code.
In this way you can get a better understanding of how your changes affect execution and output.  

PyCharm will be the main tool for coding once you became familiar with Python.
It is a good practice to write a clear documentation. The reader, might it be a professor, a customer or
even yourself after some time, will easily understand it and follow the logic of the implemented algorithms.

Jupyter Notebooks can be extremely useful for explaining and visualizing data. You might want to make use 
of it for either reporting or part of your documentation.
  
