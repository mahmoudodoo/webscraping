import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class WikispiderSpider(CrawlSpider):
    name = 'wikispider'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['http://en.wikipedia.org/wiki/Main_Page']

    rules = [Rule(LinkExtractor(allow=r"wiki/((?!:).)*$"),callback="parse",follow=True)]

    def parse(self, response):
        return {
            "title": response.xpath("""//*[@id="From_today's_featured_article"]/text()""").get(),
            "url": response.url,
            "article": response.xpath("""//*[@id="mp-tfa"]/p/text()[13]""").get()
        }
# now let's run the spider crawl 
# it will still running you can stop it using ctrl+c