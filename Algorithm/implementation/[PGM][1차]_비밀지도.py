# https://school.programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2):
    answer = []
    
    for idx ,data in enumerate(zip(arr1, arr2)):
        i = data[0];j=data[1]
        arr1[idx] = str(bin(i)[2:]).rjust(n, '0');arr2[idx] = str(bin(j)[2:]).zfill(n)
    print(n, arr1, arr2)
    for i in range(n):
        tmp = ''
        for j in range(n):
            k = int(arr1[i][j])
            l = int(arr2[i][j])
            
            if k|l:
                tmp+='#'
            else:
                tmp += ' '
        answer.append(tmp)
    
    return answer