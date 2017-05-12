#!usr/bin/env python3
# -*- coding:utf-8 -*-
#

'''
	处理信用卡号码。1.2节还提供了一个能够匹配信用卡(CC)号码([0-9]{15，16})的正则表达式模式。
	然而，该模式不允许使用连字符来分割数字块。
	创建一个允许使用连字符的正则表达式，但是仅能用于正确的位置。
	例如，15位的信用卡号码使用4-6-5的模式，表明4个数字-连字符-6个数字-连字符-5个数字；
		16位的信用卡号码使用4-4-4-4的模式。
	记住，要对整个字符串进行合适的分组。
	选做题：用一个判断信用卡号码是否有效的标准算法。
	编写一些代码，这些代码不但能够识别具有正确格式的号码，而且能够识别有效的信用卡号码。
'''

import re

patt = r'([0-9]{4}-?[0-9]{6}-?[0-9]{5})|([0-9]{4}-?[0-9]{4}-?[0-9]{4}-?[0-9]{4})'
# data = '1111-1111-1111-1111'
data = '1111-111111-11111'
m = re.match(patt, data)
if m is not None: print(m.group())
