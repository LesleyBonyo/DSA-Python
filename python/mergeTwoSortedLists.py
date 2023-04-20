# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        #newlist = ListNode(val=None, next=None)
        newlist = list1
        if list1 == None and list2 == None:
            return None
        if list1 == None:
            newlist = list2
        elif list2 == None:
            newlist = list1
        else:
            while list1.next != None and list2.next != None:
                if list2.val <= list1.val:
                    newlist.val = list2.val
                    newlist.next = newlist
                    list2 = list2.next
                    #newlist.next = self.mergeTwoLists(list1,list2)
                else:
                    list1 = list1.next
                    newlist.next

                    #newlist.next = list1.val
                    #newlist.next = self.mergeTwoLists(list1,list2)
                list1 = list1.next
                list2 = list2.next

        return newlist
