# Modovision private proxy pool
- [x] mongodb
- [x] mongo express (GUI)
- [x] [scylla](https://github.com/imWildCat/scylla)
- [x] automatically check the ips in proxy pool (located in mongo)
- [x] use ip+port to be the value of _id, so no repeat proxy
- [x] visualized the process of automation (e.g. airflow ..etc)

# Usage scylla:
scylla is an open source api from [here](https://github.com/imWildCat/scylla) 

## Python: method 1
```python
class MongoProxies(object):
    def __init__(self, collection) -> None:
        connection = pymongo.MongoClient(
            host=MONGODB_HOST,
            port=MONGODB_PORT,
            username=MONGODB_USERNAME,
            password=MONGODB_PASSWORD
        )
        self.__collection=collection
        self.db=connection[MONGODB_DB]
        self.collection=self.db[collection]

    def get_all_proxies(self):
        return [f.get("proxy") for f in self.collection.find({})]
```
### Then get the schema of the respond list object as follow:
```python
MongoProxies("proxy_checked").get_all_proxies()
```

## Python: method 2
```python
import requests
res_json = reqests.get("http://IP:8899/api/v1/proxies").json()

print(res_json)
```
### Then the schema of the respond json object is as follow:
```json
{
    "proxies":[
        {
            "id":206,
            "ip":"116.58.237.87",
            "port":8080,
            "is_valid":true,
            "created_at":1608271848,
            "updated_at":1608272458,
            "latency":117.0,
            "stability":1.0,
            "is_anonymous":false,
            "is_https":false,
            "attempts":1,
            "https_attempts":0,
            "location":"24.9889,121.3176","organization":"HiNet",
            "region":"Taoyuan",
            "country":"TW",
            "city":"Taoyuan District"
        },
        {
            .........
        }    
    ],
    "count": counts of proxies,
    "per_page": per page number of proxies,
    "page": now page,
    "total_page": total page
}
```
to get more api information please check [here](https://github.com/imWildCat/scylla)
