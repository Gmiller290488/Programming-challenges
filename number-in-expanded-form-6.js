// if given 12 return 10+2
function expandedForm(num) {
  var digits = num.toString()
  digits.split()
  var line = []
     for (var i = 0; i < digits.length; i++) {
        if (digits[i] != 0) {
          if (i == 0) {
             line.push(digits[i] + "0".repeat(digits.length - i -1))
        } else if (i != 0) {
            line.push(" + " + digits[i] + "0".repeat(digits.length - i -1))
        }
     }
      }
  return line.join('')
		        }
