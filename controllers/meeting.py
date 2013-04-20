#coding: utf-8
import web
from config import settings
from db import dblocal

render = settings.render

# I will add authentication after
class manage:

    def GET(self):
        return render.mm()