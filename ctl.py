/*
 * Complete the function below.
 */

/* Utility Functions to get max and minimum of two integers */
    function max(x, y) 
    {
        return Math.max(x, y);
    }
 
    function min(x, y) 
    {
        return Math.min(x, y);
    }
 

function maxDifference(a) {
   
   var totalDiff = 0;
   var i = 0;
   var j = 0;
   
   var RMax = [];
   var LMin = [];
    
   /* Construct LMin[] such that LMin[i] stores the minimum value
           from (arr[0], arr[1], ... arr[i]) */
  
   LMin[0] = a[0];
   for(i = 1; i < a.length; ++i){
       LMin[i] = min(arr[i], )
   }
    
   
   for(var i = 1; i < a.length; i ++){
       current = a[i];
       var diff = [];
       for(var j = 0; j < i; j ++){
           diff.push(current - a[j]); 
       }
       total_diff.push(Math.max.apply(null, diff));
   }
   
   return Math.max.apply(null, total_diff);
}

