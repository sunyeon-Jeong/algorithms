import java.util.*;

class Solution {
    public int[] solution(int n) {
        List<Integer> numList = new ArrayList<>();
        
        for (int i = 1; i <= n; i++) {
            if (n % i == 0) {
                numList.add(i);
            }
        }
        
        int[] answer = new int[numList.size()];
        
        for (int i = 0; i < answer.length; i++) {
            answer[i] = numList.get(i).intValue();
        }
        
        return answer;
    }
}