function towerBuilder(nFloors) {
  var tower = []
  var line, spaces
  for (var i=1; i < nFloors+1; i++) {
      var count = (i)*2-1
      spaces = " ".repeat(nFloors - i)
      line = "*".repeat(count)
      tower.push(spaces + line + spaces)
      return tower
}
