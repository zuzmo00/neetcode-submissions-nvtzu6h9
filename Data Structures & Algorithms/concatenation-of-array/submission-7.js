class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    getConcatenation(nums) {
        const arry=[]
        for(let i=0;i<2;i++){
            for (let a=0;a<nums.length;a++){
                arry.push(nums[a])
            }
        }
        return arry
    }
}
