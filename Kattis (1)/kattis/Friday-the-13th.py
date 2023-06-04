# def func(days):
#     

for i in range(0, int(input())):
    days=int(input().split()[0])
    days_in_months = list(map(lambda x: int(x), input().split()))
    presentd = 0
    current_month = 0
    count = 0
    while days > 0:
        if days_in_months[current_month] > 12 and (presentd + 12) % 7 == 5:
            count += 1
        days -= days_in_months[current_month]
        current_day = (presentd + days_in_months[current_month]) % 7
        current_month += 1
    print(count)
   



