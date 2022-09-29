from itertools import product

class Solution: 
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        dicts = {'2':['a', 'b', 'c'], '3':['d','e','f'], '4':['g','h','i'], '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'],
            '8':['t', 'u', 'v'], '9':['w','x','y','z']}
        
        res = []
        
        for d in digits:
            res.append(dicts[d])

        # product -> 중첩 반복문으로 경우의 수 찾기
        res = list(product(*res))

        return [''.join(res[i]) for i in range(len(res))]