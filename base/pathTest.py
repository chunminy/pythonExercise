#/usr/bin/env python
#-*- coding: utf-8 -*-


import os
from os import path, unlink, rename
from sys import (argv as sys_argv, getfilesystemencoding as sys_get_fs_encoding)


def main():
    rootPath = sys_argv[0].decode(sys_get_fs_encoding())
    print 'RootPath\t', rootPath
    #檔案的絕對路徑
    print 'path.abspath\t', path.abspath(rootPath)
    #檔案名稱
    print 'path.basename\t', path.basename(rootPath)
    #檢查檔案是否存在
    print 'path.exists\t', path.exists(rootPath)
    #取得檔案目錄位置
    print 'path.dirname\t', path.dirname(rootPath)
    #分割出副檔名
    print 'path.splitext\t', path.splitext(rootPath)
    #修改時間
    print 'path.getatime\t', path.getatime(rootPath)
    #檔案大小
    print 'path.getsize', path.getsize(rootPath)
    #路徑正規劃，正反斜線清除整理
    print 'path.normcase', path.normcase(rootPath)
    #由後面路徑推敲出前面路徑的相對位置
    print 'path.relpath', path.relpath(rootPath, path.dirname(rootPath)+'/../../')

    #檢查路徑下所有檔案
    print 'path.walk(path, visit, arg)'
    for root, dirs, files in os.walk(path.dirname(rootPath)):
        print root
        for f in files:
            print os.path.join(root, f)





if __name__ == '__main__':
    main()
