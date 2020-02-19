from random import choice
from datetime import datetime
import json
import requests
from bs4 import BeautifulSoup as bs
import pymysql
import pymysql.cursors

USER_AGENTS = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36']

class InstagramScraper:
    def __init__(self,url,user_agents=None):
        self.url=url
        self.user_agents=user_agents
    
    def __random_agent(self):
        if self.user_agents and isinstance(self.user_agents,list):
            return choice(self.user_agents)
        return choice(USER_AGENTS)
    
    def __requests_url(self):
        try:
            response=requests.get(self.url,headers={'User-Agent':self.__random_agent()})
            response.raise_for_status()
        except requests.HTTPError:
            raise requests.HTTPError("Received non-200 status code.")
        except requests.RequestException:
            raise requests.RequestException
        else:
            return response.text
    @staticmethod
    def extract_json(html):
        soup = bs(html,'html.parser')
        body = soup.find('body')
        script_tag = body.find('script')
        raw_string = script_tag.text.strip().replace('window._sharedData =','').replace(';','')
        return json.loads(raw_string)
    
    def page_metrics(self):
        results = {}
        try:
            response = self.__requests_url()
            json_data = self.extract_json(response)
            metrics = json_data['entry_data']['ProfilePage'][0]['graphql']['user']
        except Exception as e:
            raise e
        else:
            for key,value in metrics.items():
                if key != 'edge_owner_to_timeline_media':
                    if value and isinstance(value,dict):
                        value = value['count']
                        results[key]=value
        return results
    def post_metrics(self):
        results = []
        try:
            response = self.__requests_url()
            json_data = self.extract_json(response)
            metrics = json_data['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges']
        except Exception as e:
            raise e 
        else:
            for node in metrics:
                node = node.get('node')
                if node and isinstance(node,dict):
                    results.append(node)
        return results


url = 'https://www.instagram.com/cristiano/'

instagram = InstagramScraper(url)
post_metrics = instagram.post_metrics()
print(post_metrics)