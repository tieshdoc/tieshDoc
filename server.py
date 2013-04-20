#coding:utf-8
from config.url import urls
import web

web.config.debug = False  #to support session

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()