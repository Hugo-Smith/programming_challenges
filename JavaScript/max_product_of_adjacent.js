function adjacentElementsProduct(array) {
    let res = array[0]*array[1]
    for (i=1; i<array.length-1;i++){
        let curr = array[i]*array[i+1];
        if (Math.max(curr) > res) {
            res = curr;
        }
    }
  return res
}