import requests, json
from bs4 import BeautifulSoup

session = requests.Session()
link = 'https://oonkp3uljw-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia for vanilla JavaScript (lite) 3.27.0;instantsearch.js 2.10.0;JS Helper 2.26.0&x-algolia-application-id=OONKP3ULJW&x-algolia-api-key=eb15157a5951afee593ed4771d2070d7'
data = '{"requests":[{"indexName":"jobs:en:1","params":"query=&maxValuesPerFacet=100&page=0&filters=publishingDateTimestamp%3A1549261198%20TO%201580797198&facets=%5B%22locationArea%22%2C%22locationCity%22%2C%22locationCountry%22%2C%22mainFields%22%2C%22positions%22%2C%22employer.name%22%2C%22Agricultural%20Science%22%2C%22Anthropology%22%2C%22Architecture%20and%20Design%22%2C%22Arts%20and%20Culture%22%2C%22Biology%22%2C%22Business%20and%20Economics%22%2C%22Chemistry%22%2C%22Computer%20Science%22%2C%22Education%22%2C%22Engineering%22%2C%22Geosciences%22%2C%22History%22%2C%22Law%22%2C%22Linguistics%22%2C%22Literature%22%2C%22Mathematics%22%2C%22Medicine%22%2C%22Philosophy%22%2C%22Physics%22%2C%22Political%20Science%22%2C%22Psychology%22%2C%22Social%20Science%22%2C%22Space%20Science%22%2C%22Theology%22%2C%22location.lvl0%22%2C%22location.lvl0%22%2C%22location.lvl0%22%2C%22location.lvl0%22%5D&tagFilters="}]}'
UA = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',
    'Accept': 'application/json',
    'Accept-Language': 'en',
    'Accept-Encoding': 'gzip, deflate',
    'content-type': 'application/x-www-form-urlencoded',
    'Content-Length': str(len(data)),
    'Origin': 'https://academicpositions.com',
    'Connection': 'close',
    'Referer': 'https://academicpositions.com/find-jobs/all-in-all-by-all-in-all/all/1'
}
getlink = session.post(link, headers=UA, data=data)
resplink = BeautifulSoup(getlink.content, 'html.parser')
js_dict = json.loads(resplink.text)
for x in range(len(js_dict['results'][0]['hits'])):
    job_name = js_dict['results'][0]['hits'][x]['employer']['name']
    job_city = js_dict['results'][0]['hits'][x]['employer']['city']
    job_link = 'https://academicpositions.com'+js_dict['results'][0]['hits'][x]['renderedSlug']
    info = 'Job '+str(x+1)+': '+'Name: {} | City: {} | Link job: {}'.format(job_name, job_city, job_link)
    print(info)
