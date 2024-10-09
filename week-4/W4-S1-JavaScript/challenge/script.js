function calculate(firstNumber, secondNumber, calSign) {
  switch (calSign) {
    case "add":
      var c=firstNumber + secondNumber;
      if (typeof c !== 'number') {
        console.log("Invalid input: both arguments must be numbers.")
        }
        else{
        console.log("The sum of the numbers is: " + c)
        }
    break;
    case "subtract":
      var c=firstNumber - secondNumber;
      console.log("The sum of the numbers is: " + c)
    break;
    case "multiply":
      var c=firstNumber * secondNumber;
      console.log("The sum of the numbers is: " + c)
    break;
    case "divide":
      var c=firstNumber / secondNumber;
      console.log("The sum of the numbers is: " + c)
    break;
    default:
      console.log("Unknown operation. Please use 'add', 'subtract', 'multiply', or 'divide'.")
  } 
} 

calculate(10, 5, "add"); // Output: 15
calculate(10, 5, "subtract"); // Output: 5
calculate(10, 5, "multiply"); // Output: 50
calculate(10, 5, "divide"); // Output: 2

calculate(10, "five", "add"); // Output: "Invalid input: both arguments must be numbers."
calculate(10, 5, "square"); // Output: "Unknown operation. Please use 'add', 'subtract', 'multiply', or 'divide'."