class Solution {
    public int solution(int i, int j, int k) {
        int answer = 0;
        
        String strK = Integer.toString(k);
        
        for (int a = i; a <= j; a++) {
            String str = Integer.toString(a);
            
            if (str.contains(strK)) {
                String[] strArr = str.split("");
                
                for (String s : strArr) {
                    if (s.equals(strK)) {
                        answer++;
                    }
                }
            }
        }
        
        return answer;
    }
}