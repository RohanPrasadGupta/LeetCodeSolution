/**
 * @param {string[]} words
 * @param {string} pref
 * @return {number}
 */
var prefixCount = function(words, pref) {

    let count = 0
    n = pref.length
    for (word in words){
        let temp = words[word].slice(0,n)
        if(temp=== pref){
            count+=1
        }
    }

    return count
    
};