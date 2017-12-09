function accum(s) {
   var letters = s.split("")
   var finished = ""
   for (index = 0; index < letters.length; ++index) {
       for (count = -1; count < index; ++count) {
           if (count == -1) {
               finished += letters[index].toUpperCase()
         } else {
               finished += letters[index].toLowerCase()
                }
          }
       finished += '-'
   }
   return finished.slice(0, -1);
}
