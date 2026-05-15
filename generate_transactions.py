import uuid
import random
from datetime import datetime, timedelta

start_date = datetime(2026, 1, 1)
end_date = datetime(2026, 12, 31, 23, 59, 59)

def get_random_datetime(start: datetime, end: datetime) -> datetime:
    # Calculate the time delta between bounds
    delta = end - start
    total_seconds = int(delta.total_seconds())
    
    # Pick a random number of seconds
    random_seconds = random.randint(0, total_seconds)
    
    # Return the new timestamp
    return start + timedelta(seconds=random_seconds)

merchant_categories = ["electronics", "clothing", "groceries", "entertainment", "travel"]
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]

data = {
  "transaction_id": str(uuid.uuid4()),
  "user_id": "user_042",
  "amount": 847.32,
  "timestamp": get_random_datetime(start_date, end_date).isoformat(),
  "merchant_category": random.choice(merchant_categories),
  "city": random.choice(cities),
}