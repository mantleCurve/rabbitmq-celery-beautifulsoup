import pika
import sys
import json
filename = sys.argv[1] #getting the filename here
credentials = pika.PlainCredentials('guest', 'guest') #rabbitmq default configuration
connection = pika.BlockingConnection(pika.ConnectionParameters( host="localhost",
           socket_timeout=600,credentials=credentials))
channel = connection.channel()
channel1 = connection.channel()

with open(filename, 'rb') as urlfile:
	for url in urlfile.readlines():
		data = {"url":url}
		#sendinng data to rabbitmq queue
		channel.basic_publish(exchange='',
              routing_key='standard_url_queue',
              body=json.dumps(data))
 		print url
