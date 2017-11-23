# -*- coding: utf-8 -*-
'''
@author: pablo
'''
import os
import subprocess
import sys
import time

import behave
import bson.objectid
import pymongo
import requests
import sure

from environment import DB_HOST, DB_PORT, APP_URL_BASE


def get_current_file_basename_without_extension(file_name):
    current_file_basename = os.path.basename(file_name)
    return os.path.splitext(current_file_basename)[0]


def get_app_src_directory():
    head = os.path.abspath(__file__)
    for i in range(4):
        head, tail_= os.path.split(head)
    return os.path.join(head, 'src')


# TEST_DB_NAME cold also include the current date/time
# if we are interested on keeping it for inspection.
TEST_DB_NAME = 'test_db_to_be_deleted_' + get_current_file_basename_without_extension(__file__)
APPLICATION_URL = APP_URL_BASE + 'application'
APP_START_TIME = 8
APP_SRC_DIRECTORY = get_app_src_directory()


# ===============================================================================
# given
# ===============================================================================

@behave.given('the webserver is available')
def step_impl(context):
    '''
    This is a good candidate for environment.py "before_scenario" function
    as it is repeated in all the scenarios
    '''
    context.db_client = pymongo.MongoClient(DB_HOST, DB_PORT)  # .mongo_client
    db_names = context.db_client.database_names()
    if TEST_DB_NAME in db_names:  # Will fails if the webserver is not available.
        context.db_client.drop_database(TEST_DB_NAME)
    context.app_process = subprocess.Popen(['python',
                                            '-m',
                                            'flask_test',
                                            '--dbname',
                                            TEST_DB_NAME],
                                           cwd=APP_SRC_DIRECTORY)
    time.sleep(APP_START_TIME)


@behave.given('a valid application is generated')
def step_impl(context):  # @DuplicatedSignature
    context.application = {"age": "20",
                           "income": "1000",
                           "employed": "True"}


@behave.given('an application with age missing is generated')
def step_impl(context):  # @DuplicatedSignature
    context.application = {"income": "1000",
                           "employed": "True"}


@behave.given('an application with age as a string is generated')
def step_impl(context):  # @DuplicatedSignature
    context.application = {"age": "age as a string",
                           "income": "1000",
                           "employed": "True"}


@behave.given('an application exists in the database with id specialid')
def step_impl(context):  # @DuplicatedSignature
    context.application = {"age": "20",
                           "income": "1000",
                           "employed": "True"}
    context.response = requests.post(APPLICATION_URL, json=context.application)
    (context.response).shouldnt.be.equal(None)
    context.specialid = context.response.json()['id']
    (bson.objectid.ObjectId.is_valid(context.specialid)).should.be.equal(True)


# ===============================================================================
# when
# ===============================================================================


@behave.when('the endpoint POST /application is called')
def step_impl(context):  # @DuplicatedSignature
    context.response = requests.post(APPLICATION_URL, json=context.application)


@behave.when('GET /application/specialid is called')
def step_impl(context):  # @DuplicatedSignature
    context.response = requests.get(APPLICATION_URL + '/' + context.specialid)


@behave.when('DELETE /application/specialid')
def step_impl(context):  # @DuplicatedSignature
    context.response = requests.delete(APPLICATION_URL + '/' + context.specialid)


@behave.when('PATCH /application/specialid is called to update age')
def step_impl(context):  # @DuplicatedSignature
    context.udated_application = context.application.copy()
    context.udated_application['age'] = '30'
    context.response = requests.patch(APPLICATION_URL + '/' + context.specialid, json=context.udated_application)


# ===============================================================================
# then
# ===============================================================================


@behave.then('the application is returned with an id')
def step_impl(context):  # @DuplicatedSignature
    (context.response).shouldnt.be.equal(None)
    application_id = context.response.json()['id']
    (bson.objectid.ObjectId.is_valid(application_id)).should.be.equal(True)


@behave.then('status {status_code:d} is returned')
def step_impl(context, status_code):  # @DuplicatedSignature
    (context.response.status_code).should.be.equal(status_code)


@behave.then('the loan exists in the database')
def step_impl(context):  # @DuplicatedSignature
    response = requests.get(APPLICATION_URL + '/' + context.response.json()['id'])
    (response.json()['_id']).shouldnt.be.equal(None)


@behave.then('an error message saying {message} is returned')
def step_impl(context, message):  # @DuplicatedSignature
    '''
    Unnecessary parameter for only two cases.
    Having two methods instead would be more readable.
    '''
    attribute_name = message.split()[0]
    response_dict = context.response.json()
    (response_dict).should.have.key('messages').which.should.have.key(attribute_name)
    attribute_message = response_dict['messages'][attribute_name]
    if message.endswith('is missing'):
        (attribute_message).should.be.equal(['Missing data for required field.'])
    elif message.endswith('has wrong type'):
        (attribute_message).should.be.equal(['Not a valid integer.'])


@behave.then('the correct application is returned')
def step_impl(context):  # @DuplicatedSignature
    response = requests.get(APPLICATION_URL + '/' + context.specialid)
    response_dict = response.json().copy()
    (response_dict['_id']).shouldnt.be.equal(None)
    response_dict.pop('_id')
    (response_dict).shouldnt.be.equal(context.application)


@behave.then('the updated age is recorded in the database')
def step_impl(context):  # @DuplicatedSignature
    response = requests.get(APPLICATION_URL + '/' + context.specialid)
    response_dict = response.json().copy()
    (response_dict['_id']).shouldnt.be.equal(None)
    response_dict.pop('_id')
    (response_dict).shouldnt.be.equal(context.udated_application)


@behave.then('the application with id specialid is no longer in the database')
def step_impl(context):  # @DuplicatedSignature
    response = requests.get(APPLICATION_URL + '/' + context.specialid)
    response_dict = response.json()
    (response_dict).should.have.key('message').which.should.contain('requested URL was not found on the server')


if __name__ == '__main__':
    behave_execution_path = os.path.dirname(os.path.abspath(__file__))
    if behave_execution_path.endswith('/steps'):
        behave_execution_path = behave_execution_path[:-len('steps')]
    print('behave_execution_path', behave_execution_path)
    from behave.__main__ import main as behave_main
    behave_main(behave_execution_path + " --no-capture")
