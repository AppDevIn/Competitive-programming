
#include <iostream>

using namespace std;

class MyLinkedList {
private:

    struct ListNode
    {
        int val;
        ListNode* next;
    };
    
    
    ListNode *head;
    int size;
    
    
public:
    /** Initialize your data structure here. */
    MyLinkedList() {
        size = 0;
        head = new ListNode();
    }
    
    /** Get the value of the index-th node in the linked list. If the index is invalid, return -1. */
    int get(int index) {
        ListNode *curr = head;
        
        for(int i= 0; i < index; i++){
            curr = curr->next;
        }
        
        if(curr){
            return curr->val;
        }else{
            return -1;
        }
    }
    
    /** Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. */
    void addAtHead(int val) {

        ListNode *curr = new ListNode();
        curr->val = val;

        //Assign the temp head to the next
        curr->next = head;

        //Make the curr the head
        head = curr;
        
        
        

        
    }
    
    /** Append a node of value val to the last element of the linked list. */
    void addAtTail(int val) {
        
        ListNode *curr = head;
        
        while(curr->next){
            curr = curr->next;
        }
        
        ListNode *node = new ListNode();
        node->val = val;
        
        curr->next = node;
        
    }
    
    /** Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. */
    void addAtIndex(int index, int val) {
        
        ListNode *curr = head;


        if(index != 0){
                        
            for(int i= 0; i < (index-1); i++){
                curr = curr->next;
            }
            
            ListNode *temp = curr->next;

            ListNode *node = new ListNode();
            node->val = val;
            node->next = temp;




            
            curr->next = node;
        }else
        {
            addAtHead(val);
        }
        

        
        
        
        
        
    }
    
    /** Delete the index-th node in the linked list, if the index is valid. */
    void deleteAtIndex(int index) {

        ListNode *curr = head;


        if(index!=0){
        
            for(int i= 0; i < (index-1); i++){
                curr = curr->next;
            }

            ListNode* temp = curr->next->next;


            delete curr->next; 

            curr->next = temp;      
        } else {

            ListNode* temp = curr->next;

            delete curr;

            head = temp;
            

        }
        
    }
};
int main(int argc, char const *argv[])
{
    
    MyLinkedList* obj = new MyLinkedList();


    // obj->addAtHead(1);
    // obj->addAtTail(3);
    // obj->addAtIndex(1,2);
    // obj->get(1);
    // obj->deleteAtIndex(1);
    // obj->get(1);

    // obj->addAtIndex(0,10);
    // obj->addAtIndex(0,20);
    // obj->addAtIndex(1,30);
    // int value1 = obj->get(0);

    obj->addAtHead(1);
    obj->addAtHead(55);
    obj->addAtTail(3);
    obj->addAtIndex(1,2);
    int value1 =obj->get(1);
    obj->deleteAtIndex(0);
    int value2 =obj->get(1);

    cout << value1 << endl;
    cout << value2 << endl;
    return 0;
}




  
 