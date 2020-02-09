import requests
import re

class web:

    def __init__(self, url, depth = 0):

        self.__url   = url
        self.__depth = depth

    def scan(self):

        response = requests.get(self.__url)

        return self.__parse_response_str(response.text)

    def __parse_response_str(self, response_str):

        res = []

        for m in re.finditer(r"https?://[\w.]+", response_str):
            res.append(response_str[m.start():m.end()])

        return res


