import json

# my_json = '''
# [
# 	{"title": "Title #1", "body": "Hello, World1!"},

# 	{"title": "Title #2", "body": "Hello, World 2!"}
# ]
# '''


# my_json = '''

# {
# 	"ivan":
# 		[
# 			{"title": "Title #1", "body": "Hello, World1!"},

# 			{"title": "Title #2", "body": "Hello, World 2!"}
# 		]
# }
# '''


# html = ''
# parsed_string = json.loads(my_json)
# for tag in parsed_string:	
# 	for key, value in tag.items():
# 		if key == 'title':
# 			html += '<h1>' + value + '</h1>'
# 		if key == 'body':
# 			html += '<p>' + value + '</p>'




# new = json.dumps(parsed_string, indent=10)
# print(new)





# with open('ivan.json') as file:
# 	my_kai = loads(file)


# with open("my_json", "w", encoding="utf-8") as file:
#     json.dump(my_json, file)


#22222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222


# my_json = '''
# 		[
# 			{
# 			 "h3": "Title #1",
# 			 "div": "Hello, World 1!"
# 			}

# 		]
# 		'''
# my_json = json.loads(my_json)

# html = ''
# for set_tag in my_json:
# 	for tag, value in set_tag.items():
# 		html += "<{0}>{1}</{0}>".format(tag, value)
# print(html)


#3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333


my_json = '''
		[
			{
			"h3": "Title #1",
			"div": "Hello, World 1!"
			},
			{
			"h3": "Title #2",
			"div": "Hello, World 2!"
			}
		]
		'''
html = ""
my_json = json.loads(my_json)
json_type = type(my_json)
print(len(my_json))
count = 0
if json_type == list:
	for set_tag in my_json:
		for tag, value in set_tag.items():
			html += "<li><{0}>{1}</{0}></li>".format(tag, value)
print(html)