
"""
+------------------------------+------------------+----------+
| Description | Published Date | Victim's Website | Post URL |
+------------------------------+------------------+----------+
|      X      |                |                  |     X    |
+------------------------------+------------------+----------+
"""

import os, hashlib
from bs4 import BeautifulSoup
from sharedutils import errlog, find_slug_by_md5, extract_md5_from_filename,get_website
from parse import appender

def get_description(post,title,published):
    page = get_website(post)
    print("------")

    hash_object = hashlib.md5()
    hash_object.update(post.encode('utf-8'))
    hex_digest = hash_object.hexdigest()
    filename = 'bianlian-' + hex_digest + '.html'
    name = os.path.join(os.getcwd(), 'source', filename)
    print(name)
    with open(name, 'w', encoding='utf-8') as sitesource:
        sitesource.write(page)
        sitesource.close()
    print("===========")
    
    # todo 提取相关字段
    soup=BeautifulSoup(page,'html.parser')
    post_title = soup.title.string
    print(post_title)

    post_url = post    

    body = soup.section
    if body.p.find('a'):
        website = body.p.a['href']
        description =  body.contents[1].string
    else:
        website = ''
        description =  body.contents[0].string
    print(website)
    print(description)

        # "screenshot_path": "",
        # "price": "",
        # "pay": "",
        # "email": "",
        # "download": "" """




def main():
    url = "http://bianlivemqbawcco4cx4a672k2fip3guyxudzurfqvdszafam3ofqgqd.onion"
    for filename in os.listdir('source'):
        try:
            if filename.startswith('bianlian-'):
                html_doc='source/'+filename
                file=open(html_doc,'r')
                soup=BeautifulSoup(file,'html.parser')
                if soup.title.string != "Companies - BianLian":
                    continue
                divs_name=soup.select('li')
                for div in divs_name:
                    post = url+div.a['href']
                    title = div.a.string
                    published = div.span.string
                    
                    print(post)
                    print(title)
                    print(published)
                    get_description(post,title,published)
                    #     url = "bianlianlbc5an4kgnay3opdemgcryg2kpfcbgczopmm3dnbz3uaunad.onion" + str(post)
                    # description = div.div.text.strip()
                    # description = description.replace('%20',' ')
                    # appender(title, 'bianlian', description,"","",url)
                file.close()
        except:
            errlog("Failed during : " + filename)
