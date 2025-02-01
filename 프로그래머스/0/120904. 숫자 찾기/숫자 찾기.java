class Solution {
    public int solution(int num, int k) {
        String numStr = Integer.toString(num);
        String[] numArr = numStr.split("");
    
        for (int i = 0; i < numArr.length; i++) {
            if (numArr[i].equals(Integer.toString(k))) {
                return i + 1;
            }
        }
    
        return -1;
    }
}