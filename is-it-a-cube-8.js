// return whether the shape is a cube or not given the volume and length of one side

var cubeChecker = (v, l) => (v && l > 0) ? ((v/l/l) === l ? true : false):false
