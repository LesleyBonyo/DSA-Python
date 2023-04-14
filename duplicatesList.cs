/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode DeleteDuplicates(ListNode head) {
        var dummyList = head;
        while(dummyList.next!=null)
        {
            if(dummyList.val == dummyList.next.val){
                dummyList.next = dummyList.next.next;
            }
            else
            {
                dummyList = dummyList.next;
            }
        
        }
        
        
        return head;
    }
}