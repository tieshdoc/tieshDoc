#coding:utf-8
import time

#吐槽本部分
talks=[
    {'tid': 0, 'ptid': 0, 'potime': '2013-04-10 Wednesday 14:06:11', 'poname': 'ztall', 
    'data': '中文编码问题解决方案：tpl文件处定义charset=utf-8，处处以utf-8统一。'}, 
    {'tid': 1, 'ptid': 1, 'potime': '2013-04-10 Wednesday 14:06:15', 'poname': 'ztall', 
    'data': '回复逻辑设计：tid表示这一条talk的id,ptid表示parenttid，两者相同则说明是新发布的。'},
    {'tid': 2, 'ptid': 0, 'potime': '2013-04-10 Wednesday 14:09:11', 'poname': 'ztall', 
    'data': '新问题：在东东的windows上面编码悲剧了。'},
    {'tid': 3, 'ptid': 0, 'potime': '2013-04-10 Wednesday 14:09:11', 'poname': 'ztall', 
    'data': '新问题解决：编码错误由localtime中一部分引起，已修改。'},]

# 例会纲要部分
#meetingfile = [{'mfid': , 'ctime': ,'mtime': , 'position': ,'nummem': , 'abmem': }]
#meetingitem = [{'itemid': , 'mfid': , 'title': , 'who': , 'data': }]

def get_alltalks():
    return talks

def add_talkitem(ptid = None, poname = None, data = None):
    def get_newtid():
        return max(map(lambda x: x['tid'] ,talks)) + 1
    newtid = get_newtid()
    if not ptid:
        ptid = newtid
    potime = time.strftime('%Y-%m-%d %A %X', time.localtime())
    talkitem = dict(tid = newtid, ptid = ptid, potime = potime, poname = poname, data = data)
    talks.append(talkitem)
