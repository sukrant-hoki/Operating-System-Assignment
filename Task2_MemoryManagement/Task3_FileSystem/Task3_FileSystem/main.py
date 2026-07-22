from fifo import FIFOPageReplacement
from lru import LRUPageReplacement


reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]

FRAME_SIZE = 3

print("=" * 50)
print("FIFO PAGE REPLACEMENT")
print("=" * 50)

fifo = FIFOPageReplacement(FRAME_SIZE)

for page in reference_string:
    fifo.access_page(page)

fifo.statistics()

print("\n")

print("=" * 50)
print("LRU PAGE REPLACEMENT")
print("=" * 50)

lru = LRUPageReplacement(FRAME_SIZE)

for page in reference_string:
    lru.access_page(page)

lru.statistics()