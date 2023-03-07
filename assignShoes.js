function assignShoes(shoes){
    let interval = 0;
    let countR = 0;
    let countL = 0
    for (let i = 0; i < shoes.length; i++) {
        //const element = array[index];
        
        if (shoes[i] == 'R') {
            countR += 1;

        }
        else{
            countL += 1;
        }
        if (countL == countR){
            interval += 1;
            countL = 0;
            countR = 0;
        }
        
    }

    return interval;
}

console.log(assignShoes("LLRLRLRLRLRLRR"));
console.log(assignShoes("LLRLRLRLRLRLRR"));