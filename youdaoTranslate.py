# -*- coding:utf-8 -*-
import urllib
import urllib2
import json
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=dict2.index"
meta = {}
meta["type"] = "AUTO"
meta["doctype"] = "json"
meta["xmlVersion"] = "1.8"
meta["keyfrom"] = "fanyi.web"
meta["ue"] = "UTF-8"
meta["typoResult"] = "true"
print "welcome to youdao translate spider"
while True:
    print "input a word:"
    i = raw_input()
    try:
        
        print "------------translation result-------------"
        meta["i"] = i
        data = urllib.urlencode(meta)
        request = urllib2.Request(url, data)
        response = urllib2.urlopen(request)
        content = response.read()
        target = json.loads(content)
        s = target["smartResult"]["entries"]
        for re in s:
            print re
        print "-----------------------------------------\n"
    except:
    	print "there is an error,plese check your input\n"
    	continue
