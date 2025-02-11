class Solution {
    public int solution(String num_str) {
        int answer = 0;
        
        for (int i=0; i < num_str.length(); i++) {
            int num = Integer.parseInt(num_str.substring(i, i+1));
            answer += num;
        }
        
        return answer;
    }
}