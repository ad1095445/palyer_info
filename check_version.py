v1 = '2.1.4.3.4.9'
v2 ='2.001.4.3.4.10'
def check_version(v1,v2):
    l1 = [int(i)for i in(v1.split('.'))]
    l2 = [int(i)for i in(v2.split('.'))]

    for i in range(abs(len(l1)-len(l2))):
        if len(l1)>len(l2):
            l2.append(0)
        else:
            l1.append(0)
    count = 0
    for i in l1:
        if i > l2[l1.index(i)]:
            print(1)
            break
        elif i< l2[l1.index(i)]:
            print(-1)
            break
        else:
            count += 1
    if count == len(l1):
        print(0)


check_version(v1,v2)