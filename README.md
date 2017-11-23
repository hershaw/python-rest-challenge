# The APP needs a MongoDB running to work.

Please, let me know about any question you may have.

## For running the tests from the shell:
- go to "behave\_tests" directory and run `behave`.

## For running the app from the shell:
- You can go to the app root directory and run `python src/flask\_test.py`.

## Some important variables:

src/flask\_test.py
- APP\_DEBUG\_MODE = False
- APP\_URL = "http://127.0.0.1:5000"

features/environment.py
- BEHAVE\_DEBUG\_ON\_ERROR = False
- DB\_HOST = 'localhost'
- DB\_PORT = 27017
- APP\_URL\_BASE = 'http://localhost:5000/'

features/steps/load\_application\_api.py
- TEST\_DB\_NAME = 'test\_db\_to\_be\_deleted\_' + get\_current\_file\_basename\_without\_extension(\_\_file\_\_)
- APPLICATION\_URL = APP\_URL\_BASE + 'application'
- APP\_START\_TIME = 8
- APP\_SRC\_DIRECTORY = get\_app\_src\_directory()


### For TESTING:
APP\_START\_TIME = 8

It's the time in seconds for the app before starting the tests.
Consider increasing it if it fails.

### Notes

Behave is brilliant, I reuse many of the steps. Some more could be done though.

For testing I've used a real db connection instead of a mock object.
I suppose that a standard way of testing it exists. 

I used flask\_rest because I like the organization of HTTP methods in classes,
I also like to have all the app url defined together.

The test are the original ones.

I found the challenge reasonable to be done with 5 hours if now the tecnologies involved.
In my case I spent many time  setting up the environment and learning and combining them.

## Some useful notes for programs I used
### MONGODB
sudo apt-get install  mongodb
mkdir -p /data/db
mongod --dbpath /data/db
mongod
mongod --shutdown

### FLASK
cd /home/pablo/src/tests/neovantas/python-rest-challenge/src
export FLASK\_DEBUG=1
FLASK\_APP=flask\_test.py flask run


### VIRTUALENVWRAPPER
export WORKON\_HOME=$HOME/.virtualenvs
export PROJECT\_HOME=$HOME/src/tests
export VIRTUALENVWRAPPER\_VIRTUALENV\_ARGS='--no-site-packages'
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

