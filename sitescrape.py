# from lxml import html
# import requests
# page = requests.get('http://www.doorbuy.com/exterior-doors/decorative-glass-collections/brighton')
# tree = html.fromstring(page.content)
# buyers = tree.xpath('//div[@title="buyer-name"]/text()')
# prices = tree.xpath('//span[@class="item-price"]/text()')
# print 'Buyers: ', buyers
# import urllib
import urllib2
import time
import bs4
import re

std_page = 'http://www.doorbuy.com/assets/MASTER.php?thumbnail=1&id='

start_time = time.time()

for x in range(200, 220):
  this_page = std_page + str(x)
  this_file = 'svgs/' + str(x) + '.svg'

  # urllib.urlretrieve(this_page, this_file)
  page = urllib2.urlopen(this_page)
  page_content = page.read()

  inside = bs4.BeautifulSoup(page_content, "lxml")

  # print(inside)

  file_id = inside.find_all(id=re.compile('Product_x'))
  image_id = inside.find_all(id=re.compile('Product_Image_Glass_Image'))
  print(type(inside.string))
  print(inside.find_all(href=re.compile('//s3')))
  # .replace_with('http://s3')
  # print(image_id)
  image_name = image_id[0]['xlink:href']
 
  alt_img = image_name  

  image_name = image_name[image_name.rfind('/')+1:]
  image_name = image_name[:len(image_name)-4]

  this_file = 'svgs/' + str(file_id[0]['id']) + '-' + image_name + '.svg'
  # this_page = str(elems[0].get('xlink:href'))

  # image_id.g.replace_with('HELLO')

  # print(page_content)
  if page_content != '':
    with open(this_file, 'wb') as fid:
      fid.write(page_content)

    page.close()

print("--- %s seconds ---" % (time.time() - start_time))