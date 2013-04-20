#coding:utf-8

prefix = 'controllers.'
urls = (
    '/', prefix + 'index.index',
    '/talk', prefix + 'talk.talk',
    '/meeting/manage', prefix + 'meeting.manage',
    #for test
	'/test', prefix + 'test.test',
)
