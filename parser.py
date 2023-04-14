from bs4 import BeautifulSoup
import requests
import json


class Parser:
    def __init__(self, source):
        self.source = source
        self.currency = []
    def parse(self):
        with open(self.source) as file:
            doc = file.read()
        doc = BeautifulSoup(doc, "html.parser")
        tbody = doc.tbody
        trs = tbody.contents  
        for tr in trs[:10]:
            name = str(tr.contents[2].p.string)
            price = float(tr.contents[3].a.string[1:].replace(',', ''))
            h_24 = float(tr.contents[5].find('span').get_text()[:4])
            volume = float(tr.contents[8].p.string[1:].replace(',', ''))
            self.currency.append({"name": name, "price": price, "h_24": h_24, "volume": volume})
        return self.currency
    def save(self, parsed_file_path):
        with open(parsed_file_path, 'w') as file:
            file.write(json.dumps(self.currency))
            
            

