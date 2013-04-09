#coding:utf-8
import web
from config import settings

render = settings.render

class talk:
    def GET(self):
        return render.talk()

    def POST(self):
        
        print 'post to talk.'
