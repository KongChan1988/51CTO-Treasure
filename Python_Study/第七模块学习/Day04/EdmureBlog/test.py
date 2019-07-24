__author__ = 'Administrator'
content="""
<p class='c1' id='i1'>
	asdfaa<span style="font-family:NSimSun;">sdf<a>a</a>sdf</span>sdf
</p>
<p>
	<strong class='c2' id='i2'>asdf</strong>
	<script>alert(123)</script>
</p>
<h2>
	asdf
</h2>
"""
tags = {
	'p': ['class'],
	'strong': ['id',]
}
from bs4 import BeautifulSoup
soup = BeautifulSoup(content, 'html.parser')

for tag in soup.find_all():
	if tag.name in tags:
		pass
	else:
		tag.hidden = True
		tag.clear()
		continue

	input_attrs = tag.attrs      # {'class': 'c1', 'id': 'i1'}
	valid_attrs = tags[tag.name] # ['class']
	for k in list(input_attrs.keys()):
		if k in valid_attrs:
			pass
		else:
			del tag.attrs[k]

content = soup.decode()
print(content)

# pip3 install beatifulsoup4
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(content, 'html.parser')
# tag = soup.find('script')
# tag.hidden = True
# tag.clear()
#
# span = soup.find('span')
# # print(span.attrs)
# del span.attrs['style']
#
# content = soup.decode()
# print(content)