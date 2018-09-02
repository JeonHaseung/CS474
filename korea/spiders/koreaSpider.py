import scrapy

from korea.items import KoreaItem
import sqlite3 as lite
import unicodedata


database_filename = 'test2.db'
conn = lite.connect(database_filename)
cs = conn.cursor()
#cs.execute('create table data (title, url, content, date)')

class koreaSpider(scrapy.Spider):
    name = "koreaCrawler"
    #start_urls = []
    
    def start_requests(self):
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for i in range(8):
            for j in range(days[i]):
                if i < 9:
                    if j < 9:
                        yield scrapy.Request("https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid2=249&sid1=102&date=20180%s" % str(i+1)+"0"+str(j+1), self.parse_naver)
                    else:
                        yield scrapy.Request("https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid2=249&sid1=102&date=20180%s" % str(i+1)+str(j+1), self.parse_naver)
                else:
                    if j < 9:
                        yield scrapy.Request("https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid2=249&sid1=102&date=2018%s" % str(i+1)+"0"+str(j+1), self.parse_naver)
                    else:
                        yield scrapy.Request("https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid2=249&sid1=102&date=2018%s" % str(i+1)+str(j+1), self.parse_naver)

    def parse_naver(self, response):
        date = response.url.split('date=')[1]
        num1 = response.css('.type06_headline')
        li_xpath = num1.xpath('li')
        for k in li_xpath:
            dt_xpath = k.xpath('dl/dt').extract()
            if len(dt_xpath) == 2:
                title = k.xpath('dl/dt[2]/a/text()').extract()[0].strip()
                url = k.xpath('dl/dt[2]/a/@href').extract()[0].strip()
            else:
                title = k.xpath('dl/dt/a/text()').extract()[0].strip()
                url = k.xpath('dl/dt/a/@href').extract()[0].strip()
            content = k.xpath('dl/dd/span/text()').extract()[0].strip()
            title = title.encode("UTF-8")
            url = url.encode("UTF-8")
            content = content.encode("UTF-8")
            title = title.replace('"','')
            title = title.replace("'",'')
            content = content.replace('"','')
            content = content.replace("'",'')
            cs.execute('insert into data values (\'{}\', \'{}\', \'{}\', \'{}\')'.format(title, url, content, date))
            conn.commit()
            
        num1 = response.css('.type06')
        li_xpath = num1.xpath('li')
        for k in li_xpath:
            dt_xpath = k.xpath('dl/dt').extract()
            if len(dt_xpath) == 2:
                title = k.xpath('dl/dt[2]/a/text()').extract()[0].strip()
                url = k.xpath('dl/dt[2]/a/@href').extract()[0].strip()
            else:
                title = k.xpath('dl/dt/a/text()').extract()[0].strip()
                url = k.xpath('dl/dt/a/@href').extract()[0].strip()
            content = k.xpath('dl/dd/span/text()').extract()[0].strip()
            title = title.encode("UTF-8")
            url = url.encode("UTF-8")
            content = content.encode("UTF-8")
            title = title.replace('"','')
            title = title.replace("'",'')
            content = content.replace('"','')
            content = content.replace("'",'')
            cs.execute('insert into data values (\'{}\', \'{}\', \'{}\', \'{}\')'.format(title, url, content, date))
            conn.commit()


