import scrapy

from pep_parse.constants import (NUMBER, NAME, PEP_LINKS, STATUS, STATUS_XPATH,
                                 TITLE, TITLE_ALL)
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    """Паук для парсинга PEP с сайта."""

    name = "pep"
    allowed_domains = ["peps.python.org"]
    start_urls = ["https://peps.python.org/"]

    def parse(self, response):
        """Собирает ссылки на страницы отдельных PEP."""
        links = response.css(PEP_LINKS).getall()
        for link in links:
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        """Парсит страницу PEP и возвращает объект PepParseItem."""
        title = ''.join(response.css(TITLE_ALL).getall()).strip()

        item = PepParseItem()
        item[NUMBER] = response.css(TITLE).re_first(r'\d+')
        item[NAME] = title.split('–', 1)[-1].strip()
        item[STATUS] = response.xpath(STATUS_XPATH).get()
        yield item
