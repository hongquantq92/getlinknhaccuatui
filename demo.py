#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re 
import sys
import threading
from threading import Thread
import math
import random
import requests
import time
class ThreadWithReturnValue(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs, Verbose)
        self._return = None
    def run(self):
        if self._Thread__target is not None:
            self._return = self._Thread__target(*self._Thread__args,
                                                **self._Thread__kwargs)
    def join(self):
        Thread.join(self)
        return self._return
url='https://mp3.zing.vn/'
def add(url):
    time.sleep(random.random())
    print requests.get('http://50k.itcenter.vn/website-SEO-Internet/7463/b%C3%A1n-account-mua-ban-like-10k-coin-tr%E1%BB%9F-l%C3%AAn-cho-ai-c%C3%B3-nhu-c%E1%BA%A7u-t%C4%83ng')
    time.sleep(random.random())
    print requests.get('http://50k.itcenter.vn/Marketing-Quang-cao/7530/C%C3%A0y-%C4%91i%E1%BB%83m-tr%C3%AAn-addmefast-12000-point-nhanh-ch%C3%B3ng-kh%C3%B4ng-b%E1%BB%8B-block')
    time.sleep(random.random())
    
    print requests.get('http://50k.itcenter.vn/website-SEO-Internet/7403/%C4%91%C4%83ng-%E1%BA%A3nh-theo-ch%E1%BB%A7-%C4%91%E1%BB%81-l%C3%AAn-Facebook-page-c%E1%BB%A7a-b%E1%BA%A1n-v%E1%BB%9Bi-gi%C3%A1-50000-VN%C4%90-hay')
    
    
t=1
while t<100000:
    processes = []
    for i in range(1,15):
        if t<10000:
            processes.append(ThreadWithReturnValue(target=add, args=(url,), name='addstring'))
            t+=1
        else:
            break
    print 'so thread '+str(len(processes))
    for p in processes:
        p.start()
    for p in processes:
        p.join()
