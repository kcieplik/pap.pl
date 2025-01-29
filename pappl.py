import scrapy
from pap.items import PapItem

class PapplSpider(scrapy.Spider):
    name = "pappl"
    allowed_domains = ["pap.pl"]
    start_urls = ["https://pap.pl"]

    def parse(self, response):
        article_list=response.xpath("//h3[@class='title']/a/@href")
        for article in article_list:
            yield response.follow(article,callback=self.parse_article)


    def parse_article(self,response):

        item = PapItem()
        item['url'] = response.url
        item['title'] = response.xpath("//h1/span/text()").get()
        item['date'] = response.xpath("//div[@class='moreInfo']/text()[normalize-space(.)]").get()
        item['content_lead'] = response.xpath("//article/div/div[contains(@class,'field field--name-field-lead')]/text()").get()
        item['content_article'] = response.xpath("//article/div/div[contains(@class,'field field--name-body')]//text()").get()


        yield item




