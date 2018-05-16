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
# my_json = [{"ivan": [{"first": "1"},{"second": '2'}]}]

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


# with open("my_json.json", "w", encoding="utf-8") as file:
#     json.dump(my_json, file, indent=4)


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


# my_json = '''
# 		[
# 			{
# 			"h3": "Title #1",
# 			"div": "Hello, World 1!"
# 			},
# 			{
# 			"h3": "Title #2",
# 			"div": "Hello, World 2!"
# 			}
# 		]
# 		'''
# html = ""
# my_json = json.loads(my_json)
# json_type = type(my_json)
# if json_type == list:
# 	html += '<ul>'
# 	for set_tag in my_json:
# 		html += '<li>'
# 		for tag, value in set_tag.items():
# 			html += "<{0}>{1}</{0}>".format(tag, value)
# 		html += '</li>'
# 	html += '</ul>'
# print(html)

#44444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
# my_json = '''
# 			[
# 				{
# 				"span": "Title #1",
# 				"content": [{
# 							"p": "Example 1", 
# 							"header": "header 1" 
# 							}]
# 				},
# 				{"div": "div 1"}

# 			]		
# 		  '''


# html = ""
# my_json = json.loads(my_json)
# json_type = type(my_json)
# if json_type == list:
# 	html += '<ul>'
# 	for set_tag in my_json:
# 		html += '<li>'
# 		for tag, value in set_tag.items():
# 			if type(value) == list: 
# 				new_val = '<ul>'
# 				for set_tag_2 in value:
# 					new_val += '<li>'
# 					for ke, val in set_tag_2.items():
# 						new_val += "<{0}>{1}</{0}>".format(ke, val)
# 					new_val += '</li>'
# 				new_val += '</ul>'
# 				value = new_val
# 			html += "<{0}>{1}</{0}>".format(tag, value)
# 		html += '</li>'
# 	html += '</ul>'



# print(html)







# class IvanJson:
# 	def __init__(self, file):
# 		with open(file) as file:
# 			self.myjson = json.load(file)


# 	def convert(self):





# 	def __str__(self):
# 		return self.myjson




# first = IvanJson('source.json')
# print(first)



# my_json = '''
# 			{
# 				"p.my-class#my-id": "hello",
# 				"p.my-class1.my-class2":"example<a>asd</a>"
# 			}
# 		  '''




 

def first_lvl(file):
	html = '<ul>'
	for set_tag in file:
		html += '<li>'
		for tag, value in set_tag.items():
			print(tag)
			if type(value) == list: 
				value = second_lvl(value)
			html += input_in_format(tag, value)
		html += '</li>'
	html += '</ul>'
	return html


def second_lvl(value):
	new_val = '<ul>'
	for set_tag_2 in value:
		new_val += '<li>'
		for ke, val in set_tag_2.items():
			new_val += input_in_format(ke, val)
		new_val += '</li>'
	new_val += '</ul>'
	return new_val





def input_in_format(key, value):
	tags = "<{0}>{1}</{0}>".format(key, value)
	return tags


def my_reg(some):
	pass






def main(file):
	if type(file) == list:
		html = first_lvl(file)
		print(html)
	else:
		print()
	with open('myhtml.html', 'w', encoding='utf-8') as file:
		file.write(html)


if __name__ == '__main__':
	with open('source.json') as f:
		file = json.load(f)
		main(file)




