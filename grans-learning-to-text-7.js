// Given a string, replace 'to', 'two', 'too', with '2'
function textin(str){
  str1 = str.replace(/(too)/ig, '2')
  str2 = str1.replace(/(two)/ig, '2')
  return str3 = str2.replace(/(to)/ig, '2')
}
