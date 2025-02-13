from datetime import datetime, timedelta
now=datetime.now()
now_5= now - timedelta(days=5)
print('current date',now)
print('5 day ago',now_5)