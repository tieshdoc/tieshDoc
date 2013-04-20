#coding:utf-8
import web
from config import settings

render = settings.render

class index:
    def GET(self):
        return 'Hello index page!'