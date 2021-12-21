import scrapy


class SelfstudyspiderSpider(scrapy.Spider):
    # Spider name
    name = 'selfstudyspider'
    #list of domains
    allowed_domains = ['mahmoudodeh.pythonanywhere.com']
    # list of start urls
    start_urls = ['http://mahmoudodeh.pythonanywhere.com']

    # response = object containing the data scraped from our url website
    def parse(self, response):
        # let's fetch the data from selfstudy website using xpath
        title = response.xpath('/html/body/div[1]/div/div[1]/h5/text()').get()
        return {"title":title}
