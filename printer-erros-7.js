function printerError(s) {
    var count = s.match(/[n-z]/g || '')
    if (count == null) {
       return ("0/" + s.length)
  } else {
       return (count.length + "/" + s.length)
}
