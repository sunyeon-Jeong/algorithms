class Solution {
    public int solution(String binomial) {
        // 이항식을 공백을 기준으로 분리
        String[] binomialArr = binomial.split(" ");
        
        int a = Integer.parseInt(binomialArr[0]);
        String op = binomialArr[1];
        int b = Integer.parseInt(binomialArr[2]);
        
        int answer = 0;
        
        if (op.equals("+")) {
            answer = a + b;
        } else if (op.equals("-")) {
            answer = a - b;
        } else if (op.equals("*")) {
            answer = a * b;
        }
        
        return answer;
    }
}