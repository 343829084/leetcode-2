class Solution {
    public int strStr(String haystack, String needle) {
        int lh = haystack.length();
        int ln = needle.length();
        if(ln > lh){
            return -1 ;
        }
        for(int i= 0; i <= lh-ln; i++)
        {
            for(int j=0; j<=ln; j++){
                if(j == ln){
                    return i;
                }
                if (haystack.charAt(i+j) != needle.charAt(j)){
                    break;
                }
            }
        }
        return -1;
    }
}