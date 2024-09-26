from confluent_kafka import Consumer, KafkaException, KafkaError

# Configura el consumidor
conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'my-group',
    'auto.offset.reset': 'earliest'
}

# Crea el consumidor
consumer = Consumer(conf)
topic = 'test'

# Suscribirse al tema
consumer.subscribe([topic])

try:
    while True:
        # Espera hasta 1 segundo por nuevos mensajes
        msg = consumer.poll(timeout=1.0)

        if msg is None:
            continue

        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                # Fin de la partición alcanzado
                continue
            else:
                raise KafkaException(msg.error())

        # Imprime el mensaje recibido
        print(f"Mensaje recibido: {msg.value().decode('utf-8')}")

finally:
    # Cierra el consumidor
    consumer.close()
