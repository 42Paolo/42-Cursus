import time
from datetime import datetime

date_today = datetime.now()
epoch_seconds = time.time()

print("Seconds since January 1, 1970:", f"{epoch_seconds:,.4f}", "or", f"{epoch_seconds:.2e}", "in scientific notation")
print(date_today.strftime("%b %d %Y")) 
