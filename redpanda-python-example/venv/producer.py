from confluent_kafka import Producer

# Configura el productor
conf = {
    'bootstrap.servers': 'localhost:9092'
}

producer = Producer(conf)

# Función de callback para verificar si el mensaje se ha enviado
def delivery_report(err, msg):
    if err is not None:
        print(f"Error al enviar mensaje: {err}")
    else:
        print(f"Mensaje enviado a {msg.topic()} [{msg.partition()}]")

# Envía un mensaje al tópico 'test'
topic = 'test'
message = 'Hola, Redpanda!'

# Produce el mensaje con callback
producer.produce(topic, message.encode('utf-8'), callback=delivery_report)

# Asegúrate de enviar todos los mensajes
producer.flush()
