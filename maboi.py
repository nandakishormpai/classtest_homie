import requests   
import webbrowser
import bs4
res = requests.get('https://docs.google.com/forms/d/e/1FAIpQLSdmUGSzhsbT_w4x34DyVoOvCcnMsrWEjZwM_MCqIDWgC_tAAg/viewform?usp=sf_link') 
noStarchSoup = bs4.BeautifulSoup(res.text)                                  
elems = noStarchSoup.select('div .freebirdFormviewerComponentsQuestionBaseTitle') 
for i in elems:
    res = requests.get('http://google.com/search?q=' + (i.getText()[:-1]))
    #webbrowser.open('http://google.com/search?q=' + (i.getText()[:-1]))
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text)
    linkElems = soup.select('.r a')
    webbrowser.open('http://google.com' + (linkElems[0].get('href')))