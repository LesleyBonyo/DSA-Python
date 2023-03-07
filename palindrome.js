function palindrome(x){
    let newX;
    newX = x.toString().split('').reverse();
    newX = newX.join('');
    newX = Number(newX);

    if (x == newX)
    {
        return true;
    } 
    else {
        return false;
    }
}

function palindromeNum(x){
    let newX = x[1];
    console.log(newX);
    

}

console.log(palindromeNum(1212));