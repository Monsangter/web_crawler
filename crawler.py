import time
from selenium import webdriver
from bs4 import BeautifulSoup
import psycopg2
import requests


class WantedCrawler:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome()
        self.SCROLL_PAUSE_TIME = 0.5 # 너무 빠르면 에러.
        self.conn = psycopg2.connect(
            host="localhost",
            port="5432",
            dbname="crawling",
            user="postgres",
            password=""
        )
        self.cur = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS wanted (
                id SERIAL PRIMARY KEY,
                company VARCHAR(100),
                position VARCHAR(100),
                url TEXT,
                location VARCHAR(100),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UNIQUE (company, position)
            )
            '''
        )
        self.conn.commit()

    def scroll_down(self):
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(self.SCROLL_PAUSE_TIME)
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    def crawl(self):
        try:
            self.driver.get(self.url)
            self.scroll_down()
            soup = BeautifulSoup(self.driver.page_source, 'html.parser').select_one(('div.List_List_container__JnQMS'))
            jobs = soup.select('div.Card_className__u5rsb')
            data = []
            for job in jobs:
                company = job.select_one('.job-card-company-name').text.strip()
                position = job.select_one('.job-card-position').text.strip()
                url = 'https://www.wanted.co.kr' + job.find('a')['href']
                location = job.select_one('.job-card-company-location').text.strip()
                data.append((company, position, url, location))
            self.cur.executemany('''
            INSERT INTO wanted (company, position, url, location)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (company, position) DO NOTHING
            ''', data)
            self.conn.commit()

        except Exception as e:
            print(f"{e}1")
        
        finally:
            self.quit()


    def quit(self):
        self.driver.quit()
        self.cur.close()
        self.conn.close()


class JobKoreaCrawler:
    def __init__(self, url):
        self.url = url
        self.conn = psycopg2.connect(
            host="localhost",
            port="5432",
            dbname="crawling",
            user="postgres",
            password=""
        )
        self.cur = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS jobkorea (
                id SERIAL PRIMARY KEY,
                company VARCHAR(100),
                detail VARCHAR(100),
                url TEXT,
                exp VARCHAR(20),
                location VARCHAR(10),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UNIQUE (company, detail)
            )
            '''
        )
        self.conn.commit()

    def crawl(self):

        try:
            data = []
            for n in range(1, 4):
                soup = requests.get(self.url + f'&Page_No={str(n)}',
                                    headers={'User-Agent': 'Mozilla/5.0'})
                html = BeautifulSoup(soup.text, 'html.parser').select_one(("div.list-default"))
                jobs = html.select('li.list-post')
                page_data = []
                for job in jobs:
                    company = job.select_one('a.name').text.strip()
                    detail = job.select_one('a.title').text.strip()
                    url = 'https://www.jobkorea.co.kr' + job.find('a')['href']
                    exp = job.select_one('span.exp').text.strip()
                    location = job.select_one('span.loc').text.strip()
                    page_data.append((company, detail, url, exp, location))
                data.extend(page_data)

            self.cur.executemany('''
                INSERT INTO jobkorea (company, detail, url, exp, location)
                VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT (company, detail) DO NOTHING
                ''', data)
            self.conn.commit()
        except Exception as e:
            print(f"{e}2")

        finally:
            self.quit()

    def quit(self):
        self.cur.close()
        self.conn.close()

class SaraminCrawler:
    def __init__(self, url):
        self.url = url
        self.conn = psycopg2.connect(
            host="localhost",
            port="5432",
            dbname="crawling",
            user="postgres",
            password=""
        )
        self.cur = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS saramin (
                id SERIAL PRIMARY KEY,
                company VARCHAR(100),
                detail VARCHAR(100),
                url TEXT,
                exp VARCHAR(100),
                location VARCHAR(100),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UNIQUE (company, detail)
            )
            '''
        )
        self.conn.commit()

    def crawl(self):
        try:
            data = []
            for pageNum in range(1, 4):
                soup = requests.get(self.url + f'&recruitPage={str(pageNum)}&recruitSort=relation&recruitPageCount=20',
                                    headers={'User-Agent': 'Mozilla/5.0'})

                html = BeautifulSoup(soup.text, 'html.parser').select_one(("div.content"))

                jobs = html.select('div.item_recruit')

                page_data = []

                for job in jobs:
                    company = job.select_one('a.track_event.data_layer').text.strip()
                    detail = job.select_one('h2.job_tit').text.strip()
                    url = 'https://www.saramin.co.kr' + job.find('a')['href']
                    exp = job.select_one('span:nth-child(2)').text.strip()
                    location = job.select_one('span:nth-child(1)').text.strip()
                    page_data.append((company, detail, url, exp, location))

                data.extend(page_data)

            self.cur.executemany('''
                INSERT INTO saramin (company, detail, url, exp, location)
                VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT (company, detail) DO NOTHING
                ''', data)

            self.conn.commit()
        except Exception as e:
            print(f"{e}3")

        finally:    
            self.quit()

    def quit(self):
        self.cur.close()
        self.conn.close()
