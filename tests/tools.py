from nose.tools import *
import re

def assert_response(resp, contains=None, matches=None, headers=None, status="200"):
	
	assert status in resp.status, "Expected repsonse %r not in %r" % (
				status, resp.status)
	
	if status == "200":
		assert resp.data, "response data is empty."
		
		if contains:
			assert contains in resp.data, "response does not contain %r" %(
				contains)
		
		if matches:
			reg = re.compile(matches)
			assert reg.matches(resp.data), "response doe snot match %r" %(
				matches)
		
		if headers:
			assert_equal(resp.headers, headers)