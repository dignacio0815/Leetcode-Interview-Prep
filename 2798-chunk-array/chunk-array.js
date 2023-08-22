/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array[]}
 */
var chunk = function(arr, size) {
    const array = [];
    let tempVal = 0;
    let i = 0;
    while(i < arr.length) {
        array.push(arr.slice(i, i + size))
        i += size
    }
    
    return array;
};
