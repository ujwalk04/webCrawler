import scrapy
from ..items import WebcraltfItem

class QuoteSpider(scrapy.Spider):
    name = 'spidey'
    start_urls = ['https://books.toscrape.com/index.html']

    def parse(self, response):

       altText=response.css("img").xpath("@alt").extract()
       srcText=response.css("img").xpath("@src").extract()


       yield {'Total number of images found: ': str(len(srcText)),
              'Total number of images having alt text: ': str(len(altText)),
              'Total number of images not having alt text: ' :str(len(srcText)-len(altText))
              }
