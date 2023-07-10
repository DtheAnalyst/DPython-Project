#!/usr/bin/env python
# coding: utf-8

# In[8]:


import requests
import json
import win32com.client as wincom

city = input("Enter the name of City \n")
url=f"https://api.weatherapi.com/v1/current.json?key=47922e4bab8448f997885653231007&q={city}"

r = requests.get(url)
#print(r.text)
wdic = json.loads(r.text)

w = (wdic["current"]["temp_c"])
v = (wdic["current"]["temp_f"])
x = (wdic["location"]["localtime"])

speak = wincom.Dispatch("SAPI.SpVoice")


text = f'The current weather in {city} is {w} degrees and {v} in farhenite at {x} time'
speak.speak(text)


# In[ ]:





# In[ ]:




