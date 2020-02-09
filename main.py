from web import web

url = input('Введите URL: ')
depth = input('Введите глубину поиска: ')

web = web(url, depth)

web.scan()

