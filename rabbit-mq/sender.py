import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Create queue
channel.queue_declare(queue='hello')

# Publish Message
channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')

print("Sent 'Hello World!'")

connection.close() 