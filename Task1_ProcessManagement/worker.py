import threading
import time
import random


completed_orders = 0

lock = threading.Lock()


class Worker(threading.Thread):

    def __init__(self, worker_id, orders):
        super().__init__()
        self.worker_id = worker_id
        self.orders = orders

    def run(self):
        global completed_orders

        for order in self.orders:

            print(f"Worker {self.worker_id} is preparing Order {order}")

            
            time.sleep(random.uniform(0.5, 1.5))

          
            with lock:
                completed_orders += 1

                print(
                    f"Worker {self.worker_id} completed Order {order}"
                )

                print(
                    f"Total Completed Orders: {completed_orders}\n"
                )