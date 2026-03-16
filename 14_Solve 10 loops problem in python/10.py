import time

wait_time = 1
max_retries = 5
attempts = 1

while attempts  <= max_retries:
    if(attempts == max_retries):
        print("attempt: ", attempts, "no next attempt")
        break
    print("attempt: ", attempts, "wait time: " ,wait_time)
    time.sleep(wait_time)
    attempts += 1
    wait_time *= 2
    # wait_time = attempts ** wait_time