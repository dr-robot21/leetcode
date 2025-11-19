#include <iostream>
#include <vector>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};



ListNode* build_list(vector<int> &array) {
    ListNode *head,*current;
    head = current = new ListNode(array[0]);
    for (int i = 1 ; i < array.size() ; i++ ) {
        current->next = new ListNode(array[i]);
        current = current->next;
    }
    return head;
}


void display_list(ListNode *head) {
    ListNode *current = head;
    while (current != nullptr)
    {
        cout << current->val << "->";
        current = current->next;
    }
    cout << "NULL" << endl;
}

void free_list(ListNode *l) {
    ListNode *current = l;
    while (current != nullptr)
    {
        ListNode *tmp = current;
        current = current->next;
        delete tmp;
    }
}


ListNode* addTwoNumbers(ListNode *l1,ListNode *l2) {
    ListNode *rslt,*prev;
    rslt = l1;
    prev = nullptr;
    int carry,val1,val2,sum;
    carry = val1 = val2 = sum = 0;

    while (l1 != nullptr || l2 != nullptr || carry != 0)
    {

        val1 = l1 != nullptr ? l1->val : 0;
        val2 = l2 != nullptr ? l2->val : 0;

        sum = val1 + val2 + carry;
        carry = sum / 10;
    
        if(l1 != nullptr) {
            l1->val = sum % 10;
        }else {
            l1 = new ListNode(sum % 10);
            prev->next = l1;
        }

        prev = l1;
        l1 = l1->next;

        if(l2 != nullptr) l2 = l2->next;
    }

    return rslt;
}




int main() {

    vector<int> arr = {9,9,9,9,9,9,9};
    vector<int> arr2 = {9,9,9,9};
    ListNode *l1 = build_list(arr);
    ListNode *l2 = build_list(arr2);
    ListNode *l3 = addTwoNumbers(l1,l2);

    display_list(l1);
    display_list(l2);
    display_list(l3);

    free_list(l1);
    free_list(l2);
    free_list(l3);
    return 0;
}