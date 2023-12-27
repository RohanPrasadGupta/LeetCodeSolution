/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArray = function(nums) {

    function merge(arr,L,M,R){
        let left = arr.slice(L,M+1)
        let right = arr.slice(M+1,R+1)
        let i = L, j = 0, k = 0
        while(j<left.length && k<right.length){
            if(left[j] <= right[k]){
                arr[i] = left[j]
                j+=1
            }
            else{
                arr[i] = right[k]
                k+=1
            }
            i+=1
        }
        while(j<left.length){
            arr[i] = left[j]
            i+=1
            j+=1
        }
        while(k<right.length){
            arr[i] = right[k]
            i+=1
            k+=1
        }
    }

    function sortArray(arr,l,r){
        if(l===r){
            return arr
        }
        let m = Math.floor((l+r)/2)
        sortArray(arr,l,m)
        sortArray(arr,m+1,r)
        merge(arr,l,m,r)
        return arr
    }

    return sortArray(nums,0,nums.length-1)
};