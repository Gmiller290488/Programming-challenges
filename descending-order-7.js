function descendingOrder(n){
   nums = (""+n).split("").map(function(t){return parseInt(t)}).sort().reverse().join("")
   return parseInt(nums)
			   }
