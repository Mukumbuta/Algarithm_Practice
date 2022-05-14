//Solution #1: Manual

function removeOdd(arr){
    let oddNums = [];

    for(let number of arr){
        if(number % 2 != 0)
            oddNums.push(number);
    }
    return oddNums;
}

let randomNums = [3, 5, 6, 8, 7, 11, 23, 9, 34];
console.log(removeOdd(randomNums));


//Solution #2: Lambda Function

function removeOdd(arr){
    return arr.filter((number => (number % 2) === 0))
}

let randNums = [3, 5, 6, 8, 7, 11, 23, 9, 34];
console.log(removeOdd(randNums));



// Remove Even numbers
function removeEven(arr){
    return arr.filter((number => (number % 2) != 0))
}

let someRandNums = [3, 5, 6, 8, 7, 11, 23, 9, 34];
console.log(removeEven(someRandNums));
