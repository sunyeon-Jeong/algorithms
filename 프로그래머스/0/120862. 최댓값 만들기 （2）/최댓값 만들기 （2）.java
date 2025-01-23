import java.util.*;

class Solution {
    public int solution(int[] numbers) {
        // 배열 오름차순 정렬
        Arrays.sort(numbers);
        
        int max1 = numbers[0] * numbers[1];
        int max2 = numbers[numbers.length-2] * numbers[numbers.length-1];
        
        int answer = max1 > max2 ? max1 : max2;
        
        return answer;
    }
}