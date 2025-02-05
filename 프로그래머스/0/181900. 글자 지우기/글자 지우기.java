class Solution {
    public String solution(String my_string, int[] indices) {
        String answer = "";
        
        String[] stringArr = my_string.split("");
        
        for (int i = 0; i < indices.length; i++) {
            stringArr[indices[i]] = "";
        }
        
        for (String s : stringArr) {
            answer += s;
        }
        
        return answer;
    }
}