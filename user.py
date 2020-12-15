from datetime import datetime

class Users:
	def _nit_(self, username, password):
		self.username = username
		self.password = password
		self.joined = datetime.now()
