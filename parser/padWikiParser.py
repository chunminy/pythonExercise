#/usr/bin/env python
#-*- coding: utf-8 -*-

import os
from os import path, unlink, rename
import datetime
import time
from time import strftime
from optparse import OptionParser
from subprocess import (check_output as sp_co, CalledProcessError)
from sys import (argv as sys_argv, getfilesystemencoding as sys_get_fs_encoding)
from re import compile as re_compile
import xml.etree.cElementTree as ET
from hashlib import md5 as hl_md5
from fileinput import (input as fi_input, close as fi_close)
import json
from json import (loads as json_loads, dump as json_dump)
import smtplib
import smtplib
import urllib
import urllib2



import urllib
from sgmllib import SGMLParser

class ItemIndo(object):
    def __init__(self):
        self.name = ''
        self.prop = ''
        self.type = ''
        self.id = ''
        self.start = ''
        self.maxExt = 0
        self.sys = ''
        self.cost = 0
        self.lv1HP = 0
        self.lv1Att = 0
        self.lv1Life = 0
        self.ext = 0
        self.maxLV = 0
        self.maxHP = 0
        self.maxAtt = 0
        self.maxLift = 0
    def __str__(self):
    	info = 'ID:{}, 名稱:{}, 屬性:{}, 類型:{}, 稀有:{}, 滿級經驗:{}, 系列：{}'.format(self.id, self.name, self.prop, self.type, self.start, self.maxExt, self.sys)
    	info += ', cost:{}, LV1 HP:{}, LV1 攻擊力:{}, LV1 恢復力:{}, 經驗類型:{}'.format(self.cost, self.lv1HP, self.lv1Att, self.lv1Life, self.ext)
    	info += ', 最大LV:{}, 滿級 HP:{}, 滿級攻擊力:{}, 滿級恢復力:{}'.format(self.maxLV, self.maxHP, self.maxAtt, self.maxLift)
    	return info


class ListName(SGMLParser):
    def __init__(self):
        SGMLParser.__init__(self)
        self.is_table = 0
        self.is_td = 0
        self.listIndex = 0
        self.itemIndex = 0
        self.list = []
        self.list.append(ItemIndo())

    def start_table(self, attrs):
        if attrs [1][1][0] == 'w':
            return
        self.is_table = 1
        self.itemIndex = 0

    def end_table(self):
        self.is_table = 0
        self.listIndex += 1
        self.list.append(ItemIndo())

    def start_td(self, attrs):
        self.is_td = 1

    def end_td(self):
        self.is_td = 0

    def handle_data(self, text):
        if self.is_table != 1 or self.is_td != 1:
            return
        info = text.replace('\n','')
        info = info.replace(' ','')

        if self.itemIndex == 1:
            self.list[self.listIndex].name = info
        elif self.itemIndex == 3:
            self.list[self.listIndex].prop = info
        elif self.itemIndex == 4:
            self.list[self.listIndex].type = info
        elif self.itemIndex == 5:
            self.list[self.listIndex].id = info
        elif self.itemIndex == 6:
            self.list[self.listIndex].start = info
        elif self.itemIndex == 7:
            self.list[self.listIndex].maxExt = info
        elif self.itemIndex == 8:
            self.list[self.listIndex].sys = info
        elif self.itemIndex == 9:
            self.list[self.listIndex].cost = info
        elif self.itemIndex == 10:
            self.list[self.listIndex].lv1HP = info
        elif self.itemIndex == 11:
            self.list[self.listIndex].lv1Att = info
        elif self.itemIndex == 12:
            self.list[self.listIndex].lv1Life = info
        elif self.itemIndex == 13:
            self.list[self.listIndex].ext = info
        elif self.itemIndex == 14:
            self.list[self.listIndex].maxLV = info
        elif self.itemIndex == 15:
            self.list[self.listIndex].maxHP = info
        elif self.itemIndex == 16:
            self.list[self.listIndex].maxAtt = info
        elif self.itemIndex == 17:
            self.list[self.listIndex].maxLift = info

        self.itemIndex += 1



# Main

def parsetInfo(path):
    htmlSource = urllib.urlopen(path).read()
    listname = ListName()
    listname.feed(htmlSource)
    for item in listname.list:
        if len(item.id) == 0:
            continue
        print '================================================='
        print item



def main():

    count = 0
    begin = 0
    end = 0
    while(end < 2400):
    	begin = count * 20 + 1
    	end = (count + 1) * 20
    	count += 1
    	beginStr = '{}'.format(begin).zfill(3)
    	endStr = '{}'.format(end).zfill(3)
    	path = 'http://zh.pad.wikia.com/wiki/%E5%AE%A0%E7%89%A9%E5%88%97%E8%A1%A8{}-{}'.format(beginStr, endStr)
    	parsetInfo(path)
        time.sleep(1)



if __name__ == '__main__':
    main()
