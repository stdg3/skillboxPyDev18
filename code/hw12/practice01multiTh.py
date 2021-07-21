# from urllib.request import urlopen

from extractor import LinkExctractor
from utils import time_track

import requests

import threading

sites = [
    # "https://www.google.com"
    'https://www.fl.ru',
    'https://www.weblancer.net/',
    'https://www.freelancejob.ru/',
    # 'https://kwork.ru',
    'https://work-zilla.com/',
    'https://iklife.ru/udalennaya-rabota-i-frilans/poisk-raboty/vse-samye-luchshie-sajty-i-birzhi-v-internete.html',
]


class PageSizer(threading.Thread):
    def __init__(self, url, go_ahead=True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.url = url
        self.total_bytes = 0
        self.go_ahead = go_ahead

    def run(self):
        self.total_bytes = 0
        html_data = self._get_html(self.url)
        if html_data is None:
            return
        self.total_bytes += len(html_data)
        if self.go_ahead:
            exctractor = LinkExctractor(self.url)
            exctractor.feed(html_data)
            sizers = [PageSizer(link, False) for link in exctractor.links]
            for sizer in sizers:
                sizer.start()
            for sizer in sizers:
                sizer.join()
            for sizer in sizers:
                self.total_bytes += sizer.total_bytes

    def _get_html(self, url):
        try:
            print(f"Go {url}...")
            res = requests.get(url)
        except Exception as e:
            print(e)
        else:
            return res.text


@time_track
def main():
    sizers = [PageSizer(url=url) for url in sites]

    for sizer in sizers:
        sizer.start()
    for sizer in sizers:
        sizer.join()

    for sizer in sizers:
        print(
            f"For url {sizer.url} need {sizer.total_bytes // 1024}",
            f"KB or {sizer.total_bytes} bytes data",
            )


if __name__ == "__main__":
    main()
