import pika
from rabbitMQ.common_pb2 import OtherIndex
import hashlib
import json

def pack_pb(index, data, m_id):
    pb = OtherIndex()
    pb.index = index
    pb.data = data.encode('ascii')
    pb.mid = m_id

    res = pb.SerializeToString()
    return res

def sha256_encode(code: str):
    s = hashlib.sha256()
    s.update(code.encode())
    res = s.hexdigest()
    return res


def group2site(post,MQ):
    if type(post) == str:
        post = json.loads(post)
    site = {}
    site['isFirstView'] = True
    site['title'] = post['name']
    # site['description'] = post['description']
    site['language'] = 'en'
    site['tag'] = '勒索软件'
    site['type'] = 'tor'
    site['priority'] = 2
    # site['firstSeen'] = True
    for u in post['locations']:
        if not u['available']:
            continue
        site['lastSeen'] = u['lastscrape']
        site['url'] = u['slug']
        site['urlSha256'] = sha256_encode(u['slug'])
        
        
        # TODO 发送mq
        print(site)
        
        MQ.send_site(json.dumps(site),site['urlSha256'])

    # site['screenshot'] = True
    # site['logo_path'] = True
    


class MQ:
    def __init__(self, default_username, default_password, **kwargs):
        credentials = pika.credentials.PlainCredentials(
            default_username, default_password)

        connection = pika.BlockingConnection(pika.ConnectionParameters(credentials=credentials,heartbeat=0, **kwargs))
        self.client = connection.channel()
        self.topic = {}

        print("mq init successed")

        
    def producer(self, topic: str, msg: bytes):
        if topic not in self.topic.keys():
            self.client.exchange_declare(exchange=topic, exchange_type="topic", durable=True)
            self.topic[topic] = ""
        self.client.basic_publish(
            exchange=topic,
            routing_key="",
            body=msg,
            mandatory=True,
            properties=pika.BasicProperties(
                delivery_mode=2,  # make message persistent
            )
        ) 

    def send_site(self,data,urlSha256,exchange="zeronet_other"):

#PS：这里不同种队列不允许名字相同
        self.producer(exchange, pack_pb('deep_site_v3', data,urlSha256 ))
        
        print('push sucessed!')


