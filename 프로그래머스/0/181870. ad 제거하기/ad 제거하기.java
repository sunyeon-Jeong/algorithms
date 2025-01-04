import java.util.*;

class Solution {
    public String[] solution(String[] strArr) {
        List<String> newStrArr = new ArrayList<>();
        
        for (String str : strArr) {
            if (!str.contains("ad")) {
                newStrArr.add(str);
            }
        }
        
        String[] answer = newStrArr.toArray(String[]::new);
        
        return answer;
    }
}