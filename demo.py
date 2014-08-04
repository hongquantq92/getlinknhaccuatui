# -*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup as bs
import re
from requests import session
import sys
from threading import Thread
import time
import random
import json
import urllib
import requests
import os
check_run=0
randomlist= [{}]
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
max=10000
def highlow(text):
    
    print text

def getss(payload,url):
    proxies=random.choice(randomlist)
    #highlow(requests.get('https://m.facebook.com', verify=False).text) 
    with session() as c:
        c.get('https://m.facebook.com/', verify=False,proxies=proxies,timeout=5)
        #highlow(str(c))
        c.post(url, data=payload, verify=False,proxies=proxies,timeout=5)
        return c
def face(user,passw):
    proxies=random.choice(randomlist)
    urlpost='https://www.facebook.com/login.php?login_attempt=1'
    #highlow(urlpost)
    #highlow(user)
    #highlow(passw)
    sess=getss({'email':user,
                'pass':passw,
                'persistent':1,
                'default_persistent':1,
                'timezone':'-420',
                'locale':'en_US'}
                ,urlpost)
    title=str(bs(sess.get('https://m.facebook.com/me', verify=False,proxies=proxies,timeout=5).text).findAll('title')[0].text.encode('utf-8')) 
    highlow(title)
    if 'book' not in title:
        
        return sess
    else:
        
        return None
    
    '''import requests
    sess=face('hongquan190119913@gmail.com','meoconhocxuong92')'''
    #print sess.get('http://www.facebook.com/me').text

def like(sess,pageid,userid,token):
    proxies=random.choice(randomlist)
    try:
        payload={'fbpage_id':str(str(pageid).split('?')[0]),
        'add':'true',
        'reload':'false',
        'fan_origin':'page_timeline',
        '__user':int(userid),
        '__a':1,
        #'__dyn':'7n8a9EAMNpGudGh2u5KIGKaExEW9J6yUgByV4GFamiFo',
        '__req':'1l',
        'fb_dtsg':token,
        '__rev':'1058441',
        'ttstamp':'26581651211157111468'
        }
    except :
        highlow( 'error not id ')
    try:
        return sess.post('https://www.facebook.com/ajax/pages/fan_status.php',data=payload, proxies=proxies,verify=False,timeout=5).text
    except:
        return sess.post('https://www.facebook.com/ajax/pages/fan_status.php',data=payload, proxies=proxies,verify=False,timeout=5).text
def unlike(sess,pageid,userid,token):
    proxies=random.choice(randomlist)
    payload={'fbpage_id':pageid,
    'add':'false',
    'reload':'false',
    'fan_origin':'page_timeline',
    '__user':userid,
    '__a':1,
    '__req':'1l',
    'fb_dtsg':token,
    '__rev':'1058441',
    }
    return sess.post('https://www.facebook.com/ajax/pages/fan_status.php',data=payload, proxies=proxies,verify=False,timeout=5).text

def likephoto(sess,photoid,userid,token):
    proxies=random.choice(randomlist)
    payload={'like_action':'true',
            'ft_ent_identifier':photoid,
            'source':'2',
            #'client_id':'1388129338398:1790226072',
            #'rootid':'u_0_8',
            #'giftoccasion':'',
            #'ft[tn]':'>=',
           #' ft[type]':'20',
            '__user':userid,
            '__a':1,
            #'__dyn':'7n8apij35CFUSt2u5KIGKaExEW9ACxO4pbGAdGm',
            '__req':'9',
            'fb_dtsg':token,
            #'__rev':'1060814',
            #'ttstamp':'26581665010611610876'
            }
    return sess.post('https://www.facebook.com/ajax/ufi/like.php',data=payload,proxies=proxies, verify=False,timeout=5).text
def unlikephoto(sess,photoid,userid,token):
    proxies=random.choice(randomlist)
    payload={'like_action':'false',
            'ft_ent_identifier':photoid,
            'source':'2',
            #'client_id':'1388129338398:1790226072',
            #'rootid':'u_0_8',
            #'giftoccasion':'',
            #'ft[tn]':'>=',
           #' ft[type]':'20',
            '__user':userid,
            '__a':1,
            #'__dyn':'7n8apij35CFUSt2u5KIGKaExEW9ACxO4pbGAdGm',
            '__req':'9',
            'fb_dtsg':token,
            #'__rev':'1060814',
            #'ttstamp':'26581665010611610876'
            }
    return sess.post('https://www.facebook.com/ajax/ufi/like.php',data=payload, proxies=proxies,verify=False,timeout=5).text

def follow(sess,profile_id,userid,token):#
    proxies=random.choice(randomlist)
    payload={'profile_id':profile_id,
             'location':1,
             'feed_blacklist_action':'show_followee_on_follow',
             '__user':userid,
             '__a':1,
             '__req':'3v',
             'fb_dtsg':token
             }
    try:
        return sess.post('https://www.facebook.com/ajax/follow/follow_profile.php',data=payload, proxies=proxies,verify=False,timeout=5).text
    except:
        time.sleep(3)
        return sess.post('https://www.facebook.com/ajax/follow/follow_profile.php',data=payload, proxies=proxies,verify=False,timeout=5).text
def unfollow(sess,profile_id,userid,token):#
    proxies=random.choice(randomlist)
    payload={'profile_id':profile_id,
             'location':1,
             'feed_blacklist_action':'hide_followee_on_unfollow',
             '__user':userid,
             '__a':1,
             '__req':'3v',
             'fb_dtsg':token
             }
    return sess.post('https://www.facebook.com/ajax/follow/unfollow_profile.php',data=payload, proxies=proxies,verify=False,timeout=5).text
def get_token(sess):
    proxies=random.choice(randomlist)
    html12=sess.get('https://www.facebook.com/', verify=False).text.encode('utf-8')
    token=str(re.search('name="fb_dtsg" value="(.*?)"',str(html12)).group(1))
    return token
def accept_friend(sess,id_friend,id_profile,token):
    proxies=random.choice(randomlist)
    data={'fb_dtsg':token,
        'confirm':id_friend,
        'type':'friend_connect',
        'request_id':id_friend,
        'list_item_id':str(id_friend)+'_1_req',
        'status_div_id':str(id_friend)+'_1_req_status',
        'inline':1,
        'ref':'jewel',
        'actions[accept]':'Confirm',
        'nctr[_mod]':'pagelet_bluebar',
        '__user':id_profile,
        '__a':1,
        '__req':'3v',
          }
    return sess.post('https://www.facebook.com/ajax/reqs.php',data,proxies=proxies, verify=False,timeout=5)
def return_access_token(sess):
    proxies=random.choice(randomlist)
    text=sess.get('https://developers.facebook.com/tools/explorer/', proxies=proxies,verify=False,timeout=5).text
    id_app=str(re.findall('name="app_id" value="(\d+)\|0"',str(text))[0])

    id_profile=str(myid(sess))
    
    html= sess.get('''https://developers.facebook.com/tools/explorer/'''+id_app+'''/permissions?__asyncDialog=7&__user='''+id_profile+'''&__a=1&__req=c&__rev=1132776''', verify=False,timeout=5).text
    #print html
    token= re.findall('"([a-z_A-Z_0-9]{40,600})"',str(html))[0]
    #print token
    return token
def accept_all_friend(sess):
    id_profile=str(myid(sess))
    token=get_token(sess)
    access_token=return_access_token(sess)
    url='https://graph.facebook.com/'+id_profile+'?fields=friendrequests.limit(300)&method=GET&format=json&suppress_http_code=1&access_token='+str(access_token)
    html=sess.get(url, verify=False).text
    count=0
    for i in json.loads(str(html))['friendrequests']['data']:
        time.sleep(random.randrange(1,3))
        id_friend= str(i['from']['id'])
        accept_friend(sess,id_friend,id_profile,token)
        count+=1
    return count

urlpost='http://addmefast.com/includes/ajax.php'
headers = {'User-Agent': 'Mozilla/5.0',
           'X-Requested-With':'XMLHttpRequest'}


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
def rand():
    return 0
def myid(sess):
    proxies=random.choice(randomlist)
    url=sess.get('https://www.facebook.com/me', verify=False,proxies=proxies,timeout=5).url

    data= requests.get('http://graph.facebook.com/'+str(url).split('/')[-1], verify=False,proxies=proxies,timeout=5).text.encode('utf-8')
    #print data
    getid=json.loads(str(data))['id']
    #print getid
    return getid
def id_any(url):
    proxies=random.choice(randomlist)
    try:
        data= requests.get('http://graph.facebook.com/'+str(url), proxies=proxies,verify=False,timeout=5).text
        getid=json.loads(str(data))['id']
        #print getid
        return getid
    except:
        return url
def getssadd(payload,url):
        proxies=random.choice(randomlist)
    
        with session() as c:
            c.get('http://addmefast.com/', proxies=proxies,timeout=5)
            #c.proxies=proxies
            c.post(url, data=payload, timeout=5,proxies=proxies,headers=headers)
            return c
def addmelogin(email,passw):
    proxies=random.choice(randomlist)
    urlpost='http://addmefast.com/'
    sessadd=getssadd({'email':email,'password':passw,'login_button':'Login'},urlpost)
    sessadd.get('http://addmefast.com/free_points',proxies=proxies,headers=headers,timeout=5).text
    highlow( 'login succes addmefast !!!')
    return sessadd

def add(sess,facebook,my_id,token):
    proxies=random.choice(randomlist)
    
    quay=0
    highlow('run process like page !')
    while quay<=10:
        try:
            quay+=1
            time.sleep(random.uniform(3,6))
            html= sess.post(urlpost,data={'act':'getLinksList','params':'{"network":"1", "page":"'+str(random.randint(1,5))+'"}'},headers=headers,proxies=proxies,timeout=5).text.encode('utf-8')
            #print html
            number=re.search('class="fs18">(.*?)<',str(html)).group(1)
            highlow( str(number))
            number=re.findall('get (\d+) points',number)[0]
            if int(number) >2:
                for i in bs(html).findAll('div',{'class':True,'title':True,'id':True}):
                    #print i
                    url= i['title'].encode('utf-8')
                    id= i['id']
                    title1=re.search('<div class="freepts_row" title="(.*?)"',str(html)).group(1)
                    openw=re.search("window.open\('(.*?)'",str(html)).group(1)
                    if 'slow_down.html' in str(openw):
                        time.sleep(2000)
                    id=str(id).replace('L_', '')
                    xt= str(re.search('if\(i <= 25\){\s*(.*?)\s*}\s*else\s*\{',str(html)).group(1)).split('"')[-6]
                    xt= urllib.unquote(xt).decode('utf8') 
                    in_site= str(re.search('FBL_(\d+).closed',str(html)).group(1))
                    sess.post(urlpost,data={'act':'getFBLikesDataBefore','params':'{"id":"'+str(in_site.encode('utf-8'))+'", "url":"'+str(url)+'", "network":"1"}'}, timeout=5,proxies=proxies,headers=headers).text
                    status=  str(sess.get('http://addmefast.com'+openw, verify=False,proxies=proxies,timeout=5).status_code)
                        
                    idpage=id_any(str(title1).split('/')[-1])
                    #highlow( idpage)
                    like(facebook, idpage,my_id ,token)
                    check_out=0
                    try:
                        highlow( 'like sussec')
                        time.sleep(random.uniform(2,4))
                        p1= sess.post(urlpost,data={'act':'checkFollowed','params':'{"id":"'+str(in_site.encode('utf-8'))+'", "url":"'+str(url)+'", "network":"1"}'}, timeout=5,proxies=proxies,headers=headers).text
                        #highlow( p1)
                        if '1' in str(p1):
                            p2= sess.post(urlpost,data={'act':'updateAction','params':'{"link_id":"'+id+'", "url":"'+str(url)+'", "network":"1", "IXY5pZpE":"'+str(xt)+'"}'}, timeout=5,proxies=proxies,headers=headers)
                            #highlow( p2.text)
                            if int(p2.text.encode('utf-8')) > max:
                                #highlow( 'out with 6000 point')
                                check_out=1
                                sys.exit()
                            plai=sess.post(urlpost,data={'act':'getLikeNote','params':'{"m":"1", "cpc":"'+str(number)+'", "network":"1", "title":"'+str(title1)+'"}'},proxies=proxies,headers=headers,timeout=5)
                            #highlow( 'response for me '+bs(str(plai.text.encode('utf-8'))).text)
                           
                    except:
                        pass
                    unlike(facebook, idpage,my_id ,token)
                    if check_out==1:
                        sys.exit()
        except :
            highlow( 'error postlike ')
            proxies=random.choice(randomlist)
     
def addpostlike(sess,facebook,my_id,token):
    proxies=random.choice(randomlist)
    quay=0
    highlow('run process like photo !')
    while quay<=10:
        try:
            quay+=1
            time.sleep(random.uniform(3,7))
            html= sess.post(urlpost,data={'act':'getLinksList','params':'{"network":"25", "page":"'+str(random.randint(1,5))+'"}'}, timeout=5 ,proxies=proxies,headers=headers).text.encode('utf-8')
            #print html
            number=re.search('class="fs18">(.*?)<',str(html)).group(1)
         
            number=re.findall('get (\d+) points',number)[0]
            if 1:
                for i in bs(html).findAll('div',{'class':True,'title':True,'id':True}):
                    #print i
                    url= i['title'].encode('utf-8')
                    id= i['id']
                title1=re.search('<div class="freepts_row" title="(.*?)"',str(html)).group(1)
                openw=re.search("window.open\('(.*?)'",str(html)).group(1)
                if 'slow_down.html' in str(openw):
                    time.sleep(2000)
                id=str(id).replace('L_', '')
                xt= str(re.search('if\(i <= 25\){\s*(.*?)\s*}\s*else\s*\{',str(html)).group(1)).split('"')[-6]
                xt= urllib.unquote(xt).decode('utf8') 
                in_site= str(re.search('FBL_(\d+).closed',str(html)).group(1))
                #begin
                sess.post(urlpost,{'act':'getFBLikesDataBefore','params':'{"id":"'+str(in_site)+'", "url":"'+str(url)+'", "network":"25"}'}, timeout=5 ,proxies=proxies,headers=headers).text
                
                status= str(sess.get('http://addmefast.com'+openw, timeout=5 ,proxies=proxies,headers=headers, verify=False).status_code)
               
                idpost=str(url).split('/')[-1]
                #highlow( idpost)
                likephoto(facebook, idpost,my_id ,token)
                highlow( 'postlike sussec')
                check_out=0
                try:
                    time.sleep(random.uniform(2,4))
                    if '1' in  str(sess.post(urlpost,{'act':'checkFollowed','params':'{"id":"'+str(in_site)+'", "url":"'+str(url)+'", "network":"25"}'}, timeout=5 ,proxies=proxies,headers=headers).text.encode('utf-8')):
                        highlow( '1')
                        p2= sess.post(urlpost,{'act':'updateAction','params':'{"link_id":"'+id+'", "url":"'+str(url)+'", "network":"25", "IXY5pZpE":"'+str(xt)+'"}'}, timeout=6 ,proxies=proxies,headers=headers)
                        highlow( p2.text)
                        if int(p2.text.encode('utf-8')) > max:
                            highlow( 'out with 6000 point')
                            check_out=1
                        plai=sess.post(urlpost,{'act':'getLikeNote','params':'{"m":"1", "cpc":"'+str(number)+'", "network":"25", "title":"'+str(title1)+'"}'},proxies=proxies,timeout=5)
                        #highlow( bs(str(plai.text)).text)
                        
                except:
                    pass
                unlikephoto(facebook, idpost,my_id ,token)
                if check_out==1:
                    sys.exit()
                highlow( 'unpostlike sussec')
        except :
            highlow( 'error postlike ')
            proxies=random.choice(randomlist)
  
def follow1(sess,facebook,my_id,token):
    #print arg1
    proxies=random.choice(randomlist)
    quay=0
    highlow('run process follow !')
    while quay<=10:
        
        quay+=1
        time.sleep(random.uniform(4,7))

        html= sess.post(urlpost,{'act':'getLinksList','params':'{"network":"11", "page":"'+str(random.randint(1,5))+'"}'}, timeout=5 ,proxies=proxies,headers=headers).text.encode('utf-8')
        #print html
        number=re.search('class="fs18">(.*?)<',str(html)).group(1)
        #highlow('run process follow !')
        number=re.findall('get (\d+) points',number)[0]
        highlow(str(number))
        if int(number) >2:
            for i in bs(html).findAll('div',{'class':True,'title':True,'id':True}):
                #print i
                url= i['title'].encode('utf-8')
                id= i['id']
            title1=re.search('<div class="freepts_row" title="(.*?)"',str(html)).group(1)
            #highlow(str(title1))
            openw=re.search("window.open\('(.*?)'",str(html)).group(1)
            if 'slow_down.html' in str(openw):
                time.sleep(2000)
            id=str(id).replace('L_', '')
            #highlow(str(id))
            xt= str(re.search('if\(i <= 25\){\s*(.*?)\s*}\s*else\s*\{',str(html)).group(1)).split('"')[-6]
            xt= urllib.unquote(xt).decode('utf8') 
            in_site= str(re.search('FBL_(\d+).closed',str(html)).group(1))
            #highlow('begin')
            sess.post(urlpost,{'act':'getFBLikesDataBefore','params':'{"id":"'+str(in_site)+'", "url":"'+str(url)+'", "network":"11"}'}, timeout=6 ,proxies=proxies,headers=headers).text
            #highlow(  'follow sussec')
            status= str(sess.get('http://addmefast.com'+openw, timeout=6 ,proxies=proxies,headers=headers, verify=False).status_code)
        
        
            #highlow( status)
            idpage=id_any(str(title1).split('/')[-1])
            follow(facebook, idpage,my_id ,token)
            #highlow(  'follow sussec')
            time.sleep(random.uniform(2,4))
            check_out=0
            checkFollowed=str(sess.post(urlpost,{'act':'checkFollowed','params':'{"id":"'+str(in_site)+'", "url":"'+str(url)+'", "network":"11"}'}, timeout=5 ,proxies=proxies,headers=headers).text.encode('utf-8'))
            if 1:
                if '' in checkFollowed:
                    highlow(  '1')
                    p2= sess.post(urlpost,{'act':'updateAction','params':'{"link_id":"'+id+'", "url":"'+str(url)+'", "network":"11", "IXY5pZpE":"'+str(xt)+'"}'}, timeout=5 ,proxies=proxies,headers=headers)
                    #highlow(  p2.text+'  number')
                    if int(p2.text.encode('utf-8')) > max:
                        highlow(  'out with 6000 point')
                        check_out=1
                        
                    plai=sess.post(urlpost,{'act':'getLikeNote','params':'{"m":"1", "cpc":"'+str(number)+'", "network":"11", "title":"'+str(title1)+'"}'} ,proxies=proxies,headers=headers,timeout=5)
                    highlow( p2.text.encode('utf-8'))
            
                
            unfollow(facebook, idpage,my_id ,token)
            if check_out==1:
         
                sys.exit()
                
            highlow(  'unfollow sussec')
def running(account,account_add):
    while True:
        try:
            proxies=random.choice(randomlist)
            print 'run'
            facebook=face(str(account[0]['email']), str(account[0]['passw']))
            if facebook:
                pass
            else:
                highlow('login face error .exit and login again')
                time.sleep(7)
                sys.exit()
            highlow(  'login face')
            sess=addmelogin(account_add[0]['email'],account_add[0]['passw'])
            html_getpoint=sess.get('http://addmefast.com/free_points' ,proxies=proxies,headers=headers,timeout=5).text
            
            point_get_check='#'
            for i1 in bs(html_getpoint).findAll('span',{'class':"points_count"}):
                highlow(  'point is : '+str(i1.text))
                point_get_check=int(str(i1.text))
                if int(str(i1.text))> max:
                    highlow(  'point is max ')
                    time.sleep(7)
                    sys.exit()
            if point_get_check=='#':
                highlow('error login addmefast please check in')
                sys.exit()
            
            if facebook:
                html12=facebook.get('https://www.facebook.com/me' , verify=False,proxies=proxies,timeout=5).text.encode('utf-8')
                token=str(re.search('name="fb_dtsg" value="(.*?)"',str(html12)).group(1))
                my_id=myid(facebook)
                j,cj=0,1
                for i in range(1,10000):
                    j+=1
                    if j==30:
                        sess=addmelogin(account_add[0]['email'],account_add[0]['passw'])
                        facebook=face(str(account[0]['email']), str(account[0]['passw']))
                        if facebook:
                            html12=facebook.get('https://www.facebook.com/me' , verify=False,timeout=5).text.encode('utf-8')
                            token=str(re.search('name="fb_dtsg" value="(.*?)"',str(html12)).group(1))
                            my_id=myid(facebook)
                            j=0
                        else:
                            highlow( 'Facebook error . check facebook on brower and exits program')
                            time.sleep(7)
                            sys.exit()
                    print 'den day'
                  
                    processes = []
                    for tj in range(0,1):
                        processes.append( ThreadWithReturnValue(target=follow1, args=(sess,facebook,my_id,token,), name='add') )
                        processes.append( ThreadWithReturnValue(target=add, args=(sess,facebook,my_id,token,), name='add') )
                        processes.append( ThreadWithReturnValue(target=addpostlike, args=(sess,facebook,my_id,token,), name='add') )
                    for p in processes:
                        p.start()
                    for p in processes:
                        p.join()
                    
                    check_point=bs(sess.get('http://addmefast.com/my_sites.html' ,proxies=proxies,headers=headers,timeout=5).text.encode('utf-8')).findAll('span',{'class':"points_count"})
                    if len(check_point)==0:
                        sess=addmelogin(account_add[0]['email'],account_add[0]['passw'])
                    for i1 in check_point:
                        highlow( 'point is : '+str(i1.text))
                        if int(str(i1.text.encode('utf-8'))) >max:
                            highlow( 'point is max')
                            time.sleep(120)
                            sys.exit()
                        else:
                            time.sleep(random.uniform(10,20))
            else:
                highlow( 'Facebook error . check facebook on brower ')
        except Exception ,e:
            print Exception, e
            time.sleep(10)
    

def exit_program():
    time.sleep(7)
    sys.exit()
account=[#{'email':'nguyenhongquan3a1@gmail.com','passw':'190192'},
                #{'email':'hongquan190119913@gmail.com','passw':'meoconhocxuong92'},
                {'email':'hongquan190119913@gmail.com','passw':'meoconhocxuong92'}]
account_add=[{'email':'quyet862019@gmail.com','passw':'hongquantq92'}]
running( account,account_add)
  
