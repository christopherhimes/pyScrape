import os
import time
import lxml.html as LH
import urllib2
import bs4
# page = requests.get('http://www.doorbuy.com/exterior-doors/decorative-glass-collections/brighton')
# tree = html.fromstring(page.content)
# buyers = tree.xpath('//div[@title="buyer-name"]/text()')
# prices = tree.xpath('//span[@class="item-price"]/text()')
# print 'Buyers: ', buyers
# import urllib




start_time = time.time()

os.chdir('svgs')

for filename in os.listdir(os.getcwd()):
  if filename != '.DS_Store':
    print(filename)
    elemfile = open(filename)
    inside = bs4.BeautifulSoup(elemfile.read(), "lxml")
    elems = inside.select('#Product_Image_Glass_Image')
    this_page = str(elems[0].get('xlink:href'))

    page = urllib2.urlopen('http://'+this_page[2:])
    page_content = page.read()
    this_file = '' + this_page[50:]
    print(this_file)
    print(os.getcwd())
    if page_content != '':
      os.chdir('../img')
      print(os.getcwd()+this_file)
      with open(this_file, 'wb') as fid:
        fid.write(page_content)
        page.close()
        os.chdir('../svgs')
    print(os.getcwd())
    # print(filename)
    # this_file = open(filename)
    # this_content = this_file.read()  
    # tree = LH.parse(filename)
    # root = tree.getroot()
    # table = root[0]
    # links = table.xpath("//image[contains(@href, 'doors')]")
    # print(links)
    # link = tree.xpath("descendant::image[contains(@href, 'doors')]")
    # print(link)
    # for td in tree.xpath("//image[@href]/@href"):
    #     print(td.text())
    # print(tree.iterlinks(etree))
    # image = tree.xpath('//image[@id="Product_Image_Glass_Image"]/text()')
    # print(image)
    # print(this_content)

    # this_file.close()

print("--- %s seconds ---" % (time.time() - start_time))