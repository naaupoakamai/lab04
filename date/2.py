from datetime import datetime, timedelta
today=datetime.now()
yesterday= today - timedelta(days=1)
tomorow= today + timedelta(days=1)
print('today',today)
print('tomorow',tomorow)
print('yesterday',yesterday)