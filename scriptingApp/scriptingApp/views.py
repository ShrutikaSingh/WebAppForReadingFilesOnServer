from django.shortcuts import render
import requests

def button(config):
    return render(config,'home.html')

def output(config):
    data=requests.get("https://reqres.in/api/users")
    print (data.text)
    data=data.text
    return render(config,'home.html',{'data':data})
