# ransomwaree

## 数据逻辑

### groups.json

```
    {
        "name": "trisec_cyberoutlaw",
        "captcha": false,
        "parser": false,
        "javascript_render": false,
        "meta": null,
        "locations": [
            {
                "fqdn": "pkk4gbz7lsbgeja6s6iwsan2ce364sqioici65swwt65uhicke65uyid.onion",
                "title": "Index of /",
                "version": 3,
                "slug": "http://pkk4gbz7lsbgeja6s6iwsan2ce364sqioici65swwt65uhicke65uyid.onion",
                "available": false,
                "updated": "2024-03-18 00:51:06.322647",
                "lastscrape": "2024-03-18 00:51:06.322587",
                "enabled": true
            },
            {
                "fqdn": "orfc3joknhrzscdbuxajypgrvlcawtuagbj7f44ugbosuvavg3dc3zid.onion",
                "title": "Index of /",
                "version": 3,
                "slug": "http://orfc3joknhrzscdbuxajypgrvlcawtuagbj7f44ugbosuvavg3dc3zid.onion",
                "available": false,
                "updated": "2024-03-18 00:51:42.866920",
                "lastscrape": "2024-03-18 00:51:42.866527",
                "enabled": true
            }
        ],
        "profile": []
    },
```

- name：勒索组织名称
- captcha：
- parser：勒索组织网页解析情况
- javascript_render：勒索组织网站触发js加载
- meta
- profile：勒索组织其他信息
- locations：勒索组织网站（包含多个网站）
    - fqdn：域名
    - title：网页标题
    - version：tor版本
    - slug：爬取勒索攻击的网址
    - available：勒索攻击网址情况
    - updated：更新情况
    - lastscrape：最后爬取时间
    - enabled：勒索网站状态

### posts.json

```
    {
        "post_title": "Rotorcraft Leasing Company",
        "group_name": "0mega",
        "discovered": "2024-05-30 16:31:11.589947",
        "description": "Helicopter support, pilot training, fueling service, maintenance",
        "website": "",
        "published": "2024-01-17 00:00:00.000000",
        "post_url": "http://omegalock5zxwbhswbisc42o2q2i54vdulyvtqqbudqousisjgc7j7yd.onion/post/5.html",
        "country": "",
        "screenshot_path": "docs/screenshots/posts/ba398a6a8a5953ba54fdadb0ede60637.png",
        "price": "",
        "pay": "",
        "email": "",
        "download": [
            "http://omegalock5zxwbhswbisc42o2q2i54vdulyvtqqbudqousisjgc7j7yd.onion/downloads/5/RLCLLC/"
        ]
    },
```

- post_title：网站公布的标题
- group_name：发动勒索攻击的组织
- discovered：发现时间
- description：勒索组织对攻击的描述
- website：受害者的网站
- published：勒索攻击发布时间
- post_url：勒索攻击发布网页
- country：受害者国家
- screenshot：勒索攻击发布网页截图路径
- price：勒索金额
- pay：支付价格
- email：勒索组织联系方式
- download：提供的下载数据

### source
`source`文件夹保存爬取下来的html网页
文件名格式：`勒索组织名称-md5(url).html`

### docs/screenshots/posts
`docs/screenshots/posts`文件夹保存爬取下来的html网页
文件名格式：`md5(url).png`
