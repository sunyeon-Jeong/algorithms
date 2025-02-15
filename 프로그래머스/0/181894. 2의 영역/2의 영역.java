import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        int first = -1;
        int last = -1;
        
        // 2를 처음만나면 -> first, 그뒤에 2는 last에 계속 덮어씌워짐
        for (int i=0; i<arr.length; i++) {
            if (arr[i] == 2) {
                if (first == -1) {
                    first = i;
                }
                last = i;
            }
        }
        
        // 배열에 2가 없으면
        if (first == -1) {
            return new int[]{-1};
        }
        
        // 부분배열 반환 (copyOfRange)
        return Arrays.copyOfRange(arr, first, last+1);
    }
}