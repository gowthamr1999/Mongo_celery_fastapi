from tasks import add

# Call the Celery task asynchronously
result = add.apply_async(args=(4, 5))

# Wait for the result
print("Task ID:", result.id)
print("Task Status:", result.status)

# You can also retrieve the result later if needed
print(result.get())
