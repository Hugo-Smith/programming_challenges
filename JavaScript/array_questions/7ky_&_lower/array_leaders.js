function arrayLeaders(numbers){
    let sum = numbers.reduce((acc,n) => acc + n, 0);
    let res = [];

    for (let i=0; i < numbers.length; i++){
        sum -= numbers[i]
        if (numbers[i]> sum){
            res.push(numbers[i])
        }
        
    }
  return res;
}