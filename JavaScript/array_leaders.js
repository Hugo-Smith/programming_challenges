function arrayLeaders(numbers){
    let prod = numbers.reduce((acc,n) => acc + n, 0);
    let res = [];

    for (i=0; i < numbers.length(); i++){
        if (numbers[i]> prod){
            res.push[numbers[i]]
        }
        prod -= numbers[i]
    }
  return res;
}