class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs: string[]): string[][] {
        let dic=new Map<string,string[]>()

        for(let w of strs){
            let list=new Array(26).fill(0)

            for (let i=0;i<w.length;i++){
                let index=w.charCodeAt(i)-"a".charCodeAt(0)
                list[index]++
            }
            let key=list.join("#")
            if(!dic.has(key)){
                dic.set(key,[])
            }
            dic.get(key).push(w)
        }
        return Array.from(dic.values())
    }
}
