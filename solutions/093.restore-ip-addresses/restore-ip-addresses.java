class Solution {
    public List<String> restoreIpAddresses(String s) {
        ArrayList<String> res = new ArrayList<String>();
        if(s == null || s.length() < 4 || s.length() > 12) return res;
        StringBuilder curIp = new StringBuilder();
        
        dfs(1, 0, s, curIp, res);
        
        return res;
        
    }
    
    private void dfs(int depth, int from, String s, StringBuilder curIp, ArrayList<String> res){
        if(depth == 5){
            if(from == s.length()){
                res.add(curIp.toString().substring(0, from+3));
            }
            return;
        }
        
        for (int i=1; i <= 3 && from+i <= s.length(); i++){
            String curSec = s.substring(from, from + i);
            if(isValid(curSec)){
                curIp.insert(from+depth-1, curSec+".");
                dfs(depth+1, from+i, s, curIp, res);
            }
        }
    }
    private boolean isValid(String s){
        // if(s.length() <= 0) return false;
        if(s.charAt(0) == '0'){
            return s.equals("0");
        }
        
        int n = Integer.parseInt(s);
        return n > 0 && n < 256;
    }
}