// caltest.js

// 
const { calculator, checkNumber } = require("../cal.js");
const { add } = require("../add.js");
const { subtract } = require("../subtract.js");
const { multiply } = require("../multiply.js");
const { divide } = require("../divide.js");

describe("add", () => {
  test("add.js", async () => {
  expect(add(10, 5)).toBe(15);
  expect(add(-5, 10)).toBe(5);
  expect(add(0, 5)).toBe(5);
 })});

 describe("subject", () => {
  test("subtract.js", async () => {
    expect(subtract(10, 5)).toBe(5);
    expect(subtract(0, -10)).toBe(10);
    expect(subtract(0, 5)).toBe(-5);
})});

describe("multiply", () => {
  test("multiply.js", async () => {
    expect(multiply(10, 5)).toBe(50);
    expect(multiply(-5, 10)).toBe(-50);
    expect(multiply(0, 5)).toBe(0);
    expect(multiply(3.141, 5)).toBe(15.705);
})});

describe("divide", () => {
  test("divide.js", async () => {
    expect(divide(10, 5)).toBe(2);
    expect(divide(-10, 5)).toBe(-2);
    expect(divide(3.14, 1.57)).toBe(2);
    expect(divide(10, 0)).toBe("Divide by Zero");
    expect(divide(0, 10)).toBe("Divide by Zero");
})});

describe("operatorTest", () => {
  test("calculator", async () => {
    expect(calculator(10, "+", 5)).toBe(15);
    expect(calculator(10, "-", 5)).toBe(5);
    expect(calculator(10, "x", 5)).toBe(50);
    expect(calculator(10, "/", 5)).toBe(2);
    expect(calculator(10, "W", 5)).toBe("Incorrect operator!");
    expect(calculator(10, "add", 5)).toBe("Incorrect operator!");
    
  })});

describe("checkNumbers", () => {
  test("checkNumber", async () => {
    expect(checkNumber("c", 5)).toBe("First Number not a number");
    expect(checkNumber(10, "five")).toBe( "Second Number not a number");
    expect(checkNumber("a", 5)).toBe("First Number not a number");
    expect(checkNumber(10, "b")).toBe("Second Number not a number");
    expect(checkNumber(10, 5)).toBe("Numbers OK");
})});

// "file written successfully!"