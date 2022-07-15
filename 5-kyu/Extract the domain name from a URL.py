# https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python

# 1
def domain_name(url):
    return url.split("://")[-1].split(".")[-2]

# 2
def domain_name(url):
    
   if ("www" not in url): return url.split("//")[1].split(".")[0]
   else: return url.split(".")[1]

# 3
def domain_name(url):
    url = url.replace('www.','')
    url = url.replace('https://','')
    url = url.replace('http://','')
    
    return url[0:url.find('.')]
