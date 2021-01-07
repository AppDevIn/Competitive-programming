
#include <iostream> // for input/output
#include <string>   // for string class
using namespace std;


 
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

void printNode(ListNode *node)
{
    if(!node){
        cout << "Empty" << endl;
        return;
    }
    while (node->next)
    {
        cout << node->val << endl;

        node = node->next;
    }
    if (node)
    {
        cout << node->val << endl;
    }
}

ListNode* add(ListNode* l1, ListNode* l2, ListNode* temp, int value){

    if(!l1 && !l2 && value == 0) {

        return temp;
    } else {
        temp->next = new ListNode();
        temp = temp->next;
    }
    if(!l1) l1 = new ListNode();
    if(!l2) l2 = new ListNode();


    if (l1->val + l2->val + value >= 10){
        temp->val = (l1->val + l2->val + value) % 10;
    
        add(l1->next, l2->next, temp, 1);
    } else
    {        
        temp->val = (l1->val + l2->val + value);    
    
        add(l1->next, l2->next, temp, 0)  ; 
    }
    
    
    

    
}

ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    
    
    ListNode* head = new ListNode();
    return add(l1,l2,head, 0);
    
    
}



int main(int argc, char const *argv[])
{
    // ListNode* node = new ListNode(2, new ListNode(4, new ListNode(3)));
    // ListNode* node2 = new ListNode(5, new ListNode(6, new ListNode(4)));

    // printNode(addTwoNumbers(node, node2)->next);

    ListNode* node = new ListNode(9);
    ListNode* node2 = new ListNode(1, new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9))))))))));

    printNode(addTwoNumbers(node, node2));

    return 0;
}

