from celery import Celery, task
# Crea usando RPC para devolver los datos, y el broker AMQP
app = Celery("tasks", backend="rpc://", broker="pyamqp://guest@localhost//")
# Con no_ack no espera un ack al terminar
@app.task(no_ack=True)
def add(a, b):
    return a+b