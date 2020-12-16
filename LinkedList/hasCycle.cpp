/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
#include <iostream>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
 };

class Solution {
public:
    bool hasCycle(ListNode *head) {
        
        if(head == nullptr) return false;
        
        ListNode* slow = head;
        ListNode* fast = head->next;
        
        while(slow != fast){
            
            if(slow == nullptr || fast == nullptr) return false;
            slow = slow->next;
            fast = fast->next->next;
        }
        
        return true;
        
        
        
    }

    ListNode *detectCycle(ListNode *head) {
        
        return 0;
    }
};

int main(int argc, char const *argv[])
{
    Solution s;

    ListNode* n = new  ListNode(3);
    n->next = new ListNode(2);
    n->next->next = new ListNode(0);
    n->next->next->next = new ListNode(-4);
    n->next->next->next = n->next;


    // cout << s.hasCycle(n) << endl;

    s.detectCycle(n);



    return 0;
}
