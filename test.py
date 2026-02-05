from concurrent.futures import ThreadPoolExecutor
from mails import GenerateOTP
import time
global example 

executor = ThreadPoolExecutor(max_workers=20)
import time

def task(self,a, b):
    email = a
    name = b
    if not isinstance((a,b),str):
        raise Exception("wrong methods")
    print("working on the thread")
    print ("attempting to send a mail.. please wait...")
    GenerateOTP(email,name)
    print("working on the thread")   # blocking IO
    return a + b
future = executor.submit(task, "kummarirahul1980@gmail.com", "Rahul")
while not future.done():
    print("waiting for the thread to complete")
    time.sleep(1)
if future.done():
    example = future.result()
    print("thread is done    ",example)
result = future.result()
print("this is a thread main")
time.sleep(20)
print("Threads complete   ", future.result())