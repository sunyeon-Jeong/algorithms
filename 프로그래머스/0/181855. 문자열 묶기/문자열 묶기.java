class Solution {
    public int solution(String[] strArr) {
        int answer = 0;
        int[] cnt = new int[30];
        
        for (int i=0; i<strArr.length; i++){
            cnt[strArr[i].length() - 1]++;
        }
        
        for (int j : cnt) {
            if (answer < j) {
                answer = j;
            }
        }
        
        return answer;
    }
}