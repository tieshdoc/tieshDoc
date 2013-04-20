#coding:utf-8
import web

#will add "'context': session" here to enable session in template
#session is defined in server.py?
globals = {'str': str,}
render = web.template.render('templates/', globals = globals)
