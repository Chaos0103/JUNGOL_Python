while True:
    width = int(input('Width = '))
    height = int(input('Height = '))
    print('Triangle Area = %.1f' % ((width * height) / 2))
    ch = str(input('Continue? '))
    if not(ch == 'Y' or ch == 'y'):
        break
