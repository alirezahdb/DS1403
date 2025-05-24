from concurrent.futures import ThreadPoolExecutor
import time

def worker(worker_id):
    print(f"Worker {worker_id} starting.")
    time.sleep(1) 
    print(f"Worker {worker_id} finished.")

def main(num_workers):
    start_time = time.time()

    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        for i in range(num_workers):
            executor.submit(worker, i)

    end_time = time.time()
    print(f"Total time for {num_workers} workers: {end_time - start_time} seconds")

if __name__ == "__main__":
    num_workers = 10000 
    main(num_workers)