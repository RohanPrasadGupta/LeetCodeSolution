/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
var reverseStr = function(s, k) {
    s = s.split('')
    for(i=0;i<s.length;i+=2*k){
        let start = i
        let end = Math.min(i+k,s.length)
        s.splice(start, end - start, ...s.slice(start, end).reverse());

    }
    res = s.join('')

    return res
};