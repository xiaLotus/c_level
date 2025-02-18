from datetime import datetime

# 取得當前日期
today = datetime.today()

# 取得今年的第幾週
week_number = today.isocalendar()[1]

print(f"今天是今年的第 {week_number} 週")