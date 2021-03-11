from model.proxyModel import ProxyModel
import urllib.request
import socket
import urllib.error
import requests
from proxy_checker import ProxyChecker as PCh

class ProxyChecker:
    def __init__(self, proxies: list) -> None:        
        self.proxies=proxies              

    def check(self):
        checked_proxies=list()
        socket.setdefaulttimeout(10)               
        count = 0
        for index, currentProxy in enumerate(self.proxies):
            print(f"checking: {self.proxies[index]}")
            _ = currentProxy.get("proxy").split("://")
            proxy = _[1]
            uri = _[0]
            if not ProxyChecker.is_bad_proxy(uri, proxy) and count < 1500:                
                print(f"worked proxy: {proxy}")
                checked_proxies.append(self.proxies[index])
                try:
                    ProxyModel("proxy_checked").insert([self.proxies[index]])
                    count += 1
                    ProxyModel("proxy_pool_bk").insert([self.proxies[index]]) 
                except Exception as e:
                    print(e)
                    print(self.proxies[index])
        return checked_proxies

            
    @staticmethod
    def is_bad_proxy(uri, proxy):
        url = "http://forum.gamer.com.tw/ajax/rank.php?c=21&page=1"
        ip = proxy.split(':')[0]
        port = proxy.split(':')[-1]
        proxies = {"{}".format(uri): f"http://{ip}:{port}"}
        
        headers = {"User-Agent": "Mozilla/5.0"}
        try:
            res = requests.get(url, proxies=proxies, headers=headers, timeout=2)
            if res.status_code == 200:
                print(proxy + "  works!")
                return False
            else:
                print(proxy + " not working")
                return True
        except Exception as e:
            print(proxy + " Not Working :( => " + str(e))
            return True
        # checker = PCh()

        # ip = proxy.split(':')[0]
        # port = proxy.split(':')[-1]
        # c = checker.check_proxy('{}:{}'.format(ip, port))
        # if c and c["timeout"] < 500:
        #     print(c)
        #     return False
        # else:
        #     return True
        # try:
        #     proxy_handler = urllib.request.ProxyHandler({uri: proxy})
        #     opener = urllib.request.build_opener(proxy_handler)
        #     opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        #     urllib.request.install_opener(opener)
        #     req=urllib.request.Request('https://www.google.com')
        #     req1=urllib.request.Request('https://www.facebook.com')
        #     req2=urllib.request.Request('https://script.google.com/macros/s/AKfycby9S1Vx3ipI0DhQvZU5hJXOLyFpKErT9NPZwIUEI0RgssJVyV8/exec')
        #     sock=urllib.request.urlopen(req)
        #     sock=urllib.request.urlopen(req1)
        #     sock=urllib.request.urlopen(req2)
        # except urllib.error.HTTPError as e:
        #     print('Error code: ', e.code)
        #     return e.code
        # except Exception as detail:
        #     print("ERROR:", detail)
        #     return True
        # return False


if __name__ == "__main__":
    pm = ProxyModel("proxy_pool")   
    data =list(pm.get_all_data())    
    pc = ProxyModel("proxy_checked")
    data1=list(pc.get_all_data())   
    pc.drop_collection()    
    data = data + data1   
    print(data)
    checked_list = ProxyChecker(proxies=data).check()   
    pm.drop_collection()


