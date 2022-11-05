import requests
import os
from bs4 import BeautifulSoup
import pandas as pd
import time
import datetime
from tqdm import tqdm

class vac_parser:
    
    def __init__(self, 
                 url: str, 
                 path: str, 
                 text: str):
        
        self.url = url
        self.path = path
        
        self.data = pd.DataFrame({
            'id':[],
            'name':[],
            'company':[],
            'industries':[],
            'city':[],
            'experience':[],
            'salary':[],
            'responses':[],
            'description':[],
            'key_skills':[],
            'url':[]
        })
        
        self.text = text
        
        self.par = {
            'text': self.text, 
            'area':'113',
            'per_page':'10', 
            'page':1, 
            'responses_count_enabled': True
        }
        
        self.vacancies_info = requests.get(self.url, params=self.par).json()

        self.num_pages = self.vacancies_info['pages']
        
        
    def check_num_pages(self):
        print('Количество страниц для парсинга:', self.num_pages)
        

    def vacancie_parser(self, j: dict):

        vacancie_info = {}

        vacancie_info['id'] = j['id']
        vacancie_info['name'] = j['name']
        vacancie_info['company'] = j['employer']['name']
        vacancie_info['city'] = j['area']['name']
        vacancie_info['experience'] = j['experience']['name']

        if j['salary'] is not None:

            salary = str()
            if ((j['salary']['from'] is not None) and (j['salary']['to']) is not None):
                salary = 'от ' + str(j['salary']['from'])
                salary += ' до ' + str(j['salary']['to'])
                salary += ' ' + str(j['salary']['currency'])

            elif ((j['salary']['from'] is not None) and (j['salary']['to']) is None):
                salary = 'от ' + str(j['salary']['from'])
                salary += ' ' + str(j['salary']['currency'])

            else:
                salary += 'до ' + str(j['salary']['to'])
                salary += ' ' + str(j['salary']['currency'])

            if j['salary']['gross'] is True:
                salary += ' до вычета'
            elif j['salary']['gross'] is False: 
                salary += ' на руки'
            else:
                pass

            vacancie_info['salary'] = salary
        else:
            vacancie_info['salary'] = j['salary']

        vacancie_info['description'] = j['description']

        s = []
        for i in j['key_skills']:
            s.append(i['name'])
        vacancie_info['key_skills'] = ', '.join(s)

        return vacancie_info
    
    def get_info_from_page(self, page: dict):

        for i, vacancie in enumerate(page['items']):

            vac_url = vacancie['url']
            emp_url = vacancie['employer']['url']
            
            vac_info = requests.get(vac_url).json()
            emp_info = requests.get(emp_url).json()

            vacancie_info = self.vacancie_parser(vac_info)
            try: 
                vacancie_info['industries'] = emp_info['industries'][0]['name']
            except:
                vacancie_info['industries'] = None
            vacancie_info['responses'] = vacancie['counters']['responses']
            vacancie_info['url'] = vacancie['alternate_url']

            self.data.loc[len(self.data)] = vacancie_info

        time.sleep(.1)
        
    def start_final_parse(self):
        
        for page_number in tqdm(range(0, self.num_pages)):

            parameters = {
                'text': self.text, 
                'area':'113',
                'per_page':'10', 
                'page': page_number, 
                'responses_count_enabled': True
            }

            hh_page = requests.get(self.url, params=parameters).json()

            self.get_info_from_page(hh_page)
            
    def save_file(self, name: str):
        
        self.data.to_csv(self.path + '/' + name + '.csv')
        
    def save_collection(self, name:str):
        
        df_collect = pd.read_csv(self.path + '/' + name + '.csv', index_col=0)

        if df_collect.loc[len(df_collect)-1, 'date'] != datetime.date.today():
            df_collect.loc[len(df_collect), 'date'] = datetime.date.today()
            df_collect.loc[len(df_collect)-1, 'vac_number'] = len(self.data)
        else:
            pass
        
        print('Информация о сегодня сохранена')
        display(df_collect.tail())
        self.data.to_csv(self.path + '/' + name + '.csv')