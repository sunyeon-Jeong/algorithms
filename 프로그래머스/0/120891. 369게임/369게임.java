class Solution {
    public int solution(int order) {
        int answer = 0;
        
        String num = Integer.toString(order);
        String[] numArr = num.split("");
        
        for (int i = 0; i < numArr.length; i++) {
            if (numArr[i].equals("3") || numArr[i].equals("6") || numArr[i].equals("9")) {
                answer += 1;
            }
        }
        
        return answer;
    }
}