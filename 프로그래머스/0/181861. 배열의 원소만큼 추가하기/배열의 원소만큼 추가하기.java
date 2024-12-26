import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        List<Integer> answerList = new ArrayList<>();
        
        for (int num : arr) {
            for (int i = 0; i < num; i++) {
                answerList.add(num);
            }
        }
        
        int[] answer = new int[answerList.size()];
        
        for (int i = 0; i < answer.length; i++) {
            answer[i] = answerList.get(i);
        }
        
        return answer;
    }
}