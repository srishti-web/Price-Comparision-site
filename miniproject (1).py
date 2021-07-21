from tkinter import *                                                           # to use the 'original' widgets.
from tkinter import Scrollbar
from bs4 import BeautifulSoup                                                   #Python library for pulling data out of HTML and XML files.
import requests                                                                 #allows you to send HTTP requests using Python.
import webbrowser                                                               #allows to open the web browser from a python script By simply calling the open()

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


def flipkart(name = ""):
    try:
        global flipkart
        name1 = name.replace(" ","+")                                               #iphone x  -> iphone+x
        flipkart=f'https://www.flipkart.com/search?q={name1}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off'
        res = requests.get(f'https://www.flipkart.com/search?q={name1}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off',headers=headers)

        soup = BeautifulSoup(res.text,'html.parser')
        flipkart_name = soup.select('._4rR01T')[0].getText().strip()                # New Class For Product Name
        flipkart_name = flipkart_name.upper()
        if name.upper() in flipkart_name:
            flipkart_price = soup.select('._1_WHN1')[0].getText().strip()           # New Class For Product Price
            flipkart_name = soup.select('._4rR01T')[0].getText().strip()

            return f"{flipkart_name}\nPrice : {flipkart_price}\n"
        else:

            flipkart_price='Product Not Found'
            flipkart_price=0
        return flipkart_price
    except:

        flipkart_price= 'Product Not Found'
        #flipkart_price=0
    return flipkart_price

def amazon(name):
    try:
        global amazon
        name1 = name.replace(" ","-")
        name2 = name.replace(" ","+")
        amazon=f'https://www.amazon.in/{name1}/s?k={name2}'
        res = requests.get(f'https://www.amazon.in/{name1}/s?k={name2}',headers=headers)

        soup = BeautifulSoup(res.text,'html.parser')
        amazon_page = soup.select('.a-color-base.a-text-normal')
        amazon_page_length = int(len(amazon_page))
        for i in range(0,amazon_page_length):
            name = name.upper()
            amazon_name = soup.select('.a-color-base.a-text-normal')[i].getText().strip().upper()
            if name in amazon_name[0:20]:
                amazon_name= soup.select('.a-color-base.a-text-normal')[i].getText().strip().upper()
                amazon_price = soup.select('.a-price-whole')[i].getText().strip().upper()

                break
            else:
                i+=1
                i=int(i)
                if i==amazon_page_length:

                    amazon_price = '           Product Not Found'
                    amazon_price=0
                    break
        return f"{amazon_name}\nPrice : {amazon_price}\n"
    except:

        amazon_price = 'Product Not Found'
        #amazon_price=0
    return amazon_price

def olx(name):
    try:
        global olx
        name1 = name.replace(" ","-")
        olx=f'https://www.olx.in/items/q-{name1}?isSearchCall=true'
        res = requests.get(f'https://www.olx.in/items/q-{name1}?isSearchCall=true',headers=headers)

        soup = BeautifulSoup(res.text,'html.parser')
        olx_name = soup.select('._2tW1I')
        olx_page_length = len(olx_name)
        for i in range(0,olx_page_length):
            olx_name = soup.select('._2tW1I')[i].getText().strip()
            name = name.upper()
            olx_name = olx_name.upper()
            if name in olx_name:
                olx_price = soup.select('._89yzn')[i].getText().strip()
                olx_name = soup.select('._2tW1I')[i].getText().strip()
                olx_loc = soup.select('.tjgMj')[i].getText().strip()
                try:
                    label = soup.select('._2Vp0i span')[i].getText().strip()
                except:
                    label = "OLD"

                break
            else:
                i+=1
                i=int(i)
                if i==olx_page_length:

                    olx_price = '           Product Not Found'
                    olx_price=0
                    break
        return f"{olx_name}\nPrice : {olx_price}\n"
    except:

        olx_price = 'Product Not Found'
        olx_price=0
    return olx_price


def convert(a):
    b=a.replace(" ",'')
    c=b.replace("INR",'')
    d=c.replace(",",'')
    f=d.replace("₹",'')
    g=int(float(f))
    return g


def urls():
    global flipkart
    global amazon
    global olx
    return f"{flipkart}\n\n\n{amazon}\n\n\n{olx}"


def open_url(event):
        global flipkart
        global amazon
        global olx
        webbrowser.open_new(flipkart)
        webbrowser.open_new(amazon)
        webbrowser.open_new(olx)

def search():                                                       #search bar
    box1.insert(1.0,"Loding...")
    box2.insert(1.0,"Loding...")
    box3.insert(1.0,"Loding...")
    box4.insert(1.0, "Loding...")

    search_button.place_forget()


    box1.delete(1.0,"end")
    box2.delete(1.0,"end")
    box3.delete(1.0,"end")
    box4.delete(1.0,"end")

    t1=flipkart(product_name.get())
    box1.insert(1.0,t1)

    t2=amazon(product_name.get())
    box2.insert(1.0,t2)

    t3=olx(product_name.get())
    box3.insert(1.0,t3)

    t4=urls()
    box4.insert(1.0,t4)


window = Tk()
window.wm_title("E-Commerce sites Price Comparison")                                    #title
window.minsize(1500,700)

window.config(bg = "lavender")                                                         #background colour


lable_one =  Label(window, text="Enter Product Name :", font=("courier", 20))
lable_one.place(relx=0.2, rely=0.1, anchor="center")

product_name =  StringVar()
product_name_entry =  Entry(window, textvariable=product_name, width=50)
product_name_entry.place(relx=0.5, rely=0.1, anchor="center")


search_button =  Button(window, text="Search", width=12, command= search)
search_button.place(relx=0.5, rely=0.2, anchor="center")

l1 =  Label(window, text="FLIPKART", font=("courier", 20))
l2 =  Label(window, text="AMAZON", font=("courier", 20))
l3 =  Label(window, text="OLX", font=("courier", 20))
l4 =  Label(window, text="URLS", font=("courier", 20))
l5 =  Label(window, text="Loding.....", font=("courier", 30))


l1.place(relx=0.2, rely=0.3, anchor="center")
l2.place(relx=0.5, rely=0.3, anchor="center")
l3.place(relx=0.8, rely=0.3, anchor="center")
l4.place(relx=0.5, rely=0.6, anchor="center")

scrollbar = Scrollbar(window)
box1 =  Text(window, height=7, width=50, yscrollcommand=scrollbar.set)

box2 =  Text(window, height=7, width=50, yscrollcommand=scrollbar.set)

box3 =  Text(window, height=7, width=50, yscrollcommand=scrollbar.set)




box1.place(relx=0.2, rely=0.4, anchor="center")
box2.place(relx=0.5, rely=0.4, anchor="center")
box3.place(relx=0.8, rely=0.4, anchor="center")

box4 =  Text(window, height=7, width=80, yscrollcommand=scrollbar.set, fg="blue", cursor="hand2")
box4.place(relx=0.5, rely=0.7, anchor="center")
box4.bind("<Button-1>", open_url)

root=Tk()
window.mainloop()
