function maxTriSum(numbers){
  numbers.sort((a,b) => b-a);
  let newArr = [];
  for (let i = 0; i < numbers.length; i++){
    if (newArr.length === 3){
        return newArr.reduce((acc,n) => acc + n)
    }else if (newArr.includes(numbers[i]) === false){
        newArr.push(numbers[i]);
    }
    i += 1;
  }
}