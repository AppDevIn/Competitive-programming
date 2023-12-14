class MyQueue {
    Stack<Integer> stack;
    public MyQueue() {
        stack = new Stack<>();
    }
    
    public void push(int x) {
        Stack<Integer> newStack = new Stack<>();
        int[] numbers = new int[stack.size()];
        newStack.push(x);
    
        int index = 0;
        while(!this.stack.empty()) {
            numbers[index] = stack.pop();
            index++;
            
        }
        
        for(int i = numbers.length-1; i >= 0; i--) {
            newStack.push(numbers[i]);
        }
        this.stack = newStack;
        
    }
    
    public int pop() {
        return this.stack.pop();
    }
    
    public int peek() {
        return this.stack.peek();
    }
    
    public boolean empty() {
        return this.stack.empty();
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */
