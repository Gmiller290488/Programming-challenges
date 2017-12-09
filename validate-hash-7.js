function malwareValidate(hashArr) {
  var index;
  var word = "";
  var finalHashArr = [];
  for (index = 0; index < hashArr.length; ++index) {
     word = hashArr[index];
     var letterCount = word.match(/[0-9]/g || '')
     var charCount = word.match(/[a-z]/g || '')
     if (letterCount != null && charCount !== null && letterCount.length == 5 && charCount.length == 5 && finalHashArr.lastIndexOf(word) < 0) {
        finalHashArr.push(word);
     }
  }
  return finalHashArr;
}
