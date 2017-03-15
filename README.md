# RabbitMQ - Celery - Beautifulsoup 

Distributed scrapping
--

Getting started
--

**Initial Requirements**

python 2.7

virtualenv

pip

rabbitmq-server


**Installing dependencies (inside virutal environemtn)**

`pip install -r requirements.txt`


Running the server
--

**Starting rabbitmq consumer**

`python rabbit.py`

**Celery**

Starting celery worker

`celery -A processqueue.app worker`

or

`celery -A processqueue.app worker -P gevent`

to start with `gevent`


**Running the script**

`python script.py <filename>`

eg:

`python script.py urls.txt`



Mongodb export of rejected and accepted entries
--

Accepted

`mongoexport -d URLDATA -c accepted --csv --fields url --out accepted.csv`

Rejected

`mongoexport -d URLDATA -c rejected --csv --fields url --out rejected.csv`


