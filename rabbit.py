import pika

import json
from processqueue import scraptest

#rabbit-mq connection
credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',credentials=credentials,socket_timeout=600)) 
channel = connection.channel()
channel.queue_declare(queue='standard_url_queue',durable=True)



def results(ch, method, properties, body):
    url = json.loads(body)['url'].replace("\n",'')
    scraptest.delay(url) #calling the scraptest celery task to process the url
    channel.basic_ack(delivery_tag = method.delivery_tag) 
    return "done"

channel.basic_qos(prefetch_count=1)
channel.basic_consume(results,
                      queue='standard_url_queue',)

channel.start_consuming()