import json

my_json = '''
[
	{"title": "Title #1", "body": "Hello, World1!"},

	{"title": "Title #2", "body": "Hello, World 2!"}
]
'''


# my_json = '''

# {
# 	"ivan":
# 		[
# 			{"title": "Title #1", "body": "Hello, World1!"},

# 			{"title": "Title #2", "body": "Hello, World 2!"}
# 		]
# }
# '''








#my_json = json.dumps(my_json)
# print(my_json)

a = ''
parsed_string = json.loads(my_json)
for tag in parsed_string:	
	for key, value in tag.items():
		if key == 'title':
			a += '<h1>' + value + '</h1>'
		if key == 'body':
			a += '<p>' + value + '</p>'
print(a)



# new = json.dumps(parsed_string, indent=10)
# print(new)





# with open('ivan.json') as file:
# 	my_kai = loads(file)


# with open("my_json", "w", encoding="utf-8") as file:
#     json.dump(my_json, file)
















