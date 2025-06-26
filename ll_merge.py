class ListNode:
    def __init__(self, val=0, next=None):
        self.val= val
        self.next= next

class Solution:
    @staticmethod
    def merge(list1, list2):
        dummy= ListNode()
        current= dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next= list1
                list1= list1.next
            else:
                current.next= list2
                list2= list2.next
            current= current.next
        
        current.next= list1 if list1 else list2
        return dummy.next
    @staticmethod
    def build_linked_list(values):
        dummy= ListNode()
        current= dummy
        for val in values:
            current.next= ListNode(val)
            current= current.next
        return dummy.next

list1= Solution.build_linked_list([1,2,4])
list2= Solution.build_linked_list([1,3,4])

merged= Solution.merge(list1,list2)

current= merged
print("[", end="")
while current:
    print(current.val, end= ",")
    current= current.next
print("]")