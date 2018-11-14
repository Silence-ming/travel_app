from django.shortcuts import HttpResponse
from .model.sql import sql
from .model import md as m
import json
import  re
import time
import random
def ask(req):
    my=sql()
    data=my.sel_many('select * from questions order by times desc')
    my.close()
    return HttpResponse(json.dumps(data))
def askQuestion(req):
    id=req.GET.get('id')
    my = sql()
    question = my.sel_one('select * from questions where id=%s',[id])
    my.close()
    return HttpResponse(json.dumps(question))
def askDetail(req):
    id=req.GET.get('id')
    my = sql()
    answer = my.sel_many('select *,user.name,user.head,user.id from answers left join user on answers.uid=user.id where qid=%s order by times desc',[id])
    my.close()
    return HttpResponse(json.dumps(answer))
def notes(req):
    my = sql()
    notes = my.sel_many('select *,user.name,user.head,user.id from travel_note left join user on travel_note.uid=user.id order by travel_note.times desc')
    my.close()
    return HttpResponse(json.dumps(notes))
def login(req):
        userName=req.GET.get('userName')
        password=req.GET.get('password')
        my=sql()
        result=my.sel_one('select * from user where name=%s and password=%s',[userName,m.md5(password)])
        my.close()
        if result:
            return HttpResponse(str(result['id']))
        else:
            return HttpResponse("error")
def reg(req):
    userName = req.GET.get('userName')
    password = req.GET.get('password')
    password1 = req.GET.get('password1')
    db=sql()
    result=db.sel_one("select * from user where name=%s",userName)
    db.close()
    if result:
        return  HttpResponse("cunzai")
    else:
        if re.match(r'^[a-zA-Z]+\w$', userName) and re.match(r'^[a-zA-Z0-9_]{6,32}',password) and password == password1:
            my = sql()
            my.one('insert into user (name,password,head,uname,note) values (%s,%s,%s,%s,%s)',[userName,m.md5(password), 'Http://localhost:8000/static/img/11.jpg', userName, 'You can write your personalized signature here'])
            my.close()
            return HttpResponse("ok")
        else:
            return HttpResponse("no")
def person(req):
    id=req.GET.get('id')
    my=sql()
    data=my.sel_one('select * from user where id=%s',[id])
    my.close()
    return HttpResponse(json.dumps(data))
def cites(req):
    my=sql()
    data=my.sel_many('select * from city ')
    my.close()
    return HttpResponse(json.dumps(data))
def scenicBanners(req):
    my=sql()
    data=my.sel_many('select * from scenic where banner_sign = 1')
    my.close()
    return HttpResponse(json.dumps(data))
def firstScenic(req):
    my = sql()
    data = my.sel_many('select * from scenic limit 0,4')
    my.close()
    return HttpResponse(json.dumps(data))
def noteBanner(req):
    my=sql()
    data=my.sel_many('select * from travel_note where banner_sign = 1')
    my.close()
    return HttpResponse(json.dumps(data))
def scenic(req):
    cid=req.GET.get('cid')
    my=sql()
    data=my.sel_many('select * from scenic where cid=%s',[cid])
    my.close()
    return HttpResponse(json.dumps(data))
def scenicDetail(req):
    id = req.GET.get('id')
    my = sql()
    data = my.sel_one('select * from scenic where id=%s', [id])
    my.close()
    return HttpResponse(json.dumps(data))
def asking(req):
    uid=req.GET.get('uid')
    question=req.GET.get('question')
    if uid and question :
        my=sql()
        now='发表于'+str(time.strftime('%Y.%m.%d',time.localtime(time.time())))
        my.one('insert into questions (uid,times,question) values(%s,%s,%s)',[uid,now,question])
        my.close()
        return  HttpResponse('ok')
    else:
        return HttpResponse('no')
def answer(req):
    uid = req.GET.get('uid')
    qid = req.GET.get('qid')
    answer = req.GET.get('answer')
    now = str(time.strftime('%Y.%m.%d', time.localtime(time.time())))
    my = sql()
    try:
        my.one('insert into answers (uid,times,qid,answer) values (%s,%s,%s,%s)',[uid,now,qid,answer])
    except:
        pass
    else:
        my.close()
        return HttpResponse('ok')
def writing(req):
    uid = req.GET.get('uid')
    img =req.GET.get('imgs')
    experience = req.GET.get('experience')
    now = '发表于'+str(time.strftime('%Y.%m.%d', time.localtime(time.time())))
    my = sql()
    try:
        my.one('insert into travel_note (uid,times,img,experience) values (%s,%s,%s,%s)',[uid,now,img,experience])
    except:
        pass
    else:
        my.close()
        return HttpResponse('ok')
def collections(req):
    uid =req.GET.get('uid')
    my = sql()
    data = my.sel_many('select scenic.id,scenic.name,scenic.img,scenic.detail from collections as col left join scenic on col.sid = scenic.id where col.uid = %s',[uid])
    my.close()
    return HttpResponse(json.dumps(data))
def MyTravel(req):
    uid = req.GET.get('uid')
    my = sql()
    data = my.sel_many('select * from travel_note where uid = %s',[uid])
    my.close()
    return HttpResponse(json.dumps(data))
def myAsks(req):
    uid = req.GET.get('uid')
    my = sql()
    data = my.sel_many('select * from questions where uid = %s', [uid])
    my.close()
    return HttpResponse(json.dumps(data))
def myAnswers(req):
    uid = req.GET.get('uid')
    my = sql()
    data = my.sel_many('select *,questions.question from answers left join questions on answers.qid = questions.id where answers.uid = %s order by answers.times desc', [uid])
    my.close()
    return HttpResponse(json.dumps(data))
def information(req):
    uid = req.GET.get('uid')
    my = sql()
    data = my.sel_one( 'select * from user where id = %s',[uid])
    my.close()
    return HttpResponse(json.dumps(data))
def rehead(req):
    uid = req.GET.get('uid')
    newhead = req.GET.get('newhead')
    my = sql()
    my.one('update user set head = %s where id = %s',[newhead,uid])
    my.close()
    return HttpResponse('ok')
def update_info(req):
    uid = req.GET.get('uid')
    newName = req.GET.get('name')
    newNote = req.GET.get('note')
    my = sql()
    my.one('update user set uname = %s,note = %s where id = %s',[newName,newNote,uid])
    my.close()
    return HttpResponse('ok')
def rePassWord(req):
    uid = req.GET.get('uid')
    oldPassWord = req.GET.get('oldPassWord')
    newPassWord = req.GET.get('newPassWord')
    my = sql()
    data = my.sel_one( 'select user.password from user where id = %s',[uid])
    if m.md5(oldPassWord) == data['password']:
        my.one('update user set password = %s where id =%s',[m.md5(newPassWord),uid])
        my.close()
        return HttpResponse('yes')
    else:
        my.close()
        return HttpResponse('no')
