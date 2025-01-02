class Solution {
    public int solution(String myString, String pat) {
        int answer = 0;
        
        String replaceString = myString.replace('A', 'X').replace('B', 'A').replace('X', 'B');
        
        if (replaceString.contains(pat)) {
            answer = 1;
        }
        
        return answer;
    }
}