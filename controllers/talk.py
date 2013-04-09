#coding:utf-8
import web
from config import settings
from web import form

render = settings.render

talk_form = form.Form(
    form.Textbox('postername', description='postername', id='postername'),
    form.Textarea('talkdata', description='talkdata'),
    form.Button('submit', type='submit', description='submit')
)

class talk:
    def GET(self):
        tf = talk_form()
        return render.talk(tf)

    def POST(self):
        print 'post to talk.'
