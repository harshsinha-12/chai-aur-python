import time 

wait_time = 1
max_retries = 5
attempts = 0

while attempts < max_retries:
    print(f"Attempt {attempts + 1} waiting {wait_time} seconds...")
    time.sleep(wait_time)
    attempts += 1
    wait_time *= 2
    if attempts == max_retries:
        print("Sorry, I give up!")
        break