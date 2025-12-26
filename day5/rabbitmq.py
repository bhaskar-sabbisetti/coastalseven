import pika


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost")
)
channel = connection.channel()

channel.queue_declare(queue="task_queue")
message = "Hello RabbitMQ!"
channel.basic_publish(
    exchange="",
    routing_key="task_queue",
    body=message
)
for i in range(5):
    channel.basic_publish(
        exchange="",
        routing_key="task_queue",
        body=f"Task {i}"
    )

print("Message sent:", message)

connection.close()
