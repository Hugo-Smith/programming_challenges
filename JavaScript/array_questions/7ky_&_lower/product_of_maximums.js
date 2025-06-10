 function maxProduct(numbers, size){
    numbers.sort((a,b) => b-a)
    let res = numbers[0];
    for (i=1; i < size; i++){
        res *= numbers[i]
    }
    return res
}

//alternate solution
function maxProduct(numbers, size){
  return numbers.sort((a,b) => b-a).slice(0,size).reduce((acc,n) => acc*n);
}