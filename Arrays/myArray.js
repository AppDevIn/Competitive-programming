class myArray {

    constructor() {
        this.length = 0
        this.data = {}
    }

    get(index) {
        return this.data[0]
    }

    push(item) {
        this.data[this.length++] = item;
        return this.length;
    }

    pop() {
        const lastitem = this.data[this.length - 1]
        delete this.data[this.length - 1];
        this.length--;
        return lastitem;

    }

    delete(index) {
        const item = this.data[index];
        this.shiftItems(index)
    }

    shiftItems(i) {
        for (let index = i; index < this.length; index++) {
            this.data[index] = this.data[index + 1];
        }

        delete this.data[this.length - 1]
        this.length--;
    }

}



const newArray = new myArray();
console.log(newArray)
newArray.push("test01")
newArray.push("test02")
newArray.push("test03")
newArray.push("test04")
newArray.push("test05")
newArray.push("test06")
console.log(newArray.get(0))
console.log(newArray)
newArray.pop()
console.log(newArray)
newArray.delete(3)
console.log(newArray)