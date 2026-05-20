class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            # Nếu phần tử hiện tại hợp lệ (khác val), hãy giữ nó
            if nums[j] != val: 
                nums[i] = nums[j]
                i += 1
        return i