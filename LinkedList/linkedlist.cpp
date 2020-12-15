
#include <iostream>

using namespace std;


class MyLinkedList {

   struct Node{
        public:
            int val;
            Node* next;
            Node(int x): val(x), next(nullptr) {}
    };
    
public:

 
    Node* head;
    int size;

    /** Initialize your data structure here. */
    MyLinkedList() {
        size = 0;
        head = nullptr;
    }
    
    /** Get the value of the index-th node in the linked list. If the index is invalid, return -1. */
    int get(int index) {

        Node* curr = head;


        if(index < size && index >= 0){

            for (int i = 0; i < index; i++)
            {
                curr = curr->next;
            }
            
            return curr->val;
            
        }

        return -1;
        
    }
    
    /** Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. */
    void addAtHead(int val) {
        Node* curr = new Node(val);

        curr->next = head;
        head = curr;

        size++;
        
    }
    
    /** Append a node of value val to the last element of the linked list. */
    void addAtTail(int val) {

        if(head==nullptr){
            addAtHead(val);
            return;
        }

        Node* curr = head;

        Node* node = new Node(val);

        while (curr->next)
        {
            curr = curr->next;
        }

        curr->next = node;

        size++;
        
        
    }
    
    /** Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. */
    void addAtIndex(int index, int val) {

        
        if(index == 0) addAtHead(val);
        else if (index == size) addAtTail(val);
        else if(index < size && index > 0){

            Node* curr = new Node(val);
            
            Node* prev = head;


            for (int i = 0; i < index - 1; i++)
            {
                prev = prev->next;
            }

            Node* next = prev->next;

            curr->next = next;

            prev->next = curr;

            size++;

        }

        
    }
    
    /** Delete the index-th node in the linked list, if the index is valid. */
    void deleteAtIndex(int index) {

        Node* curr = head;

        if(index == 0){
            head = head->next;
        }
        else if(index < size && index >= 0){

            for (int i = 0; i < index - 1; i++)
            {
                curr = curr->next;
            }

            Node* temp = curr->next->next;

            curr->next = NULL;

            curr->next = temp;

            size--;



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

    // obj->addAtHead(1);
    // obj->addAtHead(55);
    // obj->addAtTail(3);
    // obj->addAtIndex(1,2);
    // int value1 =obj->get(1);
    // obj->deleteAtIndex(0);
    // int value2 =obj->get(1);

    // cout << value1 << endl;
    // cout << value2 << endl;

    MyLinkedList myLinkedList =  MyLinkedList();
    myLinkedList.addAtHead(7);
    myLinkedList.addAtHead(2);
    myLinkedList.addAtHead(1);
    myLinkedList.addAtIndex(3, 0);    // linked list becomes 1->2->7->0
    myLinkedList.deleteAtIndex(2);    // now the linked list is 1->7->0
    myLinkedList.addAtHead(6);         // now the linked list is 6->1->7->0
    myLinkedList.addAtTail(4);          // now the linked list is 6->1->7->0->4
    cout << myLinkedList.get(4) << endl;              // return 4
    cout << myLinkedList.get(1) << endl;   
    return 0;
}




  
 