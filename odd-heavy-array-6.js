// An array is considered odd heavy if there are no even numbers larger than the smallest odd number
function isOddHeavy(n){
  var evenHigh = "", oddLow = ""
  for (var i = 0; i < n.length; i++) {
    if (n[i] % 2 == 0) {
      if (evenHigh === "") { evenHigh = n[i] }
         if (n[i] > evenHigh) {
            evenHigh = n[i] 
	         }
            }
    else {
      if (oddLow == "") { oddLow = n[i] }
         if (n[i] < oddLow) {
           oddLow = n[i]
	         }
     	      }
   	  }
  if (evenHigh === "" && oddLow === "") { return false }
     else if (evenHigh === "") { return true}
     else if (oddLow === "") { return false }
  if (evenHigh < oddLow) {
     return true
 	  }
  else {
     return false
 	  }
 	}
