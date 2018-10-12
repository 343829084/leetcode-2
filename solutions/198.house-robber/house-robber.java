class Solution {
    public int rob(int[] nums) {
        if (nums == null || nums.length == 0){
            return 0;
        }
        if (nums.length == 1){
            return nums[0];
        }
        int dp1 = nums[0];
        int dp2 = Math.max(dp1, nums[1]);
        for(int i=2; i < nums.length; i++){
            int dp = Math.max(dp1 + nums[i], dp2);
            dp1 = dp2;
            dp2 = dp;
        }
        return dp2;
    }
}
