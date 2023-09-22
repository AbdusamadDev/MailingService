from tasks import schedule_send

result = schedule_send.delay("asdad", "asdada", "Asadasda")  # This will not block and return immediately.
# app.py

print(result.ready())  # Check if the task has finished.
print(result.get())  # Get the result (this will block until the result is available).
