import scrapy
from stockscraper2.items import Stockscraper2Item

class MybotsSpider(scrapy.Spider):
    name = 'mybots'
    allowed_domains = ['finance.naver.com/item/sise.nhn?code=035720']
    start_urls = ['https://finance.naver.com/item/sise.nhn?code=035720']

    def parse(self, response):
        # 데이터 읽어온 시간 데이터 수집 
        read_times = response.xpath('//*[@id="time"]/em/text()').extract()
        # 현재 거래량 수집
        stock_volumes = response.xpath('//*[@id="_quant"]/text()').extract()
        # 현재 가격 수집
        now_prices = response.xpath('//*[@id="_nowVal"]/text()').extract()
        # # 최고가 수집
        max_prices = response.xpath('//*[@id="_high"]/text()').extract()
        # 최저가 수집
        min_prices = response.xpath('//*[@id="_low"]/text()').extract()
        # 종목 코드 수집
        stock_codes = response.xpath('//*[@id="middle"]/div[1]/div[1]/div/span[1]/text()').extract()

        items = []
        for idx in range(len(stock_codes)):
            item = Stockscraper2Item()

            item['read_time'] = read_times[idx]
            item['stock_volume'] = stock_volumes[idx]
            item['now_price'] = now_prices[idx]
            item['max_price'] = max_prices[idx]
            item['min_price'] = min_prices[idx]
            item['stock_code'] = stock_codes[idx]
            items.append(item)
        
        return items
