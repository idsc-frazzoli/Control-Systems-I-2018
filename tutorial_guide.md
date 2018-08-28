# PYTHON TUTORIAL

## What is Python?

Python is a high level, object oriented, interpreted language:
- __high level__: the programmers does not have to care about low-level implementation
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
     
     
## Installation instructions Linux

### 1. Anaconda 

A convenient way to install python 3.x together with the  Jupyter application is to use
the Anaconda distribution. The advantage is that you have access to over 720 
scientific packages. The system requirement is around 3 Gb of free space on disk.

1. Go to <https://www.anaconda.com/download/#linux>, select and save _Python 3.6 version_
2. Open a terminal, go to the download folder and change the script mode to executable. 
Then execute the script: 
    ```bash
    ~$ cd {installation folder path}
    ~{installation-folder-path}$ chmod +x Ananconda3-5.2.0-linux-x86_64.sh
    ~{installation-folder-path}$ ./Ananconda3-5.2.0-linux-x86_64.sh
    ``` 
3. Follow the installations instructions in the terminal and when asked to install 
Visual Studio Code, prompt _no_.
4. You can verify installation by typing 
    ```bash
    ~$ export PATH={anaconda3-install-directory}/bin:$PATH
    ~$ conda
    ``` 
    the _conda_ command manual will show in the terminal. **conda** is a tool for managing and deploying applications, environments and packages.

### 2. PyCharm

PyCharm is the _standard de facto_ IDE for professional development of Python applications.
As a student, you are eligible for the free professional version. 

1. Go to <https://www.jetbrains.com/shop/eform/students>, fill the form with your
details and follow the sign-in instructions. 
2. You can now login with your new credentials at <http://wwww.jetbrains.com> and access 
to all tools available for downlads with student license.
3. Under the tab _download_ select _PyCharm 2018.2.2_ and download the Linux distribution.
4. Extract the content of the tar archive in your favourite directory
5. Open a console and cd into the PyCharm folder:
    ```bash
    ~$ cd ~/{pycharm-dir}/bin
    ~/{pycharm-dir}/bin$ ./pycharm.sh
    ``` 
    Activate the program using your jetbrains credentials.
6. Follow the installation instructions and immediately start PyCharm creating the 
first untitled project. We require this step for creating a icon from which we
can easily start PyCharm. In the IDE window, click _Tools_ first and then select 
_Create Desktop Entry_, press _Ok_.   
You can now close the IDE and open it from the launcher icon. 

## Using Jupyter Notebook in PyCharm

Any python script (program) belongs to a _project_. Create a new folder 
called _test_, this will contain all projects files. You can create a project by 
opening your brand new PyCharm and selecting _New Project_. This will open the
_Create Project_ window. 
Specify as location the _test_ folder by clicking on the three dots and 
navigating through the dialog window. Do not click on _Create_  yet. 
 

Before starting with coding (the fun part), we need to select the proper interpreter.
Linux comes with a preinstalled python 2.7 which PyCharm recognizes and uses as 
default interpreter. We need to change it to the Anaconda interpreter. After we add this 
new entry, it will not be necessary to repeat these steps for future projects.
1. In the _Create Project_ window click on _Project Interpreter: Python x.x_.
2. After selecting _Existing Interpreter_ specify the Anaconda interpreter. 
Again, click on the three dots and navigate to the Anaconda installation folder. 
Alternatively, you can just type  `~/{anaconda3-path}/bin/python`. 
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

Double click on _hello.ipynb_. In the editor window,  you will see a line.
Any notebook consists of different type as Markdown (a way for writing highlighted text) and
python code for example. Select the type to _Code_ and type 
 ```python
print("Hello world!")    
``` 
Add one line using the plus icon. Change its mode to _Markdown_ and type 
 ```python
This is my first **Jupyter notebook**.
``` 
In Markdown quoting with double asterisks makes the text in between bold. You can 
find a Markdown cheat sheet at [here](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#code). 


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
   >This is my first **Jupyter notebook**.

Now any change you apply on the web server can be saved to the local machine and viceversa. 
Congratulations! You have successfully run your first Jupyter Notebook. 

## What's next?

We will use Jupyter notebooks for give you a basic python introduction. You can walk through the tutorial 
running each line sequentially. We strongly encourage to interact with the notebook and try to change the code.
In this way you can get a better understanding of how your changes affect execution and output.  

PyCharm will be the main tool for coding once you became familiar with Python.
It is a good practice to write a clear documentation. The reader, might it be a professor, a customer or
even yourself after some time, will easily understand it and follow the logic of the implemented algorithms.

Jupyter Notebooks can be extremely useful for explaining and visualizing data. You might want to make use 
of it for either reporting and as part of your documentation.
  