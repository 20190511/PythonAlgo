lists = None
bools = None
ret_lists = None

def recul (count: int, idx: int):
    if idx >= len(lists):
        return
    if count == 0:
        ret_lists.append([lists[i] for i, item in enumerate(bools) if item])
        return

    for i in range(idx, len(lists)):
        bools[i] = True
        recul(count-1, i+1)
        bools[i] = False

if __name__ == "__main__":
    lists = [5,4,1,2,6,10,9,11,22,52,99]
    bools = [False for _ in range(len(lists))]

    for i in range(len(lists)+1):
        recul(count=i, idx=0)
    print(ret_lists)
