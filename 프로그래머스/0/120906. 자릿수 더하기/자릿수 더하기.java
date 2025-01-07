class Solution {
    public int solution(int n) {
        int answer = 0;
        
        while(n > 0) {
            // 마지막 자리수 추출 -> answer에 더하기
            answer += n % 10;
            
            // 마지막 자리수 제거
            n /= 10;
        }
        
        return answer;
    }
}