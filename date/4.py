from datetime import datetime
date1=datetime(2025,2,10,12,30,0)
date2=datetime(2025,2,13,12,30,0)
diff=(date2-date1).total_seconds()
print(f"Diff: {diff}")