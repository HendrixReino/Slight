import scrapy
from scrapy_splash import SplashRequest

filename = 'company_ranking.txt'

class MIT(scrapy.Spider):
    name = "mit"

    def start_requests(self):
        yield SplashRequest(
        url=[
        'https://sloanreview.mit.edu/culture500/rankings/inclusivity?page=1',
        'https://sloanreview.mit.edu/culture500/rankings/inclusivity?page=2',
        'https://sloanreview.mit.edu/culture500/rankings/inclusivity?page=3',
        'https://sloanreview.mit.edu/culture500/rankings/inclusivity?page=4',
        'https://sloanreview.mit.edu/culture500/rankings/inclusivity?page=5',
        'https://sloanreview.mit.edu/culture500/rankings/inclusivity?page=6',
        'https://sloanreview.mit.edu/culture500/rankings/inclusivity?page=7',
        'https://sloanreview.mit.edu/culture500/rankings/inclusivity?page=8',
        'https://sloanreview.mit.edu/culture500/rankings/inclusivity?page=9',
        'https://sloanreview.mit.edu/culture500/rankings/inclusivity?page=10',
        'https://sloanreview.mit.edu/culture500/rankings/inclusivity?page=11',
        'https://sloanreview.mit.edu/culture500/rankings/inclusivity?page=12',
        'https://sloanreview.mit.edu/culture500/rankings/inclusivity?page=13',
        'https://sloanreview.mit.edu/culture500/rankings/inclusivity?page=14',
        'https://sloanreview.mit.edu/culture500/rankings/inclusivity?page=15',
        'https://sloanreview.mit.edu/culture500/rankings/inclusivity?page=16',
        'https://sloanreview.mit.edu/culture500/rankings/inclusivity?page=17',
        'https://sloanreview.mit.edu/culture500/rankings/inclusivity?page=18',
        'https://sloanreview.mit.edu/culture500/rankings/inclusivity?page=19',
        'https://sloanreview.mit.edu/culture500/rankings/inclusivity?page=20',
        ])
        yield SplashRequest()


def parse(self, response):

        company_list = response.xpath('//*[@id="root"]/div/div/div/div/div/div')\
            .extract()

        with open(filename, 'a+') as f:
            for company_ranking in company_list:
                f.write(company_ranking + "\n")