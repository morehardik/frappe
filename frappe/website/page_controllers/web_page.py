import frappe

class WebPage(object):
	def __init__(self, path=None, http_status_code=None):
		self.headers = None
		self.http_status_code = http_status_code or 200
		if not path:
			path = frappe.local.request.path
		self.path = path.strip('/ ')
		self.basepath = ''

	def get(self):
		if self.validate():
			return self.render()

	def validate(self):
		pass

	def render(self):
		pass

