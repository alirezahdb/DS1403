import threading
import time

def worker(worker_id):
    print(f"Worker {worker_id} starting.")
    time.sleep(1)  
    print(f"Worker {worker_id} finished.")

def main(num_workers):
    threads = []
    start_time = time.time()

    for i in range(num_workers):
        thread = threading.Thread(target=worker, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f"Total time for {num_workers} workers: {end_time - start_time} seconds")

if __name__ == "__main__":
    num_workers = 10000  
    main(num_workers)