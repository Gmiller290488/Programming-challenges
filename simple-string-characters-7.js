
function solve(s){
  var caps = s.match(/[A-Z]/g).length | 0
  var low = s.match(/[a-z]/g).length | 0
  var num = s.match(/[0-9]/g).length | 0
  var spec = s.length - caps -low - num
  return [caps, low, num, spec]
}
