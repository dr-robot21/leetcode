
import java.util.HashMap;

public class LengthOfLongestSubstring {

    static public int solution(String s) {
        HashMap<Character,Integer> map = new HashMap<>();
        int rslt,left;
        left = rslt = 0;

        for(int right = 0 ; right < s.length() ; right++) {
            if(map.containsKey(s.charAt(right)) && map.get(s.charAt(right)) + 1 > left) {
                left = map.get(s.charAt(right)) + 1;
            }
            map.put(s.charAt(right), right);

            rslt = Math.max(rslt, right - left + 1);
        }
        return rslt;
    }
    public static void main(String[] args) {
        System.out.println(solution("abcabcbb"));   
    }
}
