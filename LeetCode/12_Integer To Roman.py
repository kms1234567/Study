# 딕셔너리로 예외의 경우를 모두 넣은 풀이
class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ''
        dicts = {1000:'M', 900:'CM', 500:'D', 400:'CD',  100:'C', 90:'XC',  50:'L', 40:'XL',  10:'X', 9:'IX',  5:'V', 4:'IV', 1:'I'}
        
        for key in dicts.keys():
            share, num = divmod(num, key)
            ans += (dicts[key]*share)
            
        return ans

# 해당되는 숫자만 넣고, 예외처리를 하는 풀이
class Solution:
    def intToRoman(self, num: int) -> str:
        ans = []
        dicts = {1000:'M', 500:'D', 100:'C', 50:'L', 10:'X', 5:'V', 1:'I'}
        keys = list(dicts.keys())
        
        for i in range(len(keys)):
            key = keys[i]
            share = num // key
            
            if not share:
                continue
                
            if share == 4:
                if ans and ans[-1] == dicts[keys[i-1]]:
                    ans.pop()
                    ans.append(dicts[key])
                    ans.append(dicts[keys[i-2]])
                else:
                    ans.append(dicts[key])
                    ans.append(dicts[keys[i-1]])
                share = 0
            
            for _ in range(share):
                ans.append(dicts[key])
            num %= key
            
        return ''.join(ans)