import java.util.*;

class Solution {
    public String[] solution(String myStr) {        
        // replace는 반환된 값을 꼭 변수에 담아야 저장됨
        myStr = myStr.replace("a", " ").replace("b", " ").replace("c", " ");
        
        String[] replaced = myStr.trim().split("\\s+");
        
        return replaced.length == 0 || replaced[0].isEmpty() ? new String[] {"EMPTY"} : replaced;
    }
}