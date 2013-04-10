#coding:utf-8
from config.url import urls
import web

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()