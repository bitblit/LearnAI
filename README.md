# LearnAI

General place to jam stuff I wrote while learning about AI and ML

## Languages
I'm assuming I'll prolly be hitting Python, R, and some tertiary languages (LUA?) in here.  
This doc should hold how to set them up.

## Setting up the python VirtualEnv

All scripts in here (if any) will assume that the python virtual environment is created in a directory named
"python-env" which is directly under the LearnAI directory.  It will be git-ignored so it does not go into 
github.

All requirements go into requirements.txt as you'd expect.

The virtualenv should be created like so:

```
python3 -m venv python-env
source python-env/bin/activate
pip3 install -r requirements.txt
```

To leave the environment use : 

```
deactivate
```

### Installing new packages

First, switch to the python environment
 **source python-env/bin/activate**

 **pip install module-name**

(This will install it into the python-env enviroment)

If you need it in the deployment package (which you probably will) be sure to add it to the 
requirements.txt and full-virtualenv-requirements.txt files.

