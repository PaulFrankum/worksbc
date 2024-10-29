// switch  + - * / invlaid operator and call function 
const {add} = require("./add.js");
const {subtract} = require("./subtract.js");
const {multiply} = require("./multiply.js");
const {divide} = require("./divide.js");
const fs = require("fs");
const path = require("path");
var sum = 0
var result = 0

// input numbers
const firstNumber = Number(process.argv[2])
var operator = process.argv[3]
const secondNumber = Number(process.argv[4])

// check first number
if (typeof(firstNumber) == "NaN"){
  console.log("First Number not a number")
}
// check second number
if (typeof(secondNumber) == "NaN"){
  console.log("Second Number not a number")
}

// switch  + - * / invalid operator and call function 
  switch(operator) {
    case "+":
      sum = (add(firstNumber,secondNumber))
      break;

    case "-": 
      sum = (subtract(firstNumber,secondNumber))
      break;
 
    case "t":
      sum = (multiply(firstNumber,secondNumber))
      operator = "*"
      break;
 
    case "d":
      if (firstNumber==0 || secondNumber==0){
        Console.log("Divide by Zero")
      }
      else{
      sum = (divide(firstNumber,secondNumber))
      operator = "/"
      }
      break;
 
    default:
      sum = "Incorrect operator!"
      console.log("Incorrect operator!")
  }

// print result
result = firstNumber + " "+ operator + " " + secondNumber + " = " + sum +'\n'
console.log(result)

// save to log file
fs.appendFile("calculator.txt", result, (err) => { 
  if (err) throw err;
    console.log("file written successfully!")});

