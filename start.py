import json
import re


def edit_list(file):
	"""
	Если наш json содержит тип list
	то мы оборачиваем эти элименты в
	в ul, а конкретный каждый элемент
	в тег  il
	"""
	html = '<ul>'
	for set_tag in file:
		html += '<li>'
		for tag, value in set_tag.items():
			tag_with_attr, tag_out_attr = check_tag(tag)
			if type(value) == list: 
				value = edit_list(value)
			html += input_in_format(tag_with_attr, value, tag_out_attr)
		html += '</li>'
	html += '</ul>'
	return html


def edit_just(file):
	html = ''
	for tag, value in file.items():
		tag_with_attr, tag_out_attr = check_tag(tag)
		html += input_in_format(tag_with_attr, value, tag_out_attr)
	return html


def input_in_format(tag_with_atr, value, tag):
	tags = "<{}>{}</{}>".format(tag_with_atr, value, tag)
	return tags



def check_tag(key):
	""" 
	Сдесь идет проверка тегов. Если у них присуствует 
	специальные атрибуты в силе ссs то эта функция 
	привидет атрибуты к стилю html 
	"""
	tag = ''
	clear_tag = ''
	if '#' in key and '.' in key:
		tag += key.split('.')[0]
		clear_tag = tag
		tag_class = re.findall(r'\.([^#]+)|#([^.]+)', key)[0][0]
		tag_id = re.findall(r'\.([^#]+)|#([^.]+)', key)[1][1]
		if '.' in tag_class:
			tag_class = tag_class.replace('.', ' ')
		tag_class = ' class="{}"'.format(tag_class)
		tag += tag_class + ' id="%s"' % tag_id
	elif '.' in key:
		tag += key.split('.')[0]
		clear_tag = tag
		tag_class = re.findall(r'\.([^#]+)', key)[0]
		tag_class = tag_class.replace('.', ' ')
		tag_class = ' class="{}"'.format(tag_class)
		tag += tag_class 
	elif '#' in key:
		try:
			tag += key.split('#')[0]
			clear_tag = tag
			tag_id = re.findall(r'#([^.]+)', key)[0]
			if '#' in tag_id:
				raise KeyError
			tag += ' id="%s"' % tag_id
		except KeyError as e:
			print('Ошибка с id, не может быть 2 id у одного тега: %s' % key)
			return 'Error with attr of tag'
		else:
			pass
		finally:
			pass
	else:
		tag = key
		clear_tag = key		
	return [tag, clear_tag]


def main(file):
	"""
	Функция контроля
	"""
	if type(file) == list:
		html = edit_list(file)
	else:
		html = edit_just(file)
	print(html)	
	with open('myhtml.html', 'w', encoding='utf-8') as file:
		file.write(html)



if __name__ == '__main__':
	with open('source.json') as f:
		file = json.load(f)
		main(file)


