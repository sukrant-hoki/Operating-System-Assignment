import time


class RoundRobinScheduler:

    def __init__(self, workers):
        self.workers = workers

    def execute(self):

        print("\nROUND ROBIN SCHEDULER\n")

        for worker in self.workers:

            print(f"Starting Worker {worker.worker_id}")

            worker.start()

         
            time.sleep(0.2)

        for worker in self.workers:
            worker.join()

        print("\nAll workers have completed execution.\n")