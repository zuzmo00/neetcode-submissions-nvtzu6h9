class Solution {
    /**
     * @param {number[]} nums
     * @param {number} val
     * @return {number}
     */
    removeElement(nums: number[], val: number): number {
        let k=0
        for(let i in nums){
            if(nums[i]!=val){
                nums[k]=nums[i]
                k++
            }
        
        }
        return k
    }
}