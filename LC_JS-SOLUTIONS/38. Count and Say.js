/**
 * @param {number} n
 * @return {string}
 */
var countAndSay = function(n) {

    if (n == 1){
        return '1'
    }

    let prev = countAndSay(n-1)
    res = ''
    count = 1

    for (let i=0;i<prev.length;i++){
        if(i == prev.length -1 || prev[i]!=prev[i+1]){
            res+=count.toString() + prev[i]
            count = 1
        }
        else{
            count+=1
        }
    }
    
    return res
    
};