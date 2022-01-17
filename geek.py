# coding:utf-8

import requests
import re
import os


if not os.path.exists('./geeklibs'):
    os.mkdir('./geeklibs')

url = 'http://212.129.245.115:8080/static/js/app.7149a871ab46e4d1cdd7.js'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.62"
}

response = requests.get(url=url, headers=headers)
page_text = response.text

ex = "._v[\(](.*?)[\)]"
char_list = re.findall(ex, page_text, re.S)
while '" "' in char_list:
    char_list.remove('" "')
for char in char_list:
    char.strip('"')
    filename = 'char.txt'
    with open(filename, "a", encoding="utf-8") as fp:
        fp.write(char + '\n')
print('char are all over!!!')


pic = 'src:(.*?)}'
pic_list = re.findall(pic, page_text, re.S)
for img in pic_list:
    img = img.strip('"')
    if ',alt:' in img:
        img = img.rstrip(',alt:"')
    img_data = requests.get(url=img, headers=headers).content
    img_name = img.split('/')[-1]
    imgPath = './geeklibs/' + img_name
    with open(imgPath, 'wb') as fp:
        fp.write(img_data)
print("pictures are all over!!!")