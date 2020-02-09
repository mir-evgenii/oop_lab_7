import requests
import re

class web:

    def __init__(self, url, depth = 0):

        self.__url   = url
        self.__depth = int(depth)

    def scan(self):

        response = requests.get(self.__url)
        url_list = self.__parse_response_str(response.text)

        self.__print_url_list(url_list, self.__depth)

        while self.__depth > 0:
            for url in url_list:
                response = requests.get(self.__url)
                new_url_list = self.__parse_response_str(response.text)
                self.__print_url_list(new_url_list, self.__depth - 1)
            self.__depth -= 1
            url_list = new_url_list

    def __print_url_list(self, url_list, depth):
        for url in url_list:
            print('{} depth URL : '.format(depth) + url)

    def __parse_response_str(self, response_str):

        res = []

        for m in re.finditer(r"https?://[\w.]+", response_str):
            res.append(response_str[m.start():m.end()])

        return res


