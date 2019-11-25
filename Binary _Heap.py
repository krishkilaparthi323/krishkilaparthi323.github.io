class min_heap:
    def __init__(self):
        self.heap=[]

    def root(self, other):
        return (other-1)//2

    def heapify(self,val):
        self.heap.append(val)
        i = len(self.heap)-1
        print("length is",i)
        while(i>=0 and self.heap[self.root(i)]>self.heap[i]):
            print("inside the loop")
            print(self.heap[i])
            print(self.heap[self.root(i)])
            temp = self.heap[i]
            self.heap[i] = self.heap[self.root(i)]
            self.heap[self.root(i)]=temp
            i = self.root(i)
            print(self.heap[i])
            print(self.heap[self.root(i)])
heapobj=min_heap()
heapobj.heapify(10)
heapobj.heapify(30)
heapobj.heapify(63)
heapobj.heapify(58)
heapobj.heapify(44)
print(heapobj.heap)


