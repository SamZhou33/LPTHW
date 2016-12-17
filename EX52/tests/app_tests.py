from nose.tools import *
from app import app
from tests.tools import assert_response

client = app.test_client() # create a testing client (a fake browser)
client.testing = True # enable this so that exceptions in your code bubble up to the test

def test_index():
    global client
    resp = client.get('/') # with this client you can do all kinds of stuff
    assert_response(resp, status='302') # the roat url should give back a redirect

    resp = client.get('/game')
    assert_response(resp) # just make sure we got a valid response

    # Go to another scene in the game
    testdata = {'userinput': 'tell a joke'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="Laser Weapon Armory")

    # From there, go to yet another scene
    testdata = {'userinput': '132'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contain="The Bridge")
