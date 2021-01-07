
    ListNode* node = new ListNode(9);
    ListNode* node2 = new ListNode(1, new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9))))))))));

    printNode(addTwoNumbers(node, node2));