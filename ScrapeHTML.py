# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 17:53:07 2023

@author: Ammad
"""

from bs4 import BeautifulSoup
import requests
import os 
import json

import warnings
warnings.filterwarnings('ignore')

location = r'C:\Users\Ammad\Downloads\30-01-23 (ScrapeContentForML)'

# Storing the links of each website in a variable
link1 = 'https://snov.io/'
link2 = 'https://www.superlist.com/'
link3 = 'https://surferseo.com/'
link4 = 'https://www.clickcease.com/'

# Export the whole page content as an HTML file
def writeHTML(location, content, website):
    if not os.path.exists(path):
        os.makedirs(path)
        with open(path + '//' + website + '.html', 'w', encoding = 'utf-8') as f:
            f.write(str(content))
    else:
        with open(path + '//' + website + '.html', 'w', encoding = 'utf-8') as f:
            f.write(str(content))

# Convert the Meta Tags HTML into JSON
def getAllInfo_Meta(metaTag):
    metaInfo = {}
    try:
        metaInfo['charset'] = metaTag['charset']
    except:
        pass
    try:
        metaInfo['content'] = metaTag['content']
    except:
        pass
    try:
        metaInfo['name'] = metaTag['name']
    except:
        pass
    try:
        metaInfo['property'] = metaTag['property']
    except:
        pass
    try:
        metaInfo['itemprop'] = metaTag['itemprop']
    except:
        pass
    
    return metaInfo

# Convert the Link Tags HTML into JSON
def getAllInfo_Link(linkTag):
    linkInfo = {}
    try:
        linkInfo['href'] = linkTag['href']
    except:
        pass
    try:
        linkInfo['rel'] = linkTag['rel'][0]
    except:
        pass
    try:
        linkInfo['hreflang'] = linkTag['hreflang']
    except:
        pass
    try:
        linkInfo['itemprop'] = linkTag['itemprop']
    except:
        pass
    try:
        linkInfo['sizes'] = linkTag['sizes']
    except:
        pass
    try:
        linkInfo['type'] = linkTag['type']
    except:
        pass
    
    return linkInfo


# Convert the p Tags HTML into JSON
def getAllInfo_p(pTag):
    pInfo = {}
    try:
        pInfo['text'] = pTag.text
    except:
        pass
    try:
        pInfo['class'] = pTag['class'][0]
    except:
        pass
    
    return pInfo

# Convert the a Tags HTML into JSON
def getAllInfo_a(aTag):
    aInfo = {}
    try:
        aInfo['href'] = aTag['href']
    except:
        pass
    try:
        aInfo['class'] = aTag['class'][0]
    except:
        pass
    try:
        aInfo['id'] = aTag['id']
    except:
        pass
    
    # This will extract all the p-tags inside the a-tag as well
    try:
        pTags = aTag.find_all('p')
        pInfo = [getAllInfo_p(pTag) for pTag in pTags]
        aInfo['p'] = pInfo
    except:
        pass
    
    return aInfo

# Convert the div Tags HTML into JSON
def getAllInfo_div(divTag):
    divInfo = {}
    try:
        divInfo['itemscope'] = divTag['itemscope']
    except:
        pass
    try:
        divInfo['itemtype'] = divTag['itemtype']
    except:
        pass
    try:
        divInfo['class'] = divTag['class']
    except:
        pass
    
    # Get all the meta tags inside the div
    try:
        metaTags = divTag.find_all('meta')
        metaInfo = [getAllInfo_Meta(metaTag) for metaTag in metaTags]
        divInfo['meta'] = metaInfo
    except:
        pass
    # This will extract all the p-tags inside the div-tag as well
    try:
        pTags = divTag.find_all('p')
        pInfo = [getAllInfo_p(pTag) for pTag in pTags]
        divInfo['p'] = pInfo
    except:
        pass
    # This will extract all the a-tags inside the div-tag as well
    try:
        aTags = divTag.find_all('a')
        aInfo = [getAllInfo_a(aTag) for aTag in aTags]
        divInfo['a'] = aInfo
    except:
        pass
    # This will extract div within the div inside the main div-tag 
    try:
        divTags = divTag.find_all('div')
        divInsideInfo = [getAllInfo_div(divTag) for divTag in divTags]
        divInfo['div'] = divInsideInfo
    except:
        pass
    
    return divInfo

# =============================================================================
# =============================================================================
# # # Scraping Website 1 : SNOV.IO
# =============================================================================
# =============================================================================
path = location + '//snov'

page = requests.get(link1)
soup = BeautifulSoup(page.content, 'html.parser')

########################### Getting the HTML content
htmlContent = str(soup.prettify())

# Writing the HTML file
writeHTML(path, htmlContent, 'snovHTML')

########################### Getting the Meta Tags content
metaTags = soup.find_all('meta')

# Writing the Meta Tags as JSON file    
jsonMeta = [getAllInfo_Meta(metaTag) for metaTag in metaTags]
jsonMeta = {"meta": jsonMeta}

with open(path + "//snovMeta-Tag.json", "w") as file:
   json.dump(jsonMeta, file, indent = 2)
   
########################### Getting the Link Tags content
linkTags = soup.find_all('link')

# Writing the Link Tags as JSON file
jsonLink = [getAllInfo_Link(linkTag) for linkTag in linkTags]
jsonLink = {"link": jsonLink}

with open(path + "//snovLink-Tag.json", "w") as file:
    json.dump(jsonLink, file, indent = 2)
    
########################### Getting the p Tags content
pTags = soup.find_all('p')

# Writing the Link Tags as JSON file
jsonP = [getAllInfo_p(pTag) for pTag in pTags]
jsonP = {"p": jsonP}

with open(path + "//snovP-Tag.json", "w") as file:
    json.dump(jsonP, file, indent = 2)
    

########################### Getting the a Tags content
aTags = soup.find_all('a')

# Writing the Link Tags as JSON file
jsonA = [getAllInfo_a(aTag) for aTag in aTags]
jsonA = {"a": jsonA}

with open(path + "//snovA-Tag.json", "w") as file:
    json.dump(jsonA, file, indent = 2)
    
########################### Getting the Div Tags content
divTags = soup.find_all('div')

# Writing the Link Tags as JSON file
jsonDiv = [getAllInfo_div(divTag) for divTag in divTags]
jsonDiv = {"div": jsonDiv}

with open(path + "//snovHTML.json", "w") as file:
    json.dump(jsonDiv, file, indent = 2)


# =============================================================================
# =============================================================================
# # # Scraping Website 2 : SUPERLIST.COM
# =============================================================================
# =============================================================================
path = location + '//superlist'

page = requests.get(link2)
soup = BeautifulSoup(page.content, 'html.parser')

########################### Getting the HTML content
htmlContent = str(soup.prettify())

# Writing the HTML file
writeHTML(path, htmlContent, 'superlistHTML')

########################### Getting the Meta Tags content
metaTags = soup.find_all('meta')

# Writing the Meta Tags as JSON file    
jsonMeta = [getAllInfo_Meta(metaTag) for metaTag in metaTags]
jsonMeta = {"meta": jsonMeta}

with open(path + "//superlistMeta-Tag.json", "w") as file:
   json.dump(jsonMeta, file, indent = 2)
   
########################### Getting the Link Tags content
linkTags = soup.find_all('link')

# Writing the Link Tags as JSON file
jsonLink = [getAllInfo_Link(linkTag) for linkTag in linkTags]
jsonLink = {"link": jsonLink}

with open(path + "//superlistLink-Tag.json", "w") as file:
    json.dump(jsonLink, file, indent = 2)
    
########################### Getting the p Tags content
pTags = soup.find_all('p')

# Writing the Link Tags as JSON file
jsonP = [getAllInfo_p(pTag) for pTag in pTags]
jsonP = {"p": jsonP}

with open(path + "//superlistP-Tag.json", "w") as file:
    json.dump(jsonP, file, indent = 2)
    

########################### Getting the a Tags content
aTags = soup.find_all('a')

# Writing the Link Tags as JSON file
jsonA = [getAllInfo_a(aTag) for aTag in aTags]
jsonA = {"a": jsonA}

with open(path + "//superlistA-Tag.json", "w") as file:
    json.dump(jsonA, file, indent = 2)
    
########################### Getting the Div Tags content
divTags = soup.find_all('div')

# Writing the Link Tags as JSON file
jsonDiv = [getAllInfo_div(divTag) for divTag in divTags]
jsonDiv = {"div": jsonDiv}

with open(path + "//superlistHTML.json", "w") as file:
    json.dump(jsonDiv, file, indent = 2)
    

# =============================================================================
# =============================================================================
# # # Scraping Website 3 : SURFERSEO.COM
# =============================================================================
# =============================================================================
path = location + '//surferseo'

page = requests.get(link3)
soup = BeautifulSoup(page.content, 'html.parser')

########################### Getting the HTML content
htmlContent = str(soup.prettify())

# Writing the HTML file
writeHTML(path, htmlContent, 'surferseoHTML')

########################### Getting the Meta Tags content
metaTags = soup.find_all('meta')

# Writing the Meta Tags as JSON file    
jsonMeta = [getAllInfo_Meta(metaTag) for metaTag in metaTags]
jsonMeta = {"meta": jsonMeta}

with open(path + "//surferseoMeta-Tag.json", "w") as file:
   json.dump(jsonMeta, file, indent = 2)
   
########################### Getting the Link Tags content
linkTags = soup.find_all('link')

# Writing the Link Tags as JSON file
jsonLink = [getAllInfo_Link(linkTag) for linkTag in linkTags]
jsonLink = {"link": jsonLink}

with open(path + "//surferseoLink-Tag.json", "w") as file:
    json.dump(jsonLink, file, indent = 2)
    
########################### Getting the p Tags content
pTags = soup.find_all('p')

# Writing the Link Tags as JSON file
jsonP = [getAllInfo_p(pTag) for pTag in pTags]
jsonP = {"p": jsonP}

with open(path + "//surferseoP-Tag.json", "w") as file:
    json.dump(jsonP, file, indent = 2)
    

########################### Getting the a Tags content
aTags = soup.find_all('a')

# Writing the Link Tags as JSON file
jsonA = [getAllInfo_a(aTag) for aTag in aTags]
jsonA = {"a": jsonA}

with open(path + "//surferseoA-Tag.json", "w") as file:
    json.dump(jsonA, file, indent = 2)
    
########################### Getting the Div Tags content
divTags = soup.find_all('div')

# Writing the Link Tags as JSON file
jsonDiv = [getAllInfo_div(divTag) for divTag in divTags]
jsonDiv = {"div": jsonDiv}

with open(path + "//surferseoHTML.json", "w") as file:
    json.dump(jsonDiv, file, indent = 2)
    

# =============================================================================
# =============================================================================
# # # Scraping Website 4 : CLICKCEASE.COM
# =============================================================================
# =============================================================================
path = location + '//clickcease'

page = requests.get(link4)
soup = BeautifulSoup(page.content, 'html.parser')

########################### Getting the HTML content
htmlContent = str(soup.prettify())

# Writing the HTML file
writeHTML(path, htmlContent, 'clickceaseHTML')

########################### Getting the Meta Tags content
metaTags = soup.find_all('meta')

# Writing the Meta Tags as JSON file    
jsonMeta = [getAllInfo_Meta(metaTag) for metaTag in metaTags]
jsonMeta = {"meta": jsonMeta}

with open(path + "//clickceaseMeta-Tag.json", "w") as file:
   json.dump(jsonMeta, file, indent = 2)
   
########################### Getting the Link Tags content
linkTags = soup.find_all('link')

# Writing the Link Tags as JSON file
jsonLink = [getAllInfo_Link(linkTag) for linkTag in linkTags]
jsonLink = {"link": jsonLink}

with open(path + "//clickceaseLink-Tag.json", "w") as file:
    json.dump(jsonLink, file, indent = 2)
    
########################### Getting the p Tags content
pTags = soup.find_all('p')

# Writing the Link Tags as JSON file
jsonP = [getAllInfo_p(pTag) for pTag in pTags]
jsonP = {"p": jsonP}

with open(path + "//clickceaseP-Tag.json", "w") as file:
    json.dump(jsonP, file, indent = 2)
    

########################### Getting the a Tags content
aTags = soup.find_all('a')

# Writing the Link Tags as JSON file
jsonA = [getAllInfo_a(aTag) for aTag in aTags]
jsonA = {"a": jsonA}

with open(path + "//clickceaseA-Tag.json", "w") as file:
    json.dump(jsonA, file, indent = 2)
    
########################### Getting the Div Tags content
divTags = soup.find_all('div')

# Writing the Link Tags as JSON file
jsonDiv = [getAllInfo_div(divTag) for divTag in divTags]
jsonDiv = {"div": jsonDiv}

with open(path + "//clickceaseHTML.json", "w") as file:
    json.dump(jsonDiv, file, indent = 2)
    
