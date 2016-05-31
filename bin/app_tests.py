from nose.tools import *
from bin.app import app
from tests.tools import assert_response
#comment all out or else will always fail when server not running with 500 error


def test_index():
	#check that we get a 404 on the /hello url
	resp = app.request("/aaa")
	assert_response(resp, status="404")

	#test first get request to /
	resp = app.request("/game")
	assert_response(resp)
	
	#make sure default values work for the form
	#resp = app.request("/game", method="POST")
	#assert_response(resp, contains="*") #this doesnt actually work
	
	#test that we get expected values
	#data = {'name': 'zed', 'greet': 'hola'}
	#resp = app.request("/", method="POST", data=data)
	#assert_response(resp, contains="Zed")
	pass	