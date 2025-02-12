import java.util.*;

class Solution {
    public int[] solution(int n) {
        List<Integer> intList = new ArrayList<>();
        
        for (int i=2; i<=n; i++) {
            if (n%i == 0) {
                while (n%i == 0) {
                    n /= i;
                }
                intList.add(i);
            }
        }
        
        int[] answer = new int[intList.size()];
        
        for (int i=0; i<answer.length; i++) {
            answer[i] = intList.get(i);
        }
        
        return answer;
    }
}