## Installing python
- Install latest LTS python version from https://www.python.org/downloads/

### Checking the installed python version
- Open command prompt and just type:

``
python --version
``

## Creating virtual environment for a project
- As a pre requisite python has to installed into the system globally. from there we can create a N number of virtual environments.
- To check where the python installed. run the command ``where python``
- To create a virtual env run the below command

```
For Linux:

python -m venv <path>/.venv

for windows:

python -m venv <path>/.venv

```
The second argument is the location to create the virtual environment. Generally, you can just create this in your project and call it .venv

venv will create a virtual Python installation in the .venv folder.

## Activating a virtual environment
- Before you can start installing or using packages in your virtual environment you’ll need to activate it. Activating a virtual environment will put the virtual environment-specific python and pip executables into your shell’s PATH

```
For Linux:

source .venv/bin/activate

for windows:

.\.venv\Scripts\activate
```
You can confirm you’re in the virtual environment by checking the location of your Python interpreter, it should point to the .venv directory
- Now if you type ``` where python``` you should be able to see two set up's one would be global and other one would be the cerated venv

## Leaving the virtual environment
- If you want to switch projects or otherwise leave your virtual environment, simply run: ``` deactivate ```
- If you want to re-enter the virtual environment just follow the same instructions above about activating a virtual environment. There’s no need to re-create the virtual environment.

## Installing packages
- Now that you’re in your virtual environment you can install packages

```
pip install <package_name [(== | >= | < | <= ) version]>
```
- For example, to install a requests package
``` pip install requests ```
- To install a specific version of requests package:
``` pip install requests==2.18.4```

- check list of installed packages just use: ``` pip list```

## To create project dependencies list
- It is always a good practice to maintain the list of packages that are being used in project to install it during the deployment.
- To create a requirement.txt just run: 

    ``` pip freeze -l > requirements.txt ```
- To install the list of packages from the requirement.txt

    ``` pip install -r requirements.txt ```

### For more information refer: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/