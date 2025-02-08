class Solution {
    public String solution(String myString, String pat) {
        // 인덱스 0 부터 시작해서 pat 문자열 시작 전 인덱스 + pat 길이
        String answer = myString.substring(0, myString.lastIndexOf(pat) + pat.length());
        
        return answer;
    }
}