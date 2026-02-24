import time
from collections import defaultdict

class TokenBucket:
    def __init__(self, capacity, refill_rate):
        """
        capacity: Maximum tokens bucket can hold
        refill_rate: Tokens added per second
        """
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.tokens = capacity
        self.last_refill = time.time()

    def allow_request(self):
        current_time = time.time()
        elapsed = current_time - self.last_refill

        # Add tokens based on time passed
        refill_tokens = elapsed * self.refill_rate
        self.tokens = min(self.capacity, self.tokens + refill_tokens)
        self.last_refill = current_time

        if self.tokens >= 1:
            self.tokens -= 1
            return True
        return False


class RateLimiter:
    def __init__(self, capacity=5, refill_rate=1):
        """
        capacity = max requests allowed
        refill_rate = tokens added per second
        """
        self.users = defaultdict(lambda: TokenBucket(capacity, refill_rate))

    def allow(self, user_id):
        bucket = self.users[user_id]
        return bucket.allow_request()


# Example usage
if __name__ == "__main__":
    limiter = RateLimiter(capacity=5, refill_rate=1)

    user = "kanishga_user"

    for i in range(10):
        if limiter.allow(user):
            print(f"Request {i+1}: Allowed")
        else:
            print(f"Request {i+1}: Blocked")
        time.sleep(0.5)
