class Solution {
    public String solution(String my_string, int s, int e) {
        String answer = my_string.substring(0, s);
        
        String strSub = my_string.substring(s, e+1);
        
        String[] strArr = strSub.split("");
        
        for (int i = strArr.length - 1; i >= 0; i--) {
            answer += strArr[i];
        }
        
        answer += my_string.substring(e+1);
        
        return answer;
    }
}