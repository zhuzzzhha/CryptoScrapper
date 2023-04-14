import json
def process(url, web_page_path=None, data_path=None):
    downloader = DownLoader(url, params = {})
    downloader.save(web_page_path)
    
    parser = Parser(downloader.file_path)
    parser.parse()
    parser.save(data_path)
    
    data = Datahandler(data_path)
    data1 = data.loader()
    currency_volume_graph(data1)
    currency_price_graph(data1)
url = "https://coinmarketcap.com/"
params = {}
web_page_path = 'data.txt'
data_path = 'parsed.json'
process(url, web_page_path, data_path)
