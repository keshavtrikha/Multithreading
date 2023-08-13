import threading

# Function to print 'a's in a loop
def lw():
    while True:
        print('a')

# Function with an infinite loop
def b():
    while True:
        pass

# Create threads for functions 'lw' and 'b'
thread_lw = threading.Thread(target=lw)
thread_b = threading.Thread(target=b)

# Start the threads
thread_lw.start()
thread_b.start()

# Wait for both threads to finish
thread_lw.join()
thread_b.join()
