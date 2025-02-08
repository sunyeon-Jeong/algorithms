import java.util.*;

class Solution {
    public int solution(String before, String after) {
        int answer = 0;
        
        char[] bef = before.toCharArray();
        char[] aft = after.toCharArray();
        
        Arrays.sort(bef);
        Arrays.sort(aft);
        
        answer = Arrays.equals(bef, aft) ? 1 : 0;
        
        return answer;
    }
}