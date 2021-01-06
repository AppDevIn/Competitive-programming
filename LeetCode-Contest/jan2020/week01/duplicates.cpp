
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
    
    int count = -1;
    while(curr){
        
        if(curr->next){
            if(curr->val == curr->next->val){
                if(!curr->next->next){
                    head = nullptr;
                }
                else if(curr->next->val != curr->next->next->val){
                    head = curr->next->next;
                } else {
                    head = curr->next;
                }
                curr = head;
            }
            else if(!curr->next->next){
                break;
            }
            else if(curr->next->val == curr->next->next->val){
                if(curr->next->next->next->val != curr->next->val){
                    curr->next = curr->next->next->next;
                } else {
                    curr->next = curr->next->next;
                }
            } else{
                curr = curr->next;
            }
        } else {
            break;
        }

        
    }

    return head;

    

    
}


int main(int argc, char const *argv[])
{

    // ListNode* node = new ListNode(1, new ListNode(2, new ListNode(3,  new ListNode(3, new ListNode(3, new ListNode(4, new ListNode(4, new ListNode(5))))))));
    // ListNode* node = new ListNode(1, new ListNode(1, new ListNode(1, new ListNode(2, new ListNode(3)))));
    ListNode* node = new ListNode(1, new ListNode(2, new ListNode(3)));

    node = deleteDuplicates(node);

    printNode(node);
    
    return 0;
}
