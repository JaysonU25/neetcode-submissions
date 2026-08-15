class Solution {
    public boolean hasDuplicate(int[] nums) {
        int length = nums.length;
        
        Set<Integer> set = (Arrays.stream(nums).boxed().collect(Collectors.toSet()));

        if(length > set.size()){
            return true;
        } else{
            return false;
        }
    }
}