class Solution:
    # 백트래킹 문제이다.
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        def back(prev, tmp):
            sum_tmp = sum(tmp)
            
            if sum_tmp == target:
                answer.append(tmp)
            elif sum_tmp > target:
                return
            
            # 모든 경우의 수를 탐색한다. product와 유사하지만, 중간에 끊을 수 있다.
            for i in range(prev, len(candidates)):
                num = candidates[i]
                back(i, tmp+[num])
            
        back(0, [])
        return answer