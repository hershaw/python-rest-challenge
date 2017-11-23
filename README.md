# The APP needs a MongoDB running to work.

The test are the original ones.
I'll improve the documentation tomorrow with some analysis of the test and my impressions,
or I could comment it live using Skype.

## For running the tests from the shell:
- go to "behave_tests" directory and run `behave`.

## For running the app from the shell:
- You can go to the app root directory and run `python src/flask_test.py`.

## Some important variables:
- APP_DEBUG_MODE = False
- APP_URL = "http://127.0.0.1:5000"

### For TESTING:
APP_START_TIME = 8

It's the time in seconds for the app before starting the tests.
Consider increasing it if it fails.

### Notes

Behave is brilliant, I reuse many of the steps. Some more could be done though.

For testing I've used a real db connection instead of a mock object.


## Some useful notes for programs I used
### MONGODB
sudo apt-get install  mongodb
mkdir -p /data/db
mongod --dbpath /data/db
mongod
mongod --shutdown

### FLASK
cd /home/pablo/src/tests/neovantas/python-rest-challenge/src
export FLASK_DEBUG=1
FLASK_APP=flask_test.py flask run


### VIRTUALENVWRAPPER
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/src/tests
export VIRTUALENVWRAPPER_VIRTUALENV_ARGS='--no-site-packages'
source /home/pablo/programs/anaconda3/bin/virtualenvwrapper.sh
workon
mkvirtualenv neo
setvirtualenvproject /home/pablo/.virtualenvs/neo /home/pablo/src/tests/neovantas/python-rest-challenge
workon neo

### BEHAVE
behave --no-capture # print stdout


### PIP

**if there is any issue, check pip-requirements-full-freeze.txt**

pip (9.0.1)
setuptools (36.7.2)
wheel (0.30.0)

pip install Flask
Successfully installed Flask-0.12.2 Jinja2-2.10 MarkupSafe-1.0 Werkzeug-0.12.2 click-6.7 itsdangerous-0.24

pip install Flask-PyMongo
Successfully installed Flask-PyMongo-0.5.1 PyMongo-3.5.1

pip install Flask-RESTful
Successfully installed Flask-RESTful-0.3.6 aniso8601-1.3.0 python-dateutil-2.6.1 pytz-2017.3 six-1.11.0

pip install webargs
Successfully installed marshmallow-2.14.0 webargs-1.8.1

### PIP for testing/developing
pip install requests
Successfully installed certifi-2017.11.5 chardet-3.0.4 idna-2.6 requests-2.18.4 urllib3-1.22

pip install ipdb
Successfully installed decorator-4.1.2 ipdb-0.10.3 ipython-6.2.1 ipython-genutils-0.2.0 jedi-0.11.0 parso-0.1.0 pexpect-4.3.0 pickleshare-0.7.4 prompt-toolkit-1.0.15 ptyprocess-0.5.2 pygments-2.2.0 simplegeneric-0.8.1 traitlets-4.3.2 wcwidth-0.1.7

pip install behave
Successfully installed behave-1.2.5 parse-1.8.2 parse-type-0.4.2

pip install sure
Successfully installed mock-2.0.0 pbr-3.1.1 sure-1.4.7

# THANK YOU :)

@hershaw
