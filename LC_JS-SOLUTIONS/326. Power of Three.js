/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfThree = function(n) {

    if (n<=0){
        return false
    }
    let count = 1
    while (count < n){
        count*=3
    }

    return (count == n)
  
};


// RECURSIVE SOLUTION


/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfThree = function(n) {

    if (n<=0){
        return false
    }
    else if(n===1){
        return true
    }
    else if(n%3===0){
        return isPowerOfThree(n/3)
    }

    return false
    
};
