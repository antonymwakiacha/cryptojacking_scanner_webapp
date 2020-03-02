import requests
import bs4
import re
import os
import time
import colorama
from colorama import Fore
from colorama import Style
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
	return render(request,'home.html')

def first(request):
	if request.method=="POST":
		answer=request.POST.get('answer',None)
		if answer == "yes" or answer =="y":
			return render(request,"site.html")
		elif answer == "no" or answer =='n':
		    return render(request,'file.html')
		else:
			return HttpResponse("Invalid input.Please enter yes or no")

	else:
		return HttpResponse("Please enter an answer")



def scanning(request):
	if request.method=="POST":
		website=request.POST.get('website',None)
		try:


			website2=requests.get('http://' + website)

			website2.raise_for_status()

			website3=bs4.BeautifulSoup(website2.text,"html.parser")

			minerRegex = re.compile(r'coinhive.min.js|wpupdates.github.io/ping|cryptonight.asm.js|coin-hive.com|jsecoin.com|cryptoloot.pro|webassembly.stream|ppoi.org|xmrstudio|webmine.pro|miner.start|allfontshere.press|upgraderservices.cf|vuuwd.com')

			final=website3.find("script",text=minerRegex)

			return HttpResponse(final)

		except:
			return HttpResponse("Could not connect.Please check your internet connection or you have entered a wrong site name")
    
	else:
		return HttpResponse("Pleae enter a website")

    	


def multiscanning(request):
	if request.method=="POST" and request.FILES['myfile']:
		multiscan1=request.FILES['myfile']
	
		multiscan=multiscan1.read().splitlines()
		for line in multiscan:
			line=line.decode('utf-8')
			# return HttpResponse(('scanning:'+ line))
			try:
				multiscan2=requests.get('http://' + line.strip(), verify==False,timeout==5)

				multiscan2.raise_for_status()

				multiscan3=bs4.BeautifulSoup(multiscan2.text,"html.parser")

				multifinal=multiscan3.find("script",text=minerRegex)
				if len(str(multifinal) > 16):
						

			
					return HttpResponse(multifinal)

			except:
				pass
				return HttpResponse('connection issues')


