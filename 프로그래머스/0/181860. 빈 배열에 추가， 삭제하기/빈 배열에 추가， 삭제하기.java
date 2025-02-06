import java.util.*;

class Solution {
    public int[] solution(int[] arr, boolean[] flag) {
        List<Integer> x = new ArrayList<>();
        
        for (int i=0; i < arr.length; i++) {
            
            if (flag[i]) {
                int num = arr[i];
                for (int j=0; j < num*2; j++) {
                    x.add(num);
                }
            } else {
                int num = arr[i];
                for (int j=0; j < num; j++) {
                    x.remove(x.size() - 1);
                }
            }
        
        }
        
        int[] answer = new int[x.size()];
        
        for (int i=0; i < answer.length; i++) {
            answer[i] = x.get(i);
        }
        
        return answer;
    }
}