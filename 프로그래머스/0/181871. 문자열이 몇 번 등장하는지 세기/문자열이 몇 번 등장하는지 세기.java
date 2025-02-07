class Solution {
    public int solution(String myString, String pat) {
        int answer = 0;
        
        for (int i = myString.length()-1; i >= 0; i--) {
            String subString = myString.substring(0, i+1);
            
            if (subString.endsWith(pat)) {
                answer++;
            }
        }
        
        return answer;
    }
}