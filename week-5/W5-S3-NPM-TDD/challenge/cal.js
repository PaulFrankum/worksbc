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

function checkNumber(a, b) {
// check first number
  if (typeof(a) != "number"){
    return "First Number not a number"
  }
  else {
// check second number
    if (typeof(b) != "number"){
      return "Second Number not a number"
    }
    else{
      return "Numbers OK"
    }
  }
}

function calculator(firstNumber, operator, secondNumber){
  if (numberOk=="Numbers OK"){
  // switch  + - * / invalid operator and call function 
    switch(operator) {
      case "+":
        return  (add(firstNumber,secondNumber))
  
      case "-": 
        return  (subtract(firstNumber,secondNumber))
  
      case "x":
        return  (multiply(firstNumber,secondNumber))
  
      case "/":
        return  (divide(firstNumber,secondNumber))
  
      default:
        return "Incorrect operator!"
          }
  }
}

module.exports = { checkNumber, calculator };
numberOk = checkNumber(firstNumber, secondNumber)
sum = calculator(firstNumber, operator, secondNumber)
result = firstNumber + " "+ operator + " " + secondNumber + " = " + sum +'\n'
// print result
// console.log(result)

//  save to log file
fs.appendFile("calculator.txt", result, (err) => { 
if (err) throw err;
  // console.log("file written successfully!")
});