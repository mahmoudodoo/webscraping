import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from engo.items import EngoItem

class EngospiderSpider(CrawlSpider):
   name = 'engospider'
   allowed_domains = ['engoo.com.tw']
   start_urls = ['https://engoo.com.tw/app/daily-news/article/uk-man-builds-model-train-with-1-kilometer-of-tracks/Y-y2Vl6rEey-riMkm7WgAA']
   rules = [Rule(LinkExtractor(allow=r"app/daily-news/article/((?!:).)*$"),callback="parse",follow=True)]

   def parse(self, response):
       article = EngoItem()
       article['title']= response.xpath("""//*[@id="content"]/div/div[1]/div/div/div/div/div/div[1]/div/div/div[2]/div[2]/div[1]/div/span/span/span/text()""").get()
       article['url']= response.url
       article['date']= response.xpath("""//*[@id="content"]/div/div[1]/div/div/div/div/div/div[1]/div/div/div[2]/div[2]/div[3]/span/text()""").get()
       return article