# -*- coding:utf-8 -*-
import urllib2
import re
import gzip
import StringIO
agent = 'Mozilla/5.0 (X11; Linux x86_64)'
headers = { 'User-Agent' : agent}
print "welcome to youdao translation spider"
while True:
    print "input a word:"
    i = raw_input()
    url ="http://dict.youdao.com/search?q="+i+"&keyfrom=fanyi.smartResult"
    try:
        print "------------translation result-------------"
        request = urllib2.Request(url,headers=headers)
        request.add_header('Accept-encoding', 'gzip')
        opener=urllib2.build_opener()
        response = opener.open(request)
        htmldata = response.read()
        htmlstream = StringIO.StringIO(htmldata)
        html=gzip.GzipFile(fileobj=htmlstream).read()
        #pattern is to locate where translation and pronunciation is
        pattern=re.compile(r'''<h2 class="wordbook-js">(.*?)</ul>.*?</div>.*?</div>''',re.S)
        result = pattern.search(html)
        if result :
            content = result.group(0).decode('utf-8')
        #pattern1 is to find pronunciation
        pattern1=re.compile(r'''<span class="phonetic">(.*?)</span>''')
        pron=pattern1.findall(content)
        #pattern2 is to find translation
        pattern2 = re.compile('<li>(.*?)</li>')
        trans=pattern2.findall(content)
        length = len(pron)
        if length == 2:
            print u'英:'+pron[0]
            print u'美:'+pron[1]
        elif length==1:
            print u'发音:'+pron.pop()
        if len(trans) != 8:
            for t in trans:
                 print t
        print "-------------------------------------------\n"
    except urllib2.HTTPError,e:
        if hasattr(e,'code'):
            print e.code()
        if hasattr(e,'raeson'):
            print e.reason()
    except urllib2.URLError,e:
        if hasattr(e,'code'):
            print e.code()
        if hasattr(e,'reason'):
            print e.reason()
    except:
        continue
