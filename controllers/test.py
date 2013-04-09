#coding:utf-8
import web
from config import settings

render = settings.render

class test:
	def GET(self):
		return render.test()
