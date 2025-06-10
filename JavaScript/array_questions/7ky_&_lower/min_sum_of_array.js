function minSum(arr) {
    arr.sort((a,b) => a - b);
    let lp = 0;
    let rp = arr.length-1;
    let total = 0

    while (lp < rp){
        total += (arr[lp]*arr[rp]);
        lp ++;
        rp --;
    }
    return total
}

let arr = [5,4,2,3]
print(minSum(arr))