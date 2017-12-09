function longest(s1, s2) {
  var joined = s1+s2
  joined = joined.split('').sort();
  var word = joined[0]
  for (var i = 1; i < joined.length; i++) {
      if (joined[i] != joined[i-1]) {
          word += joined[i]
          }
      }
  return word
			    }
