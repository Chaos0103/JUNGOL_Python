ch = input()

KOI_cnt = 0
IOI_cnt = 0

for idx in range(len(ch) - 2):
    if ch[idx] == 'K' and ch[idx + 1] == 'O' and ch[idx + 2] == 'I':
        KOI_cnt += 1
    elif ch[idx] == 'I' and ch[idx + 1] == 'O' and ch[idx + 2] == 'I':
        IOI_cnt += 1
        
print(KOI_cnt)
print(IOI_cnt)
