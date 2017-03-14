"""Queue processing happens here
   Celery maintains the pool to speed up the multiprocessing
"""

from celery import Celery

from bs4 import BeautifulSoup
from mongoengine import *
import requests

app = Celery('tasks', broker='pyamqp://guest@localhost//') #celery setting 
														   #rabbitmq-server as its broker


#Mongoengine models
class Accepted(Document):
	url = StringField()

class Rejected(Document):
	url = StringField()


#defining the celery task
@app.task(name='scraptest')
def scraptest(url):
	connect('URLDATA') # mongodb databse connection. Defined 
						#here to fix fork problem of celery
	r = requests.get(url)
	data = r.content
	soup = BeautifulSoup(data,"html.parser")
	js_data = soup.find_all('script')
	js_exists = None
	for js in js_data:
		if "jquery.js" in str(js): #checking whether jquery.js exist in the sciript tag
			js_exists = True
		else:
			js_exists = False
	if js_exists:
		accepted = Accepted(url=url)
		accepted.save()
	else:
		rejected = Rejected(url=url)
		rejected.save()
	return "done" # response being send back to acknowledge the process