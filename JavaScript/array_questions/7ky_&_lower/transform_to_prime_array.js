function minimumNumber(numbers) {
    const sum = numbers.reduce((acc, n) => acc + n);
    let res = 0;

    while (true) {
        let n = sum + res;
        let isPrime = true;

        for (let i = 2; i * i <= n; i++) {
            if (n % i === 0) {
                isPrime = false;
                break;
            }
        }

        if (isPrime) {
            return res;
        }

        res += 1;
    }
}
