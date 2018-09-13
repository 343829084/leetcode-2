class Solution {
    public boolean isValid(String s) {
        char[] stack = new char[s.length() + 1];
        int top = 1;  // top is null
        for(int i=0; i < s.length(); i++){
            char c = s.charAt(i);
            if(c == '(' || c == '[' || c == '{') {
                stack[top++] = c;
            } else if(c == ')' && stack[--top] != '('){
                return false;
            }else if(c == ']' && stack[--top] != '['){
                return false;
            }else if(c == '}' && stack[--top] != '{'){
                return false;
            }
        }
        return top == 1;
    }
}