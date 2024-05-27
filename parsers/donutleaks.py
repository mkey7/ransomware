
"""
+------------------------------+------------------+----------+
| Description | Published Date | Victim's Website | Post URL |
+------------------------------+------------------+----------+
|      X      |                |          X       |          |
+------------------------------+------------------+----------+
Rappel : def appender(post_title, group_name, description="", website="", published="", post_url=""):
"""
import os
from bs4 import BeautifulSoup
from sharedutils import errlog, get_website
from parse import appender, existingpost
import re

# TODO 完成单独爬取网页
def get_post(url):
    print(url)
    page = get_website(url)
    print(page)
    



def main():
    group_name = 'donutleaks'

    for filename in os.listdir('source'):
        try:
            if filename.startswith('donutleaks-'):
                html_doc='source/'+filename
                file=open(html_doc,'r')
                soup=BeautifulSoup(file,'html.parser')
                # divs_name=soup.find_all('div', {"class": "box post-box"})
                
                if soup.title.text!='d#nut':
                    continue

                articles = soup.find_all("article")  

                # Regular expression pattern to extract the date in the desired format
                date_pattern = r"(\d{2}-\d{2}-\d{4})"

                # Extract article details
                for article in articles:
                    # Extract title
                    title = article.find("h2", class_="post-title").text.strip()
                    
                    if existingpost(title,group_name):
                        continue

                    # Extract date and convert it to the desired format
                    date_string = article.find("time").get("datetime")
                    date = re.search(date_pattern, date_string).group(0)
                    date_formatted = date[6:10] + "-" + date[3:5] + "-" + date[0:2] + " 00:00:00.00000"

                    # Extract URL
                    url = "http://sbc2zv2qnz5vubwtx3aobfpkeao6l4igjegm3xx7tk5suqhjkp5jxtqd.onion/" + article.find("a").get("href")

                    get_post(url)

                    # Extract description
                    description = article.find("p", class_="post-excerpt").text.strip()

                    # appender(title, 'donutleaks', description.replace('|','-'),'',date_formatted,'http://sbc2zv2qnz5vubwtx3aobfpkeao6l4igjegm3xx7tk5suqhjkp5jxtqd.onion'+url)
                file.close()
        except:
            errlog('donutleaks: ' + 'parsing fail')
            pass    
