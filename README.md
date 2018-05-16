
Hana to Python Application
===================

The purpose of this project is to implement a simple Python application to demonstrate the integration between a common third party application to a SAP Hana database.

> **Note:**
> 
> - This project is directly linked to  the project at the [HanaService](https://github.com/NickChecan/HanaService) repository.
> - Project developed with Python 3.7.


----------

Project Components
-------------

This project uses the [Flask](http://flask.pocoo.org/) framework to serve data through a simple web site platform locally. 

```
HanaToPython-Application
	├── app
	│    ├── modules
	│    │    ├── Controller.py
	│    │    ├── Model.py
	│    │    └── __init__.py
	│    ├── templates
	│    │    └── index.html
	│    └── __init__.py
	├── config.py
	├── requirements.txt
	└── run.py
```

The routes used in this application can be found at **./app/modules/Controller.py**.

The **.app/modules/Model.py** file will be responsible to access the Hana data through a database connection established by the information provided at the **config.py** file.

The template folder will handle all views available for the application.

The file **requirements.txt** contains all the plugins used for the current application and the **run.py** file will be responsible for the application execution.


----------

Getting Started
-------------

Before importing this project to your Python workspace, it is necessary to make sure the prerequisites steps are properly done in your development environment.
The installation procedure described in this documentation will assume you've already have Python installed at your computer.

#### <i class="icon-layers"></i> Prerequisites

 - Hana Service </br>
 To execute this application it will be necessary to properly deploy the [Hana Service](https://github.com/NickChecan/HanaService) project into your Hana Trial environment.

 - A Python Editor of your choice </br>
 For this project the [PyCharm](https://www.jetbrains.com/pycharm/) IDE and [Visual Studio Code](https://code.visualstudio.com/) were used for development, but the same is not required to correctly deploy the application it self.

 - Install the virtual environment package </br>
 **Virtual Environment** (virtualenv) is a tool to create isolated Python environments. The *virtualenv* command creates a folder which contains all the necessary executables to use the packages that a Python project would need. The same can be installed as described in [this link](http://docs.python-guide.org/en/latest/dev/virtualenvs/) through the following command:

```
$ pip install virtualenv
```


#### <i class="icon-download"></i> Installing

The steps bellow will guide you through the project installation.  </br>
The following commands should be executed in your computer console at the project folder:

* Clone the project to your local repository workspace;

* Create a virtual environment for the imported application through the following command:
```
$ virtualenv <Virtual Environment name>
```
* Activate your virtual environment with the command:
```
$ <Virtual Environment name>\Scripts\activate
```
 * With the virtual environment properly activated, install the plugins available at the **requirements.txt** file through the command:
```
$ pip install -r requirements.txt
```
This process should enable your application to be deployed in a local server for test purpose.


> **Note:**
> 
> - With the [Hana Service](https://github.com/NickChecan/HanaService) properly deployed, the **config.py** file should be modified to attend the address of your Hana Trial Instance.


----------

Deployment
-------------

With the Hana Service properly deployed, the **config.py** file modified to attend your Hana Trial Instance and the virtual environment activated, the python application should run through the following command:

```
$ python run.py
```

The same will enable the project to be accessed by you web browser trough a URL displayed by the mentioned command execution.

> **Tips:**
> 
> - As mentioned in the Hana Service project repository, always remember to make sure the Hana Trial Instance is up and running through the Cloud Platform Cockpit before execute commands or test any application directly linked to the Hana Service.



Acknowledgments
-------------
This project was made possible thanks to the Flask framework tutorials available at the [Tutorials Point](https://www.tutorialspoint.com/flask/) and at [Bruno Rocha](http://brunorocha.org/) personal blog. These two web sites was incredibly helpful in the development and preparation step of this project.
