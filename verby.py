import http.client

def scan(resource):
	"""scans the given resource for http verbs."""
	verbs = [
		'HEAD',
		'OPTIONS',
		'GET',
		'PUT',
		'POST',
		'DELETE',
		'TRACE',
		'CONNECT',
		'OPTIONS',
		'PROPFIND'
	]

	for verb in verbs:
		conn = http.client.HTTPConnection(resource)
		conn.request(verb, '/')
		response = conn.getresponse()
		print("Verb: {:10s} Code: {}".format(verb, response.code))

if __name__ == '__main__':
	resource = input("Enter the resource to be scanned: ")
	scan(resource)