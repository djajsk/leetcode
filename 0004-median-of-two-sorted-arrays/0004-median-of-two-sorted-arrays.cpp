class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int> ans;
        
        for(int i = 0; i< nums1.size(); i++){
            ans.push_back(nums1[i]);
        }
        for(int i = 0; i<nums2.size(); i++){
            ans.push_back(nums2[i]);
        }
        sort(ans.begin(), ans.end());
        int n = ans.size();
        
        

        if(n% 2 != 0){
            return ans[n/2];}
        else{
            float m = ans[n/2] + ans[n/2-1];
            return m/2;}
       
        
    return ans[n/2];
        
    }
};