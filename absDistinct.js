function solution(A){
    let countDistinctValue = 0;
    //let newA = [];
    A = A.map(Math.abs);
    A = A.sort();
    /*A = Math.abs(A);
    A.forEach(element => {
        A.push(Math.abs(element));
        console.log(element);
    });*/

    for (let i = 0; i < A.length; i++) {
        //Math.abs(A[i]);
        
        if (A[i] != A[i+1]){
            countDistinctValue += 1;
        } 
    /*if (newA.includes(A[i])) {
        newA = newA
    }else{
        newA.push(A[i]);
        countDistinctValue = newA.length;
        return countDistinctValue;
    }*/
   }
   console.log(A);
    return countDistinctValue;
}

console.log(solution([-5,-3,-1,0,3,6]));