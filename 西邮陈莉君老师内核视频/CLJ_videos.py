 
#! -*- coding:utf-8 -*-
import datetime
import time

import pymysql
import requests
from lxml import etree
from selenium import webdriver
import os
import re
import urllib
import wget



def get_first_page(url):

    driver.get(url)
    time.sleep(6)
    # 增加点击的动作  //*[@id="movieplay"]/div[1]/div/div[2]/div[3]/span[1]/a
    driver.find_element_by_xpath('//*[@id="movieplay"]/div[1]/div/div[2]/div[3]/span[1]/a').click()
    html = driver.page_source
    return html




if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome("/usr/bin/chromedriver", chrome_options=options)
    num_l =["/video/22555","/video/22556","/video/22557","/video/22558","/video/22559","/video/22560","/video/22561","/video/22562","/video/22563","/video/22564","/video/22565","/video/22566","/video/22567","/video/22568","/video/22569","/video/22570","/video/22571","/video/22572","/video/22573","/video/22574","/video/22575","/video/22576","/video/22577","/video/22578","/video/22579","/video/22580","/video/22581","/video/22582","/video/22583","/video/22584","/video/22585","/video/22586","/video/22587","/video/22588","/video/22589","/video/22590","/video/22591","/video/22592","/video/22593","/video/22594","/video/22595","/video/22596","/video/22597","/video/22598","/video/22599","/video/22600","/video/22601","/video/22602","/video/22603","/video/22604"]
    title_l =["课时1：Linux 操作系统概述","课时2：Linux内核结构以及内核模块编程","课时3：Linux内核源码中的双链表结构","课时4：源码分析-内核中的哈希表","课时5：动手实践-Linux内核模块的插入和删除","课时6：内存管理之内存寻址","课时7：段机制","课时8：分页机制","课时9：动手实践-把虚拟地址转换成物理地址","课时10：进程概述","课时11：Linux进程创建","课时12：Linux进程调度","课时13：动手实践-打印进程描述符task_struct中的字段","课时14：工程实践-基于内核模块的负载监控","课时15：Linux内存管理机制","课时16：进程用户空间管理机制","课时17：物理内存分配与回收机制（上）","课时18：物理内存分配与回收机制（下）","课时19：动手实践-Linux内存映射基础（上）","课时20：动手实践-Linux内存映射实现（中）","课时21：动手实践-Linux内存映射测试（下）","课时22：中断机制概述","课时23：中断处理机制","课时24：中断下半部处理机制","课时25：时钟中断机制","课时26：动手实践-中断上半部的代码分析及应用","课时27：动手实践-中断下半部的代码分析及应用","课时28：Linux中的各种API","课时29：系统调用机制","课时30：动手实践-添加系统调用（系统调用日志收集系统）","课时31：内核同步概述","课时32：内核同步机制","课时33：动手实践-内核多任务并发实例（上）","课时34：动手实践-内核多任务并发实例（下）","课时35：虚拟文件系统的引入","课时36：虚拟文件系统的主要数据结构","课时37：文件系统中的各种缓存","课时38：页高速缓存机制以及读写","课时39：动手实践-编写一个文件系统（上）","课时40：动手实践-编写一个文件系统（中）","课时41：动手实践-编写一个文件系统（下）","课时42：设备驱动概述","课时43：IO空间管理","课时44：设备驱动模型","课时45：字符设备驱动程序简介","课时46：块设备驱动程序简介","课时47：动手实践-编写字符设备驱动程序","课时48：工程实践-编写块设备驱动的基础（上）","课时49：工程实践-块设备驱动程序分析（中）","课时50：工程实践-块设备驱动程序实现（下）"]
    f_dic = dict(zip(num_l,title_l))



    

    for item_dict in f_dic:
        # item  /video/22555"  f_dic[item_dict]  课时1：Linux 操作系统概述 
        f_url = 'http://training.eeworld.com.cn{0}'.format(item_dict)
        print(f_url)
        html = get_first_page(f_url)
        selector = etree.HTML(html)

        
        video_url = selector.xpath('//*[@id="lesson-preview-video-player"]/div[2]/video/@src')
        print(video_url)
        for item_url in video_url:
            n_path = os.getcwd()
            print(item_url)
            print(f_dic[item_dict])
    
  
                # urllib.request.urlretrieve(item_url[:-4], '{0}/{1}.mp4'.format(n_path,f_dic[item_dict]))
            out_filename = '{0}/{1}.mp4'.format(n_path,f_dic[item_dict])
            wget.download(item_url, out=out_filename)



