import java.util.*;

class Solution {
    public String solution(String s) {
        String answer = "";
        
        String[] strArr = s.split("");
        Arrays.sort(strArr);
        
        int cnt = 0;
        for (int i=0; i<strArr.length; i++) {
            cnt = 0;
            for (int j=0; j<strArr.length; j++) {
                if (strArr[i].equals(strArr[j])) {
                    cnt++;
                }
            }
            
            if (cnt==1) {
                answer += strArr[i];
            }
        }
        
        return answer;
    }
}