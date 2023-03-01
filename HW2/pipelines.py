# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class Hw2Pipeline:
    def process_item(self, item, spider):
        return item

class SqliteDemoPipeline:

    def __init__(self):

        ## Create/Connect to database
        self.con = sqlite3.connect('laptops.db')

        ## Create cursor, used to execute commands
        self.cur = self.con.cursor()
        self.cur.execute("""
        DROP TABLE laptops
        """)
        ## Create quotes table if none exists
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS laptops(
            Id INTEGER PRIMARY KEY,
            url TEXT,
            visited_at TEXT,
            ecname TEXT,
            item_mhz REAL,
            ram INTEGER,
            ssd INTEGER,
            price_rub INTEGER,
            rating INTEGER
        )
        """)
        
    def process_item(self, item, spider):

        ## Define insert statement
        self.cur.execute("""
            INSERT INTO laptops (item_mhz, url, price_rub, ecname, visited_at, ssd, ram, rating) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
                 item['item_mhz'],
                 item['url'],
                 item['price_rub'],
                 item['ecname'],
                 item['visited_at'],
                 item['ssd'],
                 item['ram'],
                 (int(item['item_mhz'])*(0.01))+int(item['price_rub'])*(-0.01)+int(item['ram']*3)+int(item['ssd'])*0.01
        ))

        ## Execute insert of data into database
        self.con.commit()
        return item