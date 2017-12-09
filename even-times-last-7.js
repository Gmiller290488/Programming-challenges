function evenLast(numbers) {
  var total = 0
  if (numbers.length == 0) {
     return total
  }
  for (var i= 0; i < numbers.length; i+= 2) {
      total += numbers[i]
  }
  return total * numbers.pop()
  }
