public class AddTwoNumbers {

    static public class ListNode {
        int val;
        ListNode next = null;
        ListNode(int val) { this.val = val; }
    }

    static public ListNode build_list(int[] array) {
        ListNode head,current;
        head = current = new ListNode(array[0]);

        for(int i = 1; i < array.length ; i ++) {
            current.next = new ListNode(array[i]);
            current = current.next;
        }
        return head;
    }


    static public ListNode addTwoNumbers(ListNode l1,ListNode l2) {
        ListNode rslt = l1;
        ListNode prev = null;
        int val1,val2,carry,sum;
        carry = 0;

        while(l1 != null || l2 != null || carry != 0) {
            val1 = l1 != null ? l1.val : 0;
            val2 = l2 != null ? l2.val : 0;
            sum = val1 + val2 + carry;

            carry = sum / 10;

            if(l1 != null) {
                l1.val = sum % 10;
            }else {
                prev.next = new ListNode(sum % 10);
                l1 = prev.next;
            }

            prev = l1;
            l1 = l1.next;

            if(l2 != null ) {
                l2 = l2.next;
            }

        }

        return rslt;
    } 

    static public void display_list(ListNode l) {
        ListNode current = l;
        while(current != null) {
            System.out.print(current.val + "->");
            current = current.next;
        }
        System.out.print("NULL \n");
    }


    public static void main(String[] args) {
        int[] arr1 = {9,9,9,9,9,9};
        int[] arr2 = {9,9,9};

        ListNode l1 = build_list(arr1);
        ListNode l2 = build_list(arr2);
        display_list(l1);
        display_list(l2);
        ListNode l3 = addTwoNumbers(l1, l2);

        display_list(l3);
    }

}
