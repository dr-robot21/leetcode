
import java.util.HashMap;



public class TwoSum {
    public static void main(String[] args) {
        int[] arr = {7,2,11,13,12,11,5};
        int[] output = solution(arr, 18);

        System.out.println(output[0] + "," + output[1]);
    }

    static public int[] solution(int[] nums , int target) {
        HashMap<Integer,Integer> map = new HashMap<>();
        int x;
        int[] output = new int[2];

        for (int i = 0; i < nums.length; i++) {
            x = target - nums[i];
            if (map.containsKey(x)) {
                output[0] = i; output[1] = map.get(x);
                return output;
            }
            map.put(nums[i], i);
        }
        return  output;
    }
}