function digital_root(n) {
   while (n > 10) {
      var sum = 0
      var nums = (""+n).split("")
      for (var i = 0; i < nums.length; i++) {
         sum += parseInt(nums[i]) 
      }
      n = sum
      }
   return n
}
