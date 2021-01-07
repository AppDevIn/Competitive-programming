
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

string add(ListNode* l1){
    if(!l1){ 
        return "";
    }    
    return add(l1->next) + to_string(l1->val);
}

ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    
    string val1 = add(l1);
    string val2 = add(l2);

    long total = stol(val1) + stol(val2);

    
    char v =  to_string(total)[to_string(total).length()-1];
    ListNode* head = new ListNode(int(v)-48);
    ListNode* temp = head;
    for (int i = to_string(total).length()-2; i >= 0 ; i--)
    {
        char v =  to_string(total)[i];
        temp->next = new ListNode(int(v)-48);
        temp = temp->next;
        
    }

    return head;
    
    
}



int main(int argc, char const *argv[])
{
    // ListNode* node = new ListNode(2, new ListNode(4, new ListNode(3)));
    // ListNode* node2 = new ListNode(5, new ListNode(6, new ListNode(4)));

    // printNode(addTwoNumbers(node, node2));

    ListNode* node = new ListNode(9);
    ListNode* node2 = new ListNode(1, new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9))))))))));

    printNode(addTwoNumbers(node, node2));

    return 0;
}

