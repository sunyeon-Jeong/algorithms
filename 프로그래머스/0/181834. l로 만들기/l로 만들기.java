class Solution {
    public String solution(String myString) {
        // 정규식(Regex) -> ^는 부정의 의미
        return myString.replaceAll("[^l-z]", "l");
    }
}