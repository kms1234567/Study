# https://school.programmers.co.kr/learn/courses/30/lessons/60057#

def solution(s):
    len_s = len(s)
    answer = len_s

    # 1~len(s)//2
    for n in range(1, (len_s//2 +1)):
        tmp = '';str_iter = '';cnt = 0
        for c in range(len_s//n):
            str_tmp = s[c*n:c*n+n]
            
            if str_iter:
                if str_iter == str_tmp:
                    cnt += 1
                    continue
                else:
                    if not cnt:
                        tmp += str_iter
                    else:
                        tmp += (str(cnt+1) + str_iter)
            str_iter = str_tmp;cnt = 0
                    
        if not cnt:
            tmp += str_iter
        else:
            tmp += (str(cnt+1) + str_iter)

        tmp += s[(c+1)*n:]
        answer = min(answer,len(tmp))
    
    return answer