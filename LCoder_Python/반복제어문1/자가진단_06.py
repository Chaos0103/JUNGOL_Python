while True:
    print('1. Korea')
    print('2. USA')
    print('3. Japan')
    print('4. China')
    num = int(input('number? '))

    if not(1 <= num <= 4):
        print('none')
        break

    if num == 1:
        print('Seoul')
    elif num == 2:
        print('Washington')
    elif num == 3:
        print('Tokyo')
    elif num == 4:
        print('Beijing')
