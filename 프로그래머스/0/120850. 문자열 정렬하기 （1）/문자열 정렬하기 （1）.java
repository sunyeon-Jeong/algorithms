import java.util.*;
class Solution {
    public int[] solution(String my_string) {
        // 소문자 제거
        my_string = my_string.replaceAll("[a-z]", "");
        // 문자열 -> String 배열
        String[] stringArr = my_string.split("");
        
        // 정수배열 생성
        int[] answer = new int[stringArr.length];
        for (int i = 0; i < stringArr.length; i++) {
            answer[i] = Integer.parseInt(stringArr[i]);
        }
        
        // 배열 오름차순 정렬
        Arrays.sort(answer);
        
        return answer;
    }
}