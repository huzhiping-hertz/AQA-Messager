import requests
from datetime import datetime
import pytz
import json
import hashlib

class WebApi:

    def __init__(self):
        self.url = "http://127.0.0.1:9090/api/v1/query?"
        self.timezone = pytz.timezone('Asia/ShangHai') 
        tm = datetime.now(self.timezone)
        tmstr=tm.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
        
    def pack_data(self,dictObj,data_type,dt):
        
        for elm in dt.json()["data"]["result"]:
            
            obj={}
            obj["src"]=elm["metric"]["source_name"]
            obj["dst"]=elm["metric"]["destination_name"]
            obj[data_type]=elm["value"][1]
            key=elm["metric"]["source_name"]+"To"+elm["metric"]["destination_name"]
            if key in dictObj:
                dictObj[key][data_type]=elm["value"][1]
            else:
                dictObj[key]=obj
    
    def getLostPacket(self):
        
        
        dictObj={}
        
        avg="query=avg_over_time(aqa_rtcp_packets_lost[5m])"
        avg_url=self.url+avg
        rsq=requests.request(method="Get",url=avg_url)
        rs=self.pack_data(dictObj,"avg",rsq)
        
        avg="query=max_over_time(aqa_rtcp_packets_lost[5m])"
        avg_url=self.url+avg
        rsq=requests.request(method="Get",url=avg_url)
        rs=self.pack_data(dictObj,"max",rsq)
        
        avg="query=min_over_time(aqa_rtcp_packets_lost[5m])"
        avg_url=self.url+avg
        rsq=requests.request(method="Get",url=avg_url)
        rs=self.pack_data(dictObj,"min",rsq)
        
        Objs={"type":"packet_lost"}
        Objs["data"]=dictObj
        rs=json.dumps(Objs)
        print(rs)
        return rs

       
        
    def getDelay(self):
        dictObj={}
        avg="query=avg_over_time(aqa_rtcp_dlsr[5m])"
        avg_url=self.url+avg
        rsq=requests.request(method="Get",url=avg_url)
        rs=self.pack_data(dictObj,"avg",rsq)
      
        avg="query=max_over_time(aqa_rtcp_dlsr[5m])"
        avg_url=self.url+avg
        rsq=requests.request(method="Get",url=avg_url)
        rs=self.pack_data(dictObj,"max",rsq)  
        
        avg="query=min_over_time(aqa_rtcp_dlsr[5m])"
        avg_url=self.url+avg
        rsq=requests.request(method="Get",url=avg_url)
        rs=self.pack_data(dictObj,"min",rsq)
        
        Objs={"type":"delay"}
        Objs["data"]=dictObj
        rs=json.dumps(Objs)
        print(rs)
        return rs
    
    
    def getJitter(self):
        
        dictObj={}
         
        avg="query=avg_over_time(aqa_rtcp_jitter[5m])"
        avg_url=self.url+avg
        rsq=requests.request(method="Get",url=avg_url)
        rs=self.pack_data(dictObj,"avg",rsq)
        
        avg="query=max_over_time(aqa_rtcp_jitter[5m])"
        avg_url=self.url+avg
        rsq=requests.request(method="Get",url=avg_url)
        rs=self.pack_data(dictObj,"max",rsq)
        
        avg="query=min_over_time(aqa_rtcp_jitter[5m])"
        avg_url=self.url+avg
        rsq=requests.request(method="Get",url=avg_url)
        rs=self.pack_data(dictObj,"min",rsq)
        
        Objs={"type":"jitter"}
        Objs["data"]=dictObj
        rs=json.dumps(Objs)
        print(rs)
        return rs
