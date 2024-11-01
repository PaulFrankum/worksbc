function divide(a, b) {
    if (a==0 || b==0){
        return "Divide by Zero"
    }
    else{
        return a/b;
    }
}

module.exports = { divide };
