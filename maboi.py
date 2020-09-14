import requests   
import webbrowser
import bs4
form_link = input("Enter the link for google form: ")
try:
    res = requests.get(form_link)
except requests.exceptions.RequestException as e:
    raise SystemExit(e)
noStarchSoup = bs4.BeautifulSoup(res.text,"html.parser")                                  
elems = noStarchSoup.select('div .freebirdFormviewerComponentsQuestionBaseTitle') 
for i in elems:
    res = requests.get('http://google.com/search?q=' + (i.getText()[:-1]))
    #webbrowser.open('http://google.com/search?q=' + (i.getText()[:-1]))
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text,"html.parser")
    linkElems = soup.select(".r a")
    print(len(linkElems))
    #webbrowser.open('http://google.com' + (linkElems[0].get('href')))
