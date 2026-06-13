# SE Intern Assessment – Data Structures & Systems Design

## Problem 1: LRU Cache

Built an LRU Cache using a **hash map + doubly linked list** combination.

- `get(key)` – fetches the value for a key and marks it as recently used. Returns -1 if not found.
- `put(key, value)` – adds or updates a key. If the cache is full, the least recently used item is removed first.

Both run in **O(1)** time.

**File:** `lru_cache.py`

---

## Problem 2: Event Scheduler

- `can_attend_all(events)` – checks if all events can be attended without any time conflicts.
- `min_rooms_required(events)` – finds the minimum number of rooms needed to run all events at the same time.

Approach: sort by start time + **min-heap** to track room availability. Time complexity: **O(n log n)**.

**File:** `event_scheduler.py`

---

## Language
Python 3
