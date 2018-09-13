class Solution {
    public String longestCommonPrefix(String[] strs) {
        int len = strs.length;
        if (len == 0) {
            return "";
        }
        for(int i = 0; i < strs[0].length(); i++){
            for(int s=0; s<len; s++){
                if(strs[s].length() <= i || strs[s].charAt(i) != strs[0].charAt(i)){
                    return strs[0].substring(0, i);
                }
            }
        }
        
        return strs[0];
        
    }
}