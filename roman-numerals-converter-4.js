// Given a number return the correct roman numeral number
function solution(number){
  var result = '';
  var decimal = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
  var roman = ["M", "CM","D","CD","C", "XC", "L", "XL", "X","IX","V","IV","I"];
  for (var i = 0; i <= decimal.length; i++) {
    while (number % decimal[i] < number) {   
      result += roman[i];
      number -= decimal[i];
    }
  }
  return result;
}

