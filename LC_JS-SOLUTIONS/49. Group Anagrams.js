/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {

    strDic = {}
    res = []
    for(let index in strs){
        //console.log(strs[index].split('').sort().join(''))
        if(!(strs[index].split('').sort().join('') in strDic)){
            strDic[strs[index].split('').sort().join('')] = [strs[index]]
        }
        else{
            strDic[strs[index].split('').sort().join('')].push(strs[index])
         }
    }

    for (index in strDic){
        res.push(strDic[index])
    }

    return(res)
    
};