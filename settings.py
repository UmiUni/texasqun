# -*- coding: UTF-8 -*-
import datetime
def init():

  global chatGroups
  global vT
  global usersDict
  global admins 
  global ADMIN
  global previousDay

  chatGroups =[
  u'达拉斯租房二手万能总群',
  u'休斯顿租房二手万能总群',
  u'leetcode天天',
  u'北美CPA',
  u'北美妈妈',
  u'北美信用',
  u'线上KTV',
  u'北美表情分享',
  u'德州实习工作内推总群'
  ]

  v000= u"您好,德州加群建群小助手为您服务:)\n"
  v00=u"每天只能加3个群哦;\n"
  v0= u"回复 0 加达拉斯租房二手万能总群;\n"
  v1= u"回复 1 加休斯顿租房二手万能总群;\n"
  v2= u"回复 2 加leetcode天天刷题群;\n"
  v3= u"回复 3 加北美CPA,REG会计群;\n"
  v4= u"回复 4 加北美妈妈母婴总群;\n"
  v5= u"回复 5 加北美信用卡爱好者总群;\n"
  v6= u"回复 6 加线上KTV开嗓🎙️北美总群;\n"
  v7= u"回复 7 加北美表情分享总群;\n"
  v8= u"回复 8 加德州实习工作内推总群;"
  v12= u"回复 99 查看【北美加群小助手Jogchat.com】\n 公众号二维码加硅谷、西雅图、三番、UIUC、Purdue等地群\n"
  vT =v000+v00+v0+v1+v2+v3+v4+v5+v6+v7+v12
  
  usersDict = {}
  admins = []
  ADMIN = u'NY纽约加群小助手'
  previousDay = datetime.datetime.now().day
