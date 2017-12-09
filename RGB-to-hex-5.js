function rgb(r, g, b){
    rCol = componentToHex(r).toUpperCase()
    gCol = componentToHex(g).toUpperCase()
    bCol = componentToHex(b).toUpperCase()
    return rCol + gCol + bCol
			    
function check(value) {
    if (value < 0) { value = 0}
    else if (value > 255) { value = 255 }
    return value

function componentToHex(c) {
    if (c < 0) { c = 0 }
    else if (c > 255) {c = 255}
    var hex = c.toString(16);
    return hex.length == 1 ? "0" + hex : hex;
    }
}
