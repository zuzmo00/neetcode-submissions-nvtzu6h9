class Solution {
    /**
     * @param {string[]} strs
     * @return {string}
     */
    longestCommonPrefix(strs: string[]): string {
        let res=""
        for (let i =0 ; i<strs[0].length;i++){
            for(let w=0; w<strs.length;w++){
                if(i===strs[w].length || strs[w][i]!==strs[0][i]){
                    return res
                }
            }
            res+=strs[0][i]
        }
        return res
    }
}
