
"""
+------------------------------+------------------+----------+
| Description | Published Date | Victim's Website | Post URL |
+------------------------------+------------------+----------+
|      X      |                |        X         |     X    |
+------------------------------+------------------+----------+
Rappel : def appender(post_title, group_name, description="", website="", published="", post_url=""):
"""
import os
from bs4 import BeautifulSoup
from sharedutils import stdlog, errlog
from parse import appender
import re


def main():
    for filename in os.listdir('source'):
        try:
            if filename.startswith('abyss-'):
                html_doc='source/'+filename
                file=open(html_doc,'r')
                soup=BeautifulSoup(file,'html.parser')
                predata=soup.find('pre')
                predata = predata.text
                index1 = predata.find('[')
                index2 = predata.rfind(']')
                predata = predata[index1:index2+1]
                # print(predata)
                # # 去除文本中的多余空格和换行符
                predata = predata.strip()
                # print(predata)

                # # 去除文本中的特殊字符 '&lt;' 和 '&gt;'
                predata = predata.replace('&lt;', '<').replace('&gt;', '>').replace('<br>','')
                # print(predata)
                
                datas = predata.split('},\n{')
                for data in datas:
                    ptitle = r"'title' : '(.*)',"
                    title = re.search(ptitle,data).group(1)
                    description = data[data.find('full')+8:data.find("links")-30].replace('\'','').replace('+','').replace('/t            ','')
                    pdownload = re.findall(r"http(.*)",data)
                    downloads = []
                    for i in pdownload:
                        downloads.append("http"+i[:i.find('\"')])
                    appender(title, 'abyss', description,title,"","http://3ev4metjirohtdpshsqlkrqcmxq6zu3d7obrdhglpy5jpbr7whmlfgqd.onion/",download=downloads)

                # data = json.loads(predata)
                # print(data)
                # for div in divs_name:
                    # title = div.find('h5',{"class": "card-title"}).text.strip()
                    # description = div.find('p',{"class" : "card-text"}).text.strip()
                    # appender(title, 'abyss', description.replace('\n',''))
                file.close()
        except:
            errlog('blackbasta: ' + 'parsing fail')
            pass    
        