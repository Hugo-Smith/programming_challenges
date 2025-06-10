// Objects
const user = {
    name: 'Hugo',
    age: 20,
    practicing: true
};


//functions
function greet(name) {
    return `Hellow, ${name}`;
}

const bye = (name) => {
    return `Goodbye, ${name}`;
};
const byeShort = name => `Goodbye, ${name}`;



//Arrays
const numbers = [1, 2, 3, 4];

// .map() – transform each item
const doubled = numbers.map(n => n * 2); // [2, 4, 6, 8]

// .filter() – keep items that match
const evens = numbers.filter(n => n % 2 === 0); // [2, 4]

// .reduce() – combine items into one value
const sum = numbers.reduce((acc, n) => acc + n, 0); // 10

const fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits.includes("Mango"); //returns true

//array sorts
const nums = [10, 2, 5];
nums.sort();
console.log(nums); // [10, 2, 5] ➜ becomes [10, 2, 5] (not sorted numerically!)

nums.sort((a, b) => a - b);
console.log(nums); // [2, 5, 10]

//array fill
let grid = new Array(10).fill(0) // creates a size 10 array filled with 0s



//conditionals
if (age >= 20) {
    console.log('Old Man');
} else { 
    console.log('Boy');
}

//switch statement
let fruit = "banana";

switch (fruit) {
  case "apple":
    console.log("Apples are red.");
  case "banana":
    console.log("Bananas are yellow."); 
  case "orange":
    console.log("Oranges are orange.");
}


//for loops
for (let i = 0; i < 5; i++) {
  console.log(i);
}

for (let num of numbers) {
  console.log(num);
}
arr = [1,2,3,4,4,5]


//type check
typeof 42 === "number";        // true
typeof "42" === "number";      // false