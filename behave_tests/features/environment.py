'''
Created on 22 Nov 2017

@author: pablo
'''
import pymongo


BEHAVE_DEBUG_ON_ERROR = False
DB_HOST = 'localhost'
DB_PORT = 27017
APP_URL_BASE = 'http://localhost:5000/'

def setup_debug_on_error(userdata):
    global BEHAVE_DEBUG_ON_ERROR
    BEHAVE_DEBUG_ON_ERROR = userdata.getbool("BEHAVE_DEBUG_ON_ERROR")


def before_all(context):
    setup_debug_on_error(context.config.userdata)


def before_scenario(context, scenario):
    '''
    We get a clean database before every scenario.
    '''


def after_scenario(context, feature):
    '''
    We don't drop the database so it could be inspected.
    '''
    if 'app_process' in context:
        context.app_process.terminate()
        context.app_process.wait()


def after_step(context, step):
    '''
    if BEHAVE_DEBUG_ON_ERROR:
        Enable debug on errors

    :param context:
    :param step:
    '''
    if BEHAVE_DEBUG_ON_ERROR and step.status == "failed":
        # -- ENTER DEBUGGER: Zoom in on failure location.
        # NOTE: Use IPython debugger, same for pdb (basic python debugger).
        import ipdb
        ipdb.post_mortem(step.exc_traceback)

