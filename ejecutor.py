import tasks
# result = tasks.async_call((5,2))
result = tasks.add.delay(5, 2)
# Espera como mucho un segundo (opcional)
print(result.get(timeout=1))