console.log("Hello World!");
//primitives or value types
let myName; //undefined
let age = 12; // number
let firstName = "Lesley"; //string
let gender = false; // boolean
let score = null; //null
const section = 1;
console.log(typeof(myName));
console.log(typeof age);
console.log(typeof score);
//reference types: objects, arrays and functions
let person = {name:'Lesley', age:20}; // objects
//access objects using dot notation
person.age = 12;
person.name = "Kim";
console.log(person.name);
//access using bracket notation
person['name'] = 'Mary';
//arrays
let selectedColors = ['red','blue'];
selectedColors[2] = 'green';
console.log(selectedColors[0]);
console.log(selectedColors.length);
//functions
function myfunction(myName, lastName){
    console.log('Hello I am a function created by ' + myName + ' '+ lastName);
}
myfunction('Lesley');
//function to calculate value
function square(number){
    return square * square;
}

