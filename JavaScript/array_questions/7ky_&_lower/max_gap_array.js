function maxGap (numbers) {
    numbers.sort((a,b) => a -b)
    let res = 0
    for (let i = 0; i < numbers.length -1; i ++){
        let diff = numbers[i+1] - numbers[i];
        res = Math.max(diff, res);

    }
    return res
}