#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from langconv import *
import argparse
 
# 繁体转简体
def TraditionalToSimplified(content):
    line = Converter("zh-hans").convert(content)
    return line
 
# 简体转繁体
def SimplifiedToTraditional(content):
    line = Converter("zh-hant").convert(content)
    return line
 
if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    # 文件名
    parser.add_argument('file_name',metavar='N', type=str, nargs='*')
    
    # 默认为繁体中文转简体中文
    # opposite 简体中文转繁体中文
    parser.add_argument('--op',action='store_true')
    args = parser.parse_args()
    
    
    for file_name in args.file_name:
        
        print('----------------------')
        print(f'start converting file {file_name}')
        file = open(file_name,'r',encoding='utf-8')
        contents = file.readlines()
        
        target_file_name = 'T'+file_name
        target_file = open(target_file_name,'w',encoding='utf-8')
        
        for content in contents:
            if args.op:
                target_content = SimplifiedToTraditional(content)
            else:
                target_content = TraditionalToSimplified(content)
            target_file.write(target_content)
        
        target_file.close()
        print(f'finish converting')
        print('----------------------')
        