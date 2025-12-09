from time import time, sleep
from collections import Counter


class TokenBucketRateLimiter:
    def __init__(self, capacity: int, refill_rate: int) -> None:
        self.max_capacity = capacity
        self.refill_rate = refill_rate
        self.capacity = Counter()
        self.last_refill_time = Counter()

    def allow_request(self, user_id: str, requested_capacity: int) -> bool:
        self._replenish(user_id)
        if self.capacity[user_id] >= requested_capacity:
            self.capacity[user_id] -= requested_capacity
            return True
        return False

    def _replenish(self, user_id: str) -> None:
        gained = (
            self._get_time_seconds() - self.last_refill_time[user_id]
        ) * self.refill_rate
        self.last_refill_time[user_id] = self._get_time_seconds()
        self.capacity[user_id] = min(self.max_capacity, self.capacity[user_id] + gained)

    def _get_time_seconds(self) -> int:
        return int(time())


# Example Usage
# Capacity: 10 tokens. Refills 1 token per second.
limiter = TokenBucketRateLimiter(capacity=10, refill_rate=1.0)

# t=0: User A sends a burst
print(limiter.allow_request("user_A", 5))  # True (Remaining: 5)
print(limiter.allow_request("user_A", 5))  # True (Remaining: 0)
print(limiter.allow_request("user_A", 1))  # False (Remaining: 0)

# t=2: Two seconds pass. User A should have regained 2 tokens.
sleep(2)
print(limiter.allow_request("user_A", 1))  # True (Remaining: 1)
