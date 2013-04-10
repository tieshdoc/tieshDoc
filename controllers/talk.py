#coding:utf-8
import web
from config import settings
from web import form
from db import dblocal

render = settings.render

talk_form = form.Form(
    form.Textbox('postername', description='postername', id='postername'),
    form.Textarea('talkdata', description='talkdata'),
)

class talk:
    def GET(self):
        tform = talk_form()
        talklist = dblocal.get_alltalks()
        return render.talk(tform, talklist, str)

    def POST(self):
        tform = talk_form()
        talklist = dblocal.get_alltalks()
        post_data = web.input()
        dblocal.add_talkitem(None, post_data.postername, post_data.talkdata)
        return render.talk(tform, talklist, str)