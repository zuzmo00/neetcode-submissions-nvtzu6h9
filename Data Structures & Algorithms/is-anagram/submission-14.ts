class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s: string, t: string): boolean {
        if(s.length!=t.length){
            return false
        }

        let dica: Record<string,number>={}
        let dicb: Record<string,number>={}
        for(let i=0;i<s.length;i++){
            if(s[i] in dica){
                dica[s[i]]+=1
            }
            else{
                dica[s[i]]=1
            }
        }
        for(let i=0;i<t.length;i++){
            if(t[i] in dicb){
                dicb[t[i]]+=1
            }
            else{
                dicb[t[i]]=1
            } 
        }
        for(let i in dica){
            if (dica[i]!==dicb[i]){
                return false
            }
        }
        return true
    }
}
