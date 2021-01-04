/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        
        std::map<int, int> occurence;
        std::vector<int> nodes;
        
        ListNode *ptr = head;
        
        while (ptr)
        {
            occurence[ptr->val] ++;
            ptr = ptr->next;
        }
        
        for (auto &v : occurence)
        {
            std::cout << v.first << ":" << v.second << std::endl;
            
            if (v.second == 1)
            {
                nodes.push_back(v.first);
            }
            
        }
        
        ListNode* ret = new ListNode(0);

        for (auto &v: nodes)
        {
            
            std::cout << v << std::endl;
            
        }
            
        return ret;
    }
};
