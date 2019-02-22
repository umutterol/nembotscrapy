from invasions import InvasionTimer
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import warcraftlogs.warcraftlogs.spiders

process = CrawlerProcess(get_project_settings())

process.crawl('ranking')
process.start()