from rabbitMQ import mq
import json
from sharedutils import openjson

def main():
    """
    初始化勒索攻击的爬取站点，插入到天眼的站点表中
    """
    groups = openjson("groups.json")
    
    mq1 = mq.MQ()
    # iterate each provider
    for group in groups:
        print(group)
        mq.group2site(group,mq1)
        print("successed push ",group['name'])
        
if __name__ == "__main__":
    main()
