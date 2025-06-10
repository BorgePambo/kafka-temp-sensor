from kafka import KafkaProducer
from faker import Faker
import random
import time
import json

# Inicializando Faker
fake = Faker()

# Criando o produtor Kafka
producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    api_version=(3, 8, 0),
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),  # Serializa valor para JSON
    key_serializer=lambda k: k.encode('utf-8')  # Serializa a chave para bytes
)

def generate_temperature_data():
    return {
        "sensor_id": str(random.randint(1, 50)),  # ID único do sensor
        "temperature": round(random.uniform(-10.0, 40.0), 2),  # Temperatura aleatória
        "timestamp": fake.date_time().isoformat()  # Timestamp no formato ISO
    }

if __name__ == "__main__":
    topic = "temperatura_sensor_topic"

    while True:
        data = generate_temperature_data()
        key = data["sensor_id"]  # Usando sensor_id como chave
        producer.send(topic, key=key, value=data)
        print(f"Mensagem enviada: {data}")
        time.sleep(1)  # Envia uma mensagem por segundo