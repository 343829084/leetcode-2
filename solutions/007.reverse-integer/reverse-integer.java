class Solution {
    public int reverse(int x) {
        long rev = 0;
        while (x != 0) {
            int tmp = x % 10;
            rev = rev * 10 + tmp;
            x = x /10;
        }
        
        if (rev > Integer.MAX_VALUE || rev < Integer.MIN_VALUE){
            rev = 0L;
        }
        
        return (int)rev;
    }
}