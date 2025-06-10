# Kafka Temperature Project

Projeto para produzir e consumir dados de temperatura simulados usando Kafka e Python.
## Como rodar

- Rodar o container Kafka
- Rodar o producer.py para enviar dados
- Rodar o consumer.py para consumir dados

kafka-docker-python/
├── docker-compose.yml
├── requirements.txt
├── producer.py
├── consumer.py
├── Dockerfile.producer
├── Dockerfile.consumer
└── README.md



# Kafka com Docker, Produtor e Consumidor em Python
Este é um projeto exemplo de como configurar o Apache Kafka com Docker , incluindo:

ZooKeeper
Kafka
Kafka UI (Provectus)
Produtor em Python
Consumidor em Python
Tudo orquestrado via docker-compose.yml.

## Funcionalidades
✅ Ambiente completo Kafka local
✅ Produtor enviando dados simulados (temperatura)
✅ Consumidor lendo mensagens do tópico
✅ Interface web para visualizar tópicos e consumidores
✅ Fácil setup com Docker Compose


## Tecnologias usadas
Apache Kafka
ZooKeeper
Docker & Docker Compose
Python 3.12
kafka-python
Faker (para dados simulados)
