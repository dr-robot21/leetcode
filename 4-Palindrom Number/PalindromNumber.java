public class PalindromNumber {
    public static void main(String[] args) {
        int number = 123321;
        int number2 = 124321;
        System.out.println(solution(number));
        System.out.println(solution(number2));

    }

    public static boolean  solution(int number){
        if (number < 0) {
            return false;
        }

        int reverse = 0;
        int number_cpy = number;

        while (number > 0) {
            reverse = (reverse*10) + (number % 10);
            number /= 10;
        }

        return reverse == number_cpy;
    }
}