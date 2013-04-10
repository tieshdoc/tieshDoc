#coding:utf-8
import time

talks=[
    {'tid': 0, 'ptid': 0, 'potime': '2013-04-10 Wednesday 14:06:11 CST', 'poname': 'ztall', 
    'data': '中文编码问题解决方案：tpl文件处定义charset=utf-8，处处以utf-8统一。'}, 
    {'tid': 1, 'ptid': 1, 'potime': '2013-04-10 Wednesday 14:06:15 CST', 'poname': 'ztall', 
    'data': '回复逻辑设计：tid表示这一条talk的id,ptid表示parenttid，两者相同则说明是新发布的。'}]

def get_alltalks():
    return talks

def add_talkitem(ptid = None, poname = None, data = None):
    def get_newtid():
        return max(map(lambda x: x['tid'] ,talks)) + 1
    newtid = get_newtid()
    if not ptid:
        ptid = newtid
    potime = time.strftime("%Y-%m-%d %A %X %Z", time.localtime())
    talkitem = dict(tid = newtid, ptid = ptid, potime = potime, poname = poname, data = data)
    talks.append(talkitem)