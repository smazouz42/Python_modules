import time
import datetime

current_time = time.time()

scientific_notation = f"{current_time:.2e}"

current_date = datetime.datetime.now().strftime("%b %d %Y")

print(f"Seconds since January 1, 1970: {current_time:,.4f} or {scientific_notation} in scientific notation")
print(current_date)
