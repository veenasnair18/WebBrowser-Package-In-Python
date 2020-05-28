Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # A method that can be used to download IG posts
>>> import webbrowser as w
>>> pid=input("Enter Post's ID?")
Enter Post's ID? https://www.instagram.com/p/CAueSbHgZWn/
>>> did = 'savefrom.net/' + pid
>>> w.open(did)
True
>>> 
