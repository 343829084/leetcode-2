class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        int length = nums.length;
        if (length < 3) return res;
        
        Arrays.sort(nums);
        int max = nums[length - 1];
        if (max < 0) return res;
    
        for (int i = 0; i < length-2; i++){
            if((nums[i] + nums[length-2] + max) < 0) continue;
            int left = i + 1;
            int right = length - 1;
            while(left < right){
                int sum = nums[i] + nums[left] + nums[right];
                if(sum==0){
                    res.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    while(nums[left] == nums[left+1] && left<length-2) left ++;
                    while(nums[right] == nums[right-1] && right>left) right--;
                    left++;
                } else if(sum < 0){
                    left++;
                } else {
                    right--;
                }
            }
            
            while(nums[i]==nums[i+1] && i < length-2){
                i++;
            }
            
        }
        return res;
        
    }
}