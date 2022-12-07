from bs4 import BeautifulSoup
import requests
import pandas as Pd

url_scrape ="https://books.toscrape.com/catalogue/category/books_1/page-1.html"

response = requests.get(url_scrape)

## Fetch to check status code
def getbookinfo():
   
    if (response.status_code == 200):
        print('Status Code:',response.status_code)
    else:
        print('Failed to fetch web page !!!')
getbookinfo()


doc = BeautifulSoup(response.content,'html.parser')

##Fetch to web page Book List
book_list=[]
for x in doc.find_all("h3"):
    book_list.append((x.a['title']))

##Fetch to Web page Book Rating
rating =[]
for x in doc.find_all('article'):
    rating.append(x.p['class'][1])

##Fetch to Web page Book Price
price =[]
for x in doc.find_all('p',{"class":"price_color"}):
    price.append(x.get_text())

##Fetch to Web page Book Link
links =[]
for x in doc.find_all("h3"):
    links.append(x.a['href'])

## fetch to get the result csv format
data = {'Book_Name':book_list,'Rating':rating,'Price_Tag':price,'Url_links':links}
Book_data = Pd.DataFrame(data)
Book_data.to_csv('Book_list.csv',sep=',',index=False)




   