s = int(input('成績:'))
if s > 100:
    print('錯誤')
elif s < 0:
    print('錯誤') 
elif s >=90:
    print('A') 
elif s >=80:
    print('B') 
elif s >=70:
    print('C')
elif s >=60:
    print('D') 
else:
    print('E')         