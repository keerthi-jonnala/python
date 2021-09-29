import requests
import urllib3
import json
from bs4 import BeautifulSoup
import lxml
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

r=requests.get("https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_pg_1?ie=UTF8&pg=1")
print(r.status_code)
soup=BeautifulSoup(r.text,'lxml')
soup.prettify()
def get_books():
    books=[]
    x=soup.find_all("div",class_="p13n-sc-truncate p13n-sc-line-clamp-1")
    for i in x:
        books.append(i.text.strip("\n").strip(" ").replace("\n",""))
    print("books",len(books))

    return books
def get_rating():
    ratings=[]
    x1=soup.find_all("span",{"class":"a-icon-alt"})
    for i1 in x1:
        ratings.append(i1.text)
    print("ratings",len(ratings))

    return ratings
def get_no_of_people_rated():
    no_of_people_rated=[]
    x2=soup.find_all("a",class_="a-size-small a-link-normal")
    for i2 in x2:
        no_of_people_rated.append(i2.text)
    print("no_of_people_rated",len(no_of_people_rated))
    return no_of_people_rated
def get_price():
    price=[]
    x3=soup.find_all("span",class_="p13n-sc-price")
    for i3 in x3:
        price.append(i3.text.replace("\u20b9",""))

    print("price",len(price))
    return price
def get_authors():
    authors=[]
    x4=soup.find_all("a",class_="a-size-small a-link-child")
    for i4 in x4:
        authors.append(i4.text)
    x41=soup.find_all("span",class_="a-size-small a-color-base")
    for i41 in x41:
        authors.append(i41.text)
    print("autors",len(authors))
    return authors

if r.status_code!=200:
    print("service might be busy, try again")
else:
    b=get_books()
    r=get_rating()
    g=get_no_of_people_rated()
    p=get_price()
    a=get_authors()
    dict={"Books":b,"Price":p,"Authors":a}
    df=pd.DataFrame(dict)
    print(df.head())
    z=df.head(3)
    k=df.groupby("Price")
    df["Price"]=pd.to_numeric(df["Price"])
    d=df[df["Price"]>=100]
    n=d["Books"].count()
    f1=df[df["Price"]<100]
    m=f1["Books"].count()

    print("no_of_booksless than 100 are {}".format(m))
    print("no_of_books greater than 100 are {}".format(n))

    l1=[n,m]
    my_labels=["no.of books greater than rs.100","no_of_books less than rs.100"]
   
    plt.title("pie chart")
    plt.pie(l1,shadow=True,colors=["Blue","Cyan"],labels=my_labels,explode=[0.2,0])
   
    plt.show()
