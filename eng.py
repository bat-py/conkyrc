import os
with open('num', 'r') as num:
    n = int(num.readline())
with open('num', 'w') as new:
    new.write(str(n+1))

with open(os.path.join('/home','crow','yandex','english','eng.csv'), 'r') as en:
    for i in range(n):
        en.readline()

    a = en.readline().split('-')
    try:
        print('{0: <25} {1}'.format(a[0], a[1].strip()))
    except:
        with open('num', 'w') as new:
            new.write(str(0))
        print('End of Vocabulary')
