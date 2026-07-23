class LRUPageReplacement:
    """
    Simulates Least Recently Used Page Replacement.
    """

    def __init__(self, capacity):

        self.capacity = capacity
        self.frames = []
        self.page_faults = 0
        self.page_hits = 0

    def access_page(self, page):

        if page in self.frames:

            self.page_hits += 1

            self.frames.remove(page)

            self.frames.append(page)

            print(f"Page {page}: HIT")

            return

        self.page_faults += 1

        if len(self.frames) >= self.capacity:

            removed = self.frames.pop(0)

            print(f"Removed Page {removed}")

        self.frames.append(page)

        print(f"Page {page}: FAULT")

        print(f"Frames: {self.frames}\n")

    def statistics(self):

        total = self.page_hits + self.page_faults

        print("=" * 40)

        print("LRU Statistics")

        print("=" * 40)

        print(f"Page Hits   : {self.page_hits}")

        print(f"Page Faults : {self.page_faults}")

        print(f"Hit Ratio   : {self.page_hits/total:.2f}")

        print(f"Miss Ratio  : {self.page_faults/total:.2f}")