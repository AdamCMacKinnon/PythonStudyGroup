
let array = [1,2,3,4,5];

function reverse(array){
    let newArr = [];

    for(let x = 0; x < array.length; x++){
        newArr.unshift(array[x])
        
    }
    return newArr





}

console.log(reverse(array));