import java.util.*;

class Solution {
    public String solution(int q, int r, String code) {
        String answer = "";
        
        String[] codeList = code.split("");
        
        for (int i=0; i<codeList.length; i++) {
            if (i % q == r) {
                answer += codeList[i];
            }
        }
        
        return answer;
    }
}