import requests   
import webbrowser
import bs4
from googlesearch import search
link=input("Enter the google form URL here:\n")
res = requests.get(link) 
noStarchSoup = bs4.BeautifulSoup(res.text,"html.parser")   
elems = noStarchSoup.select('div .freebirdFormviewerComponentsQuestionBaseTitle') 
j=1
print("------------------------------------------------\n--------------LINKS FOR YOU LAZY----------------")
for i in elems:
    print("------------------------------------------------")
    # desktop user-agent
    for url in search(i.getText()[:-1], tld='com', stop=1):
        print("Q",j,")",i.getText()[:-1],"\n\nLink:",url)
        j=j+1
print("------------------------------------------------")
while(True):
    alternate=input("you might have issue with some quesitons first link, type in the quesiton number for second and third link of it's answers\n")
    j=0
    print("Q )",str(elems[int(alternate)-1].getText())[:-1])
    for url in search(str(elems[int(alternate)-1].getText())[:-1], tld='com', stop=3):
        if(j!=0):
            print("\n Link",j+1,":",url)
        j=j+1
    print("------------------------------------------------")
    choice=input("Do you need extra links for any more questions? Enter Y or y as yes and N as NOoooo\n")
    if(choice!="y" and choice!="Y"):
        break
print("::::::::::::::: Thanks For using :::::::::::::")
