# https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python

'''
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"

'''

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
