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
                
    def pack_single_data(self,obj,data_type,dt):
        if len(dt.json()["data"]["result"]) > 0:
            elm=dt.json()["data"]["result"][0]
            #obj["src"]=elm["metric"]["source_name"]
            #obj["dst"]=elm["metric"]["destination_name"]
            obj[data_type]=elm["value"][1]
            
    
    def getLostPacket(self,src,dst):
        
        rsObj={"src":src,"dst":dst,"avg":"null","max":"null","min":"null"}
        
        avg="query=avg_over_time(aqa_rtcp_packets_lost{source_name='"+src+"',destination_name='"+dst+"'}[30s])"
        avg_url=self.url+avg
        rsq=requests.request(method="Get",url=avg_url)
        rs=self.pack_single_data(rsObj,"avg",rsq)
        
        avg="query=max_over_time(aqa_rtcp_packets_lost{source_name='"+src+"',destination_name='"+dst+"'}[30s])"
        avg_url=self.url+avg
        rsq=requests.request(method="Get",url=avg_url)
        rs=self.pack_single_data(rsObj,"max",rsq)
        
        avg="query=min_over_time(aqa_rtcp_packets_lost{source_name='"+src+"',destination_name='"+dst+"'}[30s])"
        avg_url=self.url+avg
        rsq=requests.request(method="Get",url=avg_url)
        rs=self.pack_single_data(rsObj,"min",rsq)
        
        return rsObj
        #Objs={"type":"packet_lost","data":[]}
        
        # Objs["data"].append(rsObj)
        # rs=json.dumps(Objs)
        # print(rs)
        # return rs

       
        
    def getDelay(self,src,dst):
        rsObj={"src":src,"dst":dst,"avg":"null","max":"null","min":"null"}
        avg="query=avg_over_time(aqa_rtcp_dlsr{source_name='"+src+"',destination_name='"+dst+"'}[30s])"
        avg_url=self.url+avg
        rsq=requests.request(method="Get",url=avg_url)
        rs=self.pack_single_data(rsObj,"avg",rsq)
      
        avg="query=max_over_time(aqa_rtcp_dlsr{source_name='"+src+"',destination_name='"+dst+"'}[30s])"
        avg_url=self.url+avg
        rsq=requests.request(method="Get",url=avg_url)
        rs=self.pack_single_data(rsObj,"max",rsq)  
        
        avg="query=min_over_time(aqa_rtcp_dlsr{source_name='"+src+"',destination_name='"+dst+"'}[30s])"
        avg_url=self.url+avg
        rsq=requests.request(method="Get",url=avg_url)
        rs=self.pack_single_data(rsObj,"min",rsq)
        
        return rsObj
    
    
    def getJitter(self,src,dst):
        
        rsObj={"src":src,"dst":dst,"avg":"null","max":"null","min":"null"}
         
        avg="query=avg_over_time(aqa_rtcp_jitter{source_name='"+src+"',destination_name='"+dst+"'}[30s])"
        avg_url=self.url+avg
        rsq=requests.request(method="Get",url=avg_url)
        rs=self.pack_single_data(rsObj,"avg",rsq)
        
        avg="query=max_over_time(aqa_rtcp_jitter{source_name='"+src+"',destination_name='"+dst+"'}[30s])"
        avg_url=self.url+avg
        rsq=requests.request(method="Get",url=avg_url)
        rs=self.pack_single_data(rsObj,"max",rsq)
        
        avg="query=min_over_time(aqa_rtcp_jitter{source_name='"+src+"',destination_name='"+dst+"'}[30s])"
        avg_url=self.url+avg
        rsq=requests.request(method="Get",url=avg_url)
        rs=self.pack_single_data(rsObj,"min",rsq)
        
        return rsObj

    def getAllLostPacket(self):
        
        
        dictObj={}
        
        avg="query=avg_over_time(aqa_rtcp_packets_lost[30s])"
        avg_url=self.url+avg
        rsq=requests.request(method="Get",url=avg_url)
        rs=self.pack_data(dictObj,"avg",rsq)
        
        avg="query=max_over_time(aqa_rtcp_packets_lost[30s])"
        avg_url=self.url+avg
        rsq=requests.request(method="Get",url=avg_url)
        rs=self.pack_data(dictObj,"max",rsq)
        
        avg="query=min_over_time(aqa_rtcp_packets_lost[30s])"
        avg_url=self.url+avg
        rsq=requests.request(method="Get",url=avg_url)
        rs=self.pack_data(dictObj,"min",rsq)
        
        Objs={"type":"packet_lost"}
        Objs["data"]=dictObj
        rs=json.dumps(Objs)
        print(rs)
        return rs

       
        
    def getAllDelay(self):
        dictObj={}
        avg="query=avg_over_time(aqa_rtcp_dlsr[30s])"
        avg_url=self.url+avg
        rsq=requests.request(method="Get",url=avg_url)
        rs=self.pack_data(dictObj,"avg",rsq)
      
        avg="query=max_over_time(aqa_rtcp_dlsr[30s])"
        avg_url=self.url+avg
        rsq=requests.request(method="Get",url=avg_url)
        rs=self.pack_data(dictObj,"max",rsq)  
        
        avg="query=min_over_time(aqa_rtcp_dlsr[30s])"
        avg_url=self.url+avg
        rsq=requests.request(method="Get",url=avg_url)
        rs=self.pack_data(dictObj,"min",rsq)
        
        Objs={"type":"delay"}
        Objs["data"]=dictObj
        rs=json.dumps(Objs)
        print(rs)
        return rs
    
    
    def getAllJitter(self):
        
        dictObj={}
         
        avg="query=avg_over_time(aqa_rtcp_jitter[30s])"
        avg_url=self.url+avg
        rsq=requests.request(method="Get",url=avg_url)
        rs=self.pack_data(dictObj,"avg",rsq)
        
        avg="query=max_over_time(aqa_rtcp_jitter[30s])"
        avg_url=self.url+avg
        rsq=requests.request(method="Get",url=avg_url)
        rs=self.pack_data(dictObj,"max",rsq)
        
        avg="query=min_over_time(aqa_rtcp_jitter[30s])"
        avg_url=self.url+avg
        rsq=requests.request(method="Get",url=avg_url)
        rs=self.pack_data(dictObj,"min",rsq)
        
        Objs={"type":"jitter"}
        Objs["data"]=dictObj
        rs=json.dumps(Objs)
        print(rs)
        return rs
