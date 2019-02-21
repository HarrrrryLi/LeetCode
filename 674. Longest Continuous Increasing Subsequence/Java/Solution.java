class Solution {
    public int findLengthOfLCIS(int[] nums) {
        if(nums == null)
            return 0;
        
        int size = nums.length;
        if(size == 0)
            return 0;
        
        int cnt = 1;
        int result = 1, temp = 1;
        while(cnt < size){
            if(nums[cnt - 1] >= nums[cnt]){
                result = Math.max(result, temp);
                temp = 1;
            }
            else
                temp ++;
            cnt += 1;
        }
        result = Math.max(result, temp);
        
        return result;
        
    }
}