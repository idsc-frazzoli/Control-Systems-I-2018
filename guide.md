# PYTHON TUTORIAL

## What is Python?

Python is a high level, object oriented, interpreted language:
- __high level__: the programmers does not have to care about low-level implementation
 details such as registers, memory addresses but hanles variables, arrays, 
 objects, logic constructors, loops.
 - __object oriented__ : programming is based on the concept of objects 
 which can contain data in form of fields known as _attributes_ and functions
 known as _methods_.
 - __interpreted__ : the original program is translated in something (_bytecode_) 
 that a virtual machine, called _interpreter_ can understand and execute. 
 
 ## Why Python?
 
 Python is:
 - __Easy to learn__ : few basic features and _self-explanatory_ syntax. Would you guess 
 what the following code return? 
 ```python
if 3 in [1,2,3]: 
    print("Hello!")
```
- __Support__ : it is open source as well as the majority of librairies with a big 
development and support community. If you are in trouble google your problem, in the
99 \% of the cases the answer is out there

- __Object oriented__: in Python everything is an object. Thinking in a object
oriented way helps to better organize the code and facilitate the transition to 
more complex programming languages as C/C++.

## What Python is used for?

- __Web browsers and applications' GUI__
- __Data Science and Machine Learning__: Python is one of the most used 
programming language as high-level interface for machine learning and numerical algorithms 
libraries. During this course, we will make use if some of them: numpy,
scipy, signal just to name a few.
- __Glue code__: it means that Python can interface and interoperate multiple
pieces of code together.

### Which version?

Python 3.x is a newer version and as such supports newer features. On the other 
hand, python 2.7 will only receive updates until 2020 
[[1]](https://www.python.org/dev/peps/pep-0373/#id2), and is used for
facing compatibility issues. The tutorials and the course programming 
exercises will use python 3.x. If your PC already have another version, 
follow the provided installation instructions.

# IDEs

How do we write code? Theoretically the  minimum setup is given by any 
text editor and a python interpreter. This solution would work but is not 
the best for fast development and troubleshooting. IDEs are  programs designed
for making our lives easier.

IDE stands for Integrated Development Environment and is a program dedicated to 
software development. IDEs generally supports usuful features such as:
- save and reload code files
- run code within the IDE
- code debugger
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

The Jupyter Notebook App can be executed on a local desktop an din addition to displaying/editing/running notebooks
documents, has a "dashboard", a "control panel" showing local files and able to run and close active kernels.

In the following chapter we will guide you through the installation instructions of PyCharm, one of the most used 
python IDE and the Jupyter Notebook. The first will be used for development and main tool for coding. The second will
be a useful  tool for reports, data visualization and the coming python tutorials.
     