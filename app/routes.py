from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Hellboy'}
	return '''
	<html>
	<head>
	<title>Home Page - Microblog</title>
	</head>
	<body>
	<h1>Hello, ''' + user['username'] +  ''' My Lord!</h1>
	</body>
	</html>
	'''