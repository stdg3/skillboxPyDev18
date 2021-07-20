def primitive():
    sites_size = dict()
    for url in sites:
        print(f"Openning {url}")
        sizer = PageSizer(url)
        sizer.run()
        # res = urlopen(url)
        # res = requests.get(url)
        # # html_data = res.read()
        # html_data = res.text
        # # pprint(html_data)  # byte
        # # html_data = html_data.decode("utf8")  # use with urlopen()
        # # pprint(html_data)
        # # print(len(html_data))
        # total_bytes = len(html_data)
        # # print("*" * 20, total_bytes)
        # exctractor = LinkExctractor()
        # exctractor.feed(html_data)
        # # print(exctractor.links)
        # for link in exctractor.links:
        #     print(f"\tExtracting {link}")
        #     try:
        #         res = requests.get(url)
        #     except Exception as e:
        #         print(e)
        #     extra_data = res.text
        #     total_bytes += len(extra_data)
        print(f"For {url} need {sizer.total_bytes// 1024} Kbytes from online")
        sites_size[url] = sizer.total_bytes // 1024

    pprint(sites_size)
