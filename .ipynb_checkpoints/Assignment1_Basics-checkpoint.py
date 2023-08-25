ques = input("Enter your question num")
if ques == '1':
    li1 = [1,2,3,4]
    li2 = ['A', 'B', 'C', 'D']
    d = {}
    for i in range(len(li1)):
        d[li1[i]] = li2[i]
    print(d)

elif ques == '2':
    dic = {1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'E', 7:'D'}
    for i in dic:
        if dic[i] == 'D':
            dic[i] = 'apple'
    print(dic)
    
elif ques == '3':
    dic1 = {'A': 1, 'B':2, 'C':3, 'D':7, 'E':4, 'F':5, 'G':6, 'H':7}
    for k,v in dic1.items():
        if dic1[k] == 7:
            dic1[k] = 10
    print(dic1)
    
elif ques == '4':
    A = [1,2,9,7,10,11]
    B = [1,9,12,13,14,10]
    for i in range(len(A)):
        for j in range(len(A)):
            if A[i] == B[j]:
                print(A[i], end=' ,')

elif ques == '5':
    
    for i in range(10):
        if i % 2 == 0:
            continue
        else:
            print(i)

    
    for i in range(10):
        if i % 2 != 0:
            print(i)
            break
        else:
            print(i)

        
    
    