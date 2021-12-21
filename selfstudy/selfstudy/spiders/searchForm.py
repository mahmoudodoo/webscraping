import scrapy
from scrapy.http import FormRequest

class SearchformSpider(scrapy.Spider):
    name = 'searchForm'
    allowed_domains = ['mahmoudodeh.pythonanywhere.com']
    # start_urls = ['http://mahmoudodeh.pythonanywhere.com/']
    def start_requests(self):
        return [
        FormRequest('http://mahmoudodeh.pythonanywhere.com/filter_course',
        formdata={'searchcourse':'python'},
        callback=self.parse
        )]

    def parse(self, response):
        return {'result':response.xpath("""/html/body/div[1]/div/h1/text()""").get()}
