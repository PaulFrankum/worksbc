
// input numbers

// check first number

// check second number

// switch  + - * / invlaid operator and call function 

switch(operator) {
    case "+":
    export function add(a, b) {return a+b};

    case "-": 
    export function subtract(a, b) {return a-b};
    
    case "*":
    export function subtract(a, b) {return a*b};
    
    case "/":
    export function subtract(a, b) {return a/b};
    
    default:
    console.log("Not correct operator")

}
// print result
console.log("sum")
// save to log file
fs.appendFile("Calculator.txt", "sum", (err) => { 
  if (err) throw err;
    console.log(" file written successfully!")});

