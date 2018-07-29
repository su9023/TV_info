import urllib.request
from bs4 import BeautifulSoup
import re

#Get URL
html = urllib.request.urlopen("https://tv.so-net.ne.jp/?SmRcid=tv_ot_pix1207")

#html parser
soup = BeautifulSoup(html,"lxml")

#Get Line of "span class" tag
title_tag = str(soup.find_all("span",class_="schedule-title"))

#Remove tag(example <a></a>)
regular_expression = re.compile(r"<[^>]*?>") 
title = regular_expression.sub("",title_tag)

#Insert indention
#insert_indention_title = title.replace(',','\n')

#split
insert_indention_title = title.split(',')


#serch "movie"
for i in range(len(insert_indention_title)):
    #print (insert_indention_title[i])
    if "巨人" in insert_indention_title[i]:
        print (insert_indention_title[i])

#Remove "&lt;""&gt""&amp"
#remove_gabage_title = insert_indention_title.replace('&lt;','')
#remove_gabage_title = remove_gabage_title.replace('&gt;','')
#remove_gabage_title = remove_gabage_title.replace('&amp;',' ')

#print (remove_gabage_title)
