import subprocess

result = subprocess.run(['grep', 'hello'], capture_output=True, text=True, input="hello world\nbye")
print("Output:", result.stdout.strip())  # Should print "hello world"