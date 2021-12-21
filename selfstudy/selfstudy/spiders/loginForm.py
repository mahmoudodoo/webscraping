import scrapy
from scrapy.http import FormRequest

class LoginformSpider(scrapy.Spider):
    name = 'loginForm'
    allowed_domains = ['mahmoudodeh.pythonanywhere.com']
    def start_requests(self):
        return [
        FormRequest('http://mahmoudodeh.pythonanywhere.com/login_view',
        formdata={'username':'user1','password':'user123456'},
        callback=self.parse
        )]

    def parse(self, response):
        return {'message':response}