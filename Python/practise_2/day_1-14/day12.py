import threading
import time


def download_package(package_name: str) -> None:
    print(f"Start download package {package_name}")
    time.sleep(2)
    print(f"Download package {package_name} complete")



total_start = time.perf_counter()

threads = []

for i in range(5):
    t = threading.Thread(target=download_package, args=(f"pkg_{i+1}",))
    threads.append(t)
    t.start()

for i in threads:
    t.join()


total_end = time.perf_counter()
total_time = total_end - total_start

print(f"\n 5 threads, took total {total_time}s")


# Problem 3

class BankAccount:
    def __init__(self, balance: int):
        self.balance = balance
        self.lock = threading.Lock()

    def transfer(self, target, amount: int):
        if amount < 0:
            return ValueError("Amount must be positive"）

        first, second = sorted([self, target], key=id)

        with first.lock:
            with second.lock:
                if amount < self.balance:
                    raise ValueError
                self.balance -= amount
                target.balance += amount

account_a = BankAccount(100_000)
account_b = BankAccount(100_000)

threads = []

for _ in range(100):
    t1 = threading.Thread(
        target=account_a.transfer,
        args=(account_b, 10)
    )

    t2 = threading.Thread(
        target=account_b.transfer,
        args=(account_a, 10)
    )

    threads.extend([t1, t2])

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print("Account A:", account_a.balance)
print("Account B:", account_b.balance)

print(
    "Total:",
    account_a.balance + account_b.balance
)






# Problem 4
def worker(event: threading.Event):
    print("worker started and waiting...")
    event.wait()
    print("worker resume and working...")


evt = threading.Event()

t3 = threading.Thread(target=worker, args=(evt,))
t3.start()

time.sleep(3)
print("set...")
evt.set()

print("join...")
t3.join()

print("clear")
evt.clear()



# Problem 5
from dataclasses import dataclass
import queue

@datalass
class Package():
    name: str
    version: str

def producer(q: queue.Queue):
    pass



def consumer(q: queue.Queue):
    pass


q = queue.Queue(maxsize=5)

producers = []
for i in range(2):
    t = threading.Thread(target=producer, args=(q))
    t.start()
    producers.append()


consumers = []
for i in range(3):
    t = threading.Thread(target=consumer, args=(q))
    t.start()
    consumers.append()


for t in producers:
    t.join()

q.join()











