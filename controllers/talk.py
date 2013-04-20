#coding:utf-8
import web
from config import settings
from web import form
from db import dblocal

render = settings.render

class talk:
    talk_form = form.Form(
        form.Textbox('postername', description='postername', id='postername'),
        form.Textarea('talkdata', description='talkdata'),
    )

    def GET(self):
        tform, talklist = self.talk_form(), dblocal.get_alltalks()
        return render.talk(tform, talklist)

    def POST(self):
        tform, talklist = self.talk_form(), dblocal.get_alltalks()
        post_data = web.input()
        dblocal.add_talkitem(None, post_data.postername, post_data.talkdata)
        return render.talk(tform, talklist)