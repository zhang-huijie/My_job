import time,datetime
date = list(input().rstrip().split('|'))
day_a = list(map(int,date[0].split(' ')))
day_b = list(map(int,date[1].split(' ')))
aa = datetime.date(day_a[0],day_a[1],day_a[2])
bb = datetime.date(day_b[0],day_b[1],day_b[2])
#比这一年大
if day_b[0]>day_a[0]:
    day_s= int((bb-aa).days)
    m = day_s%7
    if m+day_a[3]<=7:
        print(m+day_a[3])
    else:
        print(m+day_a[3]-7)
#比这一年小
elif day_b[0]<day_a[0]:
    day_s = abs(int((bb - aa).days))
    m = day_s % 7
    if m<day_a[3]:
        print(day_a[3]-m)
    else:
        print(7-(m-day_a[3]))
#同一年比较月份和日期
else :
    if day_b[1]>day_a[1]:
        day_s = int((bb - aa).days)
        m = day_s % 7
        if m + day_a[3] <= 7:
            print(m + day_a[3])
        else:
            print(m + day_a[3] - 7)
    if day_b[1]<day_a[1]:
        day_s = abs(int((bb - aa).days))
        m = day_s % 7
        if m < day_a[3]:
            print(day_a[3] - m)
        else:
            print(7 - (m - day_a[3]))
    else:
        if day_b[2]>=day_a[2]:
            day_s = int((bb - aa).days)
            m = day_s % 7
            if m + day_a[3] <= 7:
                print(m + day_a[3])
            else:
                print(m + day_a[3] - 7)
        if day_b[2]<day_a[2]:
            day_s = abs(int((bb - aa).days))
            m = day_s % 7
            if m < day_a[3]:
                print(day_a[3] - m)
            else:
                print(7 - (m - day_a[3]))














