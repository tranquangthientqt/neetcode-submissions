class Solution {
    public int[] twoSum(int[] nums, int target) {
        int need = 0;
        Map<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i < nums.length; i++) {
            need = target - nums[i];
            while(map.containsKey(need)) {
                return new int[]{map.get(need), i};
            }
            map.put(nums[i], i);
        }
        return new int[2];
    }
}
