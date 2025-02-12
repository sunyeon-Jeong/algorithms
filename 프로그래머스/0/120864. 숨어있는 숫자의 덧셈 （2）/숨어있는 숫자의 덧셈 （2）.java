class Solution {
    public int solution(String my_string) {
        int answer = 0;
        
        // 대소문자 제거
        String[] intArr = my_string.split("[a-zA-Z]");
        
        for (int i=0; i<intArr.length; i++) {
            if (! intArr[i].equals("")) {
                answer += Integer.parseInt(intArr[i]);
            }
        }
        
        return answer;
    }
}