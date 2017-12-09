// check for palindromes but check vowels and consonents separately
function palindrome(str) {
  str = str.toLowerCase()
  var vowelStr = str.match(/[^ [^\d\s.,\/#!$%\^&\*;:{}=\-_`~()bcdfghjklmnpqrstvwxyz]/ig)
  var constStr = str.match(/[^\d\s.,\/#!$%\^&\*;:{}=\-_`~()aeiou]/ig)
function checkPali(str) {
  if (str.length == 1) {return true}
     var len = Math.floor(str.length / 2);
     for (var i = 0; i < len; i++) {
         if (str[i] !== str[str.length - i - 1]) {
            return false;
        }
        }
  return true;
        }  
  var vowelAns = checkPali(vowelStr)
  var constAns = checkPali(constStr)  
  if (vowelAns == constAns) {
    if (vowelAns == true) { 
       return "both" 
    } else { 
       return "neither"
    }
 } else if (vowelAns == true) { return "vowel" }
   else { return "consonant" }
}
