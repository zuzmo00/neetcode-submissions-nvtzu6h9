class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums: number[], target: number): number[] {
        let dic:Record<number,number>={}

        for( let i=0;i<nums.length;i++){
            if(nums[i] in dic){
                return [dic[nums[i]],i]
            }
            dic[target-nums[i]] = i
        }
    }
}
