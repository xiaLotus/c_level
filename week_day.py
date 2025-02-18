from datetime import datetime, timedelta

def get_week_range(year, week):
    """ 根據年份和週數，計算該週的起始與結束日期 (星期一到星期日) """
    # 取得當年的第一天
    first_day = datetime(year, 1, 1)
    
    # ISO 週制的第一週包含 1 月 4 日，因此我們找到第一個星期一
    first_monday = first_day + timedelta(days=(7 - first_day.isoweekday() + 1) % 7)
    
    # 計算該週的開始日期 (從該年的第一個星期一開始算)
    start_date = first_monday + timedelta(weeks=week - 1)
    end_date = start_date + timedelta(days=6)  # 該週的結束日期（星期日）
    
    return start_date, end_date

# 取得今天的日期
today = datetime.today()

# 取得當前的 ISO 週數與年份
current_year, current_week, _ = today.isocalendar()

# 計算前 4 週的範圍（由最遠到最近）
for i in range(4, 0, -1):
    start, end = get_week_range(current_year, current_week - i)
    print(f"前 {i} 週 (第 {current_week - i} 週): {start.strftime('%Y-%m-%d')} 至 {end.strftime('%Y-%m-%d')}")

# 計算當前週的起點與終點
current_start, current_end = get_week_range(current_year, current_week)
print(f"本週 (第 {current_week} 週): {current_start.strftime('%Y-%m-%d')} 至 {current_end.strftime('%Y-%m-%d')}")

# 計算後 3 週的範圍（由最近到最遠）
for i in range(1, 4):
    start, end = get_week_range(current_year, current_week + i)
    print(f"後 {i} 週 (第 {current_week + i} 週): {start.strftime('%Y-%m-%d')} 至 {end.strftime('%Y-%m-%d')}")
