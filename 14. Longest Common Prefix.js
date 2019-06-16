var longestCommonPrefix = function(strs) {
  if (strs.length == 0) return "";

  let ans = "";
  i = 0
  while (i < strs[0].length){
    let temp = strs[0][i];
    for (let s of strs){
      if (s[i] !== temp) return ans;
    }
    ans += temp;
    i++;
  }
  return ans;
};
list = ["","",""]
console.log(longestCommonPrefix(list))
