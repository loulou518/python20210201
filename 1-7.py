e = int(input('英文成績:'))
m = int(input('數學成績:'))
if e >=90 and m >=90:
    print('有獎')
elif e < 60 and m < 60:
    print('處罰')
elif e < 0 and m < 0:
    print('錯誤')
else:
    print('加油')