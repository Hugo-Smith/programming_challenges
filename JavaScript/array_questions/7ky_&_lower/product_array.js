function productArray(numbers){
    let prod = numbers.reduce((acc,n) => acc*n);
    let res = [];

    for (let i=0; i < numbers.length; i++){
        res.push(prod/numbers[i]);
    }
    return res
}