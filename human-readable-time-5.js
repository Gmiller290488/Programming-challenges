// given time in seconds return the time in HH:mm:ss format
// The code I wrote for this is fairly horrid and I should definitely redo this.
//
function humanReadable(seconds) {
   if (seconds < 10) {
      return "00:00:0" + seconds
     }
   else if (seconds < 60) {
      return "00:00:" + seconds
     }
   else if (seconds == 60) {
      return "00:01:00"
     }
   else if (seconds < 3600) {
      if (Math.floor(seconds/60) <10 ) {
        return "00:0" + Math.floor(seconds/60) + ":" + seconds % 60
      }
      else{
        return "00:" + Math.floor(seconds/60) + ":" + seconds % 60
      }
   }
   else if (seconds == 86400) {
      return "24:00:00"
   }
   else if (seconds == 3600) {
      return "01:00:00"
   }
   else {
      if (Math.floor(seconds/3600) < 10) {
        return "0" + Math.floor(seconds/3600) + ":" + (Math.floor(seconds/60) % 60) + ":" + seconds % 60
        }
      else {
        return Math.floor(seconds/3600) + ":" + (Math.floor(seconds/60) % 60) + ":" + seconds % 60
         }
    }    
 }
