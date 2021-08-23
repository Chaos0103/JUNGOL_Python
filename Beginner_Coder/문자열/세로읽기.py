ch_list = list()
ch_list_len = list()
for _ in range(5):
    ch = input()
    ch_list.append(ch)
    ch_list_len.append(len(ch))

Max = max(ch_list_len)

for bidx in range(Max):
    for fidx in range(5):
        if ch_list_len[fidx] > bidx:
            print(ch_list[fidx][bidx], end='')
