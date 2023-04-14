class DownLoader:
    def __init__(self, url, params, method = "GET"):
        self.url = url
        self.params = params
        self.method = method
        self.file_path = ""
    def get_html():
        result = requests.get(url).text
        return result
    def save(self, file_path):
        with open(file_path, 'w') as outfile:
            outfile.write(requests.get(url).text)
        self.file_path = file_path
