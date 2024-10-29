// caltest.js

const { add, subtract, multiple, divide } = require("../cal.js");

describe("Add Test", () => {
  test("four calculation for + - t d ", async () => {
    expect(cal.add("10 + 5")).tobe(15);
    expect(cal.subtract("10 - 5")).tobe(5);
    expect(cal.multiple("10 t 5")).tobe(5);
    expect(cal.divide("10 d 5")).tobe(5);
  });

decribe("Invalid Number", () => {
    expect(calculate.division("10 d 0")).tobe("Divide by Zero");
    expect(calculate.division("0 d 10")).tobe("Divide by Zero");
    expect(calculate.subtract("x - 5")).tobe("First Number not a number");
    expect(calculate.multiple("10 - x")).tobe("Second Number not a number");
    expect(calculate.divide("10 x 5")).tobe("Incorrect operator!");
  })
})
