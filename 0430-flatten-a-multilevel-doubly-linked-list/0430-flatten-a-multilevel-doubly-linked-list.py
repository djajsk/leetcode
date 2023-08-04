class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return 
        T = self.traverse(head,[])
        ret_head = Node(T[0])
        curr = ret_head
        ret_head.child = None
        for i in range(1,len(T)):
            new_node = Node(T[i])
            new_node.prev = curr
            new_node.child = None
            curr.next = new_node
            curr = curr.next
        return ret_head
    def traverse(self,head,result):
        if head is None:
            return
        result.append(head.val)
        self.traverse(head.child,result)
        self.traverse(head.next,result)
        return result