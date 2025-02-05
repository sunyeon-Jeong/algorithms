class Solution {
    public int solution(int[] date1, int[] date2) {
        int answer = 0;
        
        for (int i = 0; i < date1.length; i++) {
            if (date1[i] < date2[i]) {
                answer = 1;
                break;
            } else if (date1[i] > date2[i]) {
                answer = 0;
                break;
            }
        }
        
        return answer;
    }
}

/*
public int solution(int[] date1, int[] date2) {

        LocalDate dateA = LocalDate.of(date1[0], date1[1], date1[2]);
        LocalDate dateB = LocalDate.of(date2[0], date2[1], date2[2]);

        if (dateA.isBefore(dateB)) {
            return 1;
        } else {
            return 0;
        }
    }
*/