from worker import Worker
from scheduler import RoundRobinScheduler

orders = [
    [101, 102, 103],
    [201, 202, 203],
    [301, 302, 303]
]

workers = []

for i in range(3):

    worker = Worker(i + 1, orders[i])

    workers.append(worker)

scheduler = RoundRobinScheduler(workers)

scheduler.execute()