
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

ListNode* deleteDuplicates(ListNode* head) {
    
    
    ListNode *curr = head;
    ListNode *temp = nullptr;
    
    int duplicate = -101;
    int count = -1;
    while(curr){

            if(curr->val == duplicate){
            }
            else if(curr->next && curr->val == curr->next->val){
                duplicate = curr->val;
    
            } else if(curr->next && curr->next->next && curr->next->val == curr->next->next->val){
                duplicate = curr->next->val;
            }

            if(curr->val == duplicate){
                head = curr->next;
                curr = head;
            }
            else if(curr->next && curr->next->val == duplicate){
                curr->next = curr->next->next;
            } else {
                curr = curr->next;
            }
        

    }

    

    return head;

    

    
}


int main(int argc, char const *argv[])
{

    // ListNode* node = new ListNode(1, new ListNode(2, new ListNode(3,  new ListNode(3, new ListNode(3, new ListNode(4, new ListNode(4, new ListNode(5))))))));
    // ListNode* node = new ListNode(1, new ListNode(1, new ListNode(1, new ListNode(2, new ListNode(3)))));
    // ListNode* node = new ListNode(1, new ListNode(2, new ListNode(3)));
    // ListNode* node = new ListNode(1, new ListNode(2, new ListNode(3)));
    // ListNode* node = new ListNode(1, new ListNode(1));
    // ListNode* node = new ListNode(1);
    // ListNode* node = new ListNode(1, new ListNode(1, new ListNode(2, new ListNode(2))));
    ListNode* node = new ListNode(0, new ListNode(1, new ListNode(2,  new ListNode(2, new ListNode(3, new ListNode(4))))));

    node = deleteDuplicates(node);

    printNode(node);
    
    return 0;
}
