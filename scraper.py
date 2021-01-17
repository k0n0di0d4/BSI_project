import threading

import requests
import re
from urllib.parse import urlparse

#def loop(self):
#    thread = ["t1", "t2", "t4", "t3", "t5", "t6", "t7", "t8", "t9", "t10"]
#    for i in thread:
#        thread[i] = threading.Thread(target=)
#        thread[i].start()
#        thread[i].join()

class PyCrawler(object):
    def __init__(self, starting_url):
        self.starting_url = starting_url
        self.visited = set()

    def get_html(self, url):
        try:
            html = requests.get(url)
        except Exception as e:
            print(e)
            return ""
        return html.content.decode('latin-1')

    def get_links(self, url):
        html = self.get_html(url)
        parsed = urlparse(url)
        base = f"{parsed.scheme}://{parsed.netloc}"
        links = re.findall('''<a\s+(?:[^>]*?\s+)?href="([^"]*)"''', html) #z tego trzeba wyciągnąć 10 linków
        for i, link in enumerate(links):
            if not urlparse(link).netloc:
                link_with_base = base + link
                links[i] = link_with_base

        return set(filter(lambda x: 'mailto' not in x, links))

    def extract_info(self, url):
        html = self.get_html(url)
        meta = re.findall("<meta .*?name=[\"'](.*?)['\"].*?content=[\"'](.*?)['\"].*?>", html)
        return dict(meta)

    def crawl(self, url):
        for link in self.get_links(url):
            if link in self.visited:
                continue
            self.visited.add(link)
            info = self.extract_info(link)

            print(f"""Link: {link}    
Description: {info.get('description')}    
Keywords: {info.get('keywords')}    
            """)

            self.crawl(link)

    def start(self):
        self.crawl(self.starting_url)


if __name__ == "__main__":
    crawler = PyCrawler("https://google.com")
    crawler.start()
