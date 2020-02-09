import requests
import re

class web:

    def __init__(self, url, depth = 0):

        self.__url   = url
        self.__depth = int(depth)

    def scan(self):

        response = requests.get(self.__url)
        url_list = self.__parse_response_str(response.text)

        for url in url_list:
            print('{} depth URL : '.format(self.__depth) + url)

        while self.__depth > 0:
            for url in url_list:
                response = requests.get(self.__url)
                url_list_dep = self.__parse_response_str(response.text)
                for d_url in url_list_dep:
                    print('{} depth URL : '.format(self.__depth - 1) + d_url)
            self.__depth -= 1
            url_list = url_list_dep


    def __parse_response_str(self, response_str):

        res = []

        for m in re.finditer(r"https?://[\w.]+", response_str):
            res.append(response_str[m.start():m.end()])

        return res


