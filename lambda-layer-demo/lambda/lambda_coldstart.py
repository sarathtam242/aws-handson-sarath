import time
import random

# Cold start init
start_init = time.time()
time.sleep(20)  # Simulate heavy loading
GLOBAL_INIT_DURATION = time.time() - start_init
COLD_START = True

def lambda_handler(event, context):
    global COLD_START

    if COLD_START:
        init_duration = GLOBAL_INIT_DURATION
        COLD_START = False
    else:
        init_duration = 0.0  # No init time for warm start

    start_exec = time.time()
    time.sleep(1)  # Simulate processing
    exec_duration = time.time() - start_exec

    return {
        "lambda_version": "Cold Start Test",
        "start_type": "cold" if init_duration > 0 else "warm",
        "init_duration_seconds": round(init_duration, 3),
        "execution_duration_seconds": round(exec_duration, 3),
        "random_id": random.randint(1000, 9999)
    }
