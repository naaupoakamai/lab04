from datetime import datetime
current_time=datetime.now()
current_time=current_time.replace(microsecond=0)
print(current_time)