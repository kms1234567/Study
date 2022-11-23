class Solution:
    def maximum69Number (self, num: int) -> int:
        max_num = num
        for i in range(len(str(num))):
            tmp = list(str(num))
            if tmp[i] == '6':
                tmp[i] = '9'
                tmp = int(''.join(tmp))
                if max_num < tmp:
                    max_num = tmp
                break
                
        return max_num