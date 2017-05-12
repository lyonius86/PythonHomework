#!usr/bin/env python3
# -*- coding: utf-8 -*-
#

'''
	tweet精简。有时候你想要查看由Twitter用户发送到Tiwtter服务的tweet纯文本。
	创建一个函数以获取tweet和一个可选的“元”标记，该标记默认为False，然后返回一个已精简过的tweet字符串，
	即移除所有无关信息，例如，表示转推的RT符号、前导的“.”符号，以及所有#号标签。如果元标记为True，
	就返回一个包含元数据的字典。这可以包含一个键“RT”,其相应的值是转推改消息的用户的字符串元组和/或一个键“#号标签”（包含一个#号标签元组）。
	如果值不存在（空元组），就不要为此创建一个键值条目。
'''
import re

tweet = 'RT JackMan #123456789..##22#..'

def getTweet(tweet,flag=False):
	patt = r'(RT|\.|#)'
	m = re.sub(patt, '', tweet)
	# if flag:

getTweet(tweet)
