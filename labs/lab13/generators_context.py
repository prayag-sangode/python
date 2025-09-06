# --- Generator Function Example ---
def countdown(n):
    print("Starting countdown...")
    while n > 0:
        yield n
        n -= 1

print("Countdown Generator:")
for num in countdown(5):
    print(num)

# --- Generator Expression Example ---
squares = (x*x for x in range(5))
print("Squares using generator expression:")
for sq in squares:
    print(sq)

# --- Custom Context Manager using 'with' ---
class FileWriter:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        print("Opening file...")
        self.file = open(self.filename, "w")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing file...")
        self.file.close()
        if exc_type:
            print(f"An error occurred: {exc_value}")
        return True  # suppress exceptions

# Using custom context manager
with FileWriter("sample.txt") as f:
    f.write("Hello from context manager!\n")

print("Check sample.txt for output")
