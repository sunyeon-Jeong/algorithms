class Solution {
    public int solution(int[] arr1, int[] arr2) {
        int answer = 0;
        
        int arr1_sum = 0;
        int arr2_sum = 0;
        int arr1_length = arr1.length;
        int arr2_length = arr2.length;
        
        for (int i=0; i<arr1_length; i++) {
            arr1_sum += arr1[i];
        }
        for (int j=0; j<arr2_length; j++) {
            arr2_sum += arr2[j];
        }
        
        if (arr1_length != arr2_length) {
            if (arr1_length > arr2_length) {
                answer = 1;
            } else {
                answer = -1;
            }
        } else {
            if (arr1_sum > arr2_sum) {
                answer = 1;
            } else if (arr1_sum < arr2_sum) {
                answer = -1;
            } else if (arr1_sum == arr2_sum) {
                answer = 0;
            }
        }
        
        return answer;
    }
}