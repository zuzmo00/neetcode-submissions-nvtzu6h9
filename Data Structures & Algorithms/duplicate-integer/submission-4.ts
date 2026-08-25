class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums: number[]): boolean {
        interface Dic{
            [key:number]:number
        }
        let dic:Dic={}
        for(let i=0;i<nums.length;i++){
            if (nums[i] in dic){
                return true
            }
            dic[nums[i]]=1
        
        }
        return false
    }
}
