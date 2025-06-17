date = list(map(int,input().split()))



month_date = [31,28,31,30,
              31,30,31,31,
              30,31,30,31]


day_of_week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT" ]
    
total_date = sum(month_date[:date[0]-1]) + date[1]

ans = day_of_week[total_date % 7]
print(ans)
