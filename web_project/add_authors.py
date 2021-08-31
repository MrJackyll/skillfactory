from db import db_session, User

authors = [
	{
		'first_name': 'Vasya',
		'last_name': 'Petrov',
		'email': 'vasya@example.com'
	},
	{
		'first_name': 'Misha',
		'last_name': 'Ivanov',
		'email': 'miva@example.com'
	},
	{
		'first_name': 'Masha',
		'last_name': 'Nikolaeva',
		'email': 'mava@example.com'
	}
]

for a in authors:
	author = User (a['first_name'], a['last_name'], a['email'])
	db_session.add(author)

db_session.commit()