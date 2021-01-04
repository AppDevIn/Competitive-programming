
#include <iostream> // for input/output
#include <string>   // for string class
using namespace std;

struct ListNode
{
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

ListNode *insert(ListNode *l, int val)
{

    if (l)
    {
        if (l->val >= val)
        {
            ListNode *n = new ListNode(val, l);
            return n;
        }
        else
        {

            ListNode *temp = l;

            if (temp->next)
            {
                while (temp->next)
                {
                    if (temp->next->val >= val)
                    {

                        ListNode *t = temp->next;
                        ListNode *n = new ListNode(val, t);

                        temp->next = n;

                        return l;
                    }

                    temp = temp->next;
                }
            }
            
            if (temp)
            {

                ListNode *n = new ListNode(val);

                temp->next = n;

                return l;
            }

            return l;
        }
    }

    return l;
}

ListNode *mergeTwoLists(ListNode *l1, ListNode *l2)
{

    if (!l1)
    {
        return l2;
    }
    else if (!l2)
    {
        return l1;
    }
    else
    {
        ListNode *temp = l2;
        while (temp->next)
        {
            l1 = insert(l1, temp->val);
            temp = temp->next;
        }

        if (temp)
        {
            l1 = insert(l1, temp->val);
            temp = temp->next;
        }

        return l1;
    }
}

int main(int argc, char const *argv[])
{
    /* code */
    ListNode *n = new ListNode(1, new ListNode(2, new ListNode(3)));
    n = mergeTwoLists(n, n);
    printNode(n);

    cout << "" << endl;

    ListNode *a = new ListNode(1);
    ListNode *b = new ListNode(2);
    a = mergeTwoLists(a, b);
    printNode(a);

    cout << "" << endl;

    ListNode *c = new ListNode(-9, new ListNode(3));
    ListNode *d = new ListNode(5, new ListNode(7));
    c = mergeTwoLists(c, d);
    printNode(c);


    return 0;
}
