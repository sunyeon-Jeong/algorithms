class Solution {
    public String[] solution(String my_str, int n) {
        int length = 0;
        
        if (my_str.length() % n == 0) {
            length = my_str.length() / n;
        } else {
            length = my_str.length() / n+1;
        }
        
        String[] answer = new String[length];
        
        for (int i=0; i<length; i++) {
            if (my_str.length() >= n) {
                answer[i] = my_str.substring(0, n);
                my_str = my_str.substring(n, my_str.length());
            } else {
                answer[i] = my_str.substring(0, my_str.length());
            }
        }
        
        return answer;
    }
}