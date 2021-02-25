# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class Stockscraper2Pipeline:
    def __init__(self):
        self.setupDBConnect() # DB 연결 설정 
        self.createTable() # 테이블 생성

    def process_item(self, item, spider):
        self.storeInDb(item)
        print("DB Stored")
        # print(item)

    def setupDBConnect(self):
        self.conn = pymysql.connect(host = '127.0.0.1', user = 'root', password = '', db = 'mystockdb', charset = 'utf8')
        self.cur = self.conn.cursor()
        print("DB Connected")

    def createTable(self):
        self.cur.execute("DROP TABLE IF EXISTS stock_table") # 테이블이 이미 존재할 경우 삭제
        
        self.cur.execute('''
        CREATE TABLE IF NOT EXISTS stock_table(
            id INT AUTO_INCREMENT PRIMARY KEY,
            read_time VARCHAR(100),
            stock_volume VARCHAR(100),
            now_price VARCHAR(100),
            max_price VARCHAR(100),
            min_price VARCHAR(100),
            stock_code VARCHAR(100)
        )''')

    def storeInDb(self, item):
        read_time = item.get('read_time', '').strip()
        stock_volume = item.get('stock_volume', '').strip()
        now_price = item.get('now_price', '').strip()
        max_price = item.get('max_price', '').strip()
        min_price = item.get('min_price', '').strip()
        stock_code = item.get('stock_code', '').strip()

        sql = "INSERT INTO stock_table(id, read_time, stock_volume, now_price, max_price, min_price, stock_code) VALUES(null,%s,%s,%s,%s,%s,%s)"

        self.cur.execute(sql, (read_time, stock_volume, now_price, max_price, min_price, stock_code))
        self.conn.commit()
