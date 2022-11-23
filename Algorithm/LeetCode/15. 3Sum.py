# 시간이 더 빨리 나오는 풀이
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()

        # 여기서는 맨왼쪽 숫자(i)를 증가시키면서 l은 i+1, r은 맨 끝 숫자(len(nums)-1)를 가리킨다.
        for i in range(len(nums)-2):
            # 중복 숫자를 방지하기 위해 전 숫자와 현재 숫자가 같으면 continue한다.
            if i>0 and nums[i] == nums[i-1]:
                continue 
            l, r = i+1, len(nums)-1
            while l<r:
                sum = nums[i] + nums[l] + nums[r]
                if sum<0:
                    l += 1 
                elif sum>0:
                    r -= 1 
                else:
                    answer.append([nums[i],nums[l],nums[r]])
                    # 반복하지 않기 위해 같은 숫자를 모두 건너뛰도록 한다.
                    while l<r and nums[l] == nums[l+1]:
                        l += 1 
                    while l<r and nums[r] == nums[r-1]:
                        r -= 1 
                    l += 1
                    r -= 1
        return answer


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        
        # 숫자리스트를 정렬한다.
        len_nums = len(nums)
        nums.sort()

        # left는 처음, right는 마지막 인덱스로 고정한다.
        left = 0;right = len_nums-1
        
        # mid를 차례대로 증가시키면서, left와 right를 바꿔간다.
        for mid in range(1, right):
            l = left;r = right
            while l < r and l != mid and r != mid:
                num_sum = nums[l] + nums[r] + nums[mid]
                if not num_sum:
                    ans.add((nums[l], nums[mid], nums[r]))
                    l += 1
                elif num_sum > 0:
                    r -= 1
                else:
                    l += 1

        return list(ans)
