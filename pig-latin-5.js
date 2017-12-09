// pig latin
//
function pigIt(str){
   var words = str.split(' ')
   var latinPhrase = []
   for (var i = 0; i < words.length; i++) {
       latinWord = words[i].slice(1) + words[i].slice(0,1) + 'ay '
       latinPhrase.push(latinWord)
  }
   return latinPhrase.join('').slice(0, -1)
  }
