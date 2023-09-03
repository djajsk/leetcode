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
        int s = 0;
        int e = n-1;
        int m = (s+e)/2;

        if(n% 2 != 0){
            return ans[m];}
        else{
            float res = ans[n/2] + ans[n/2 - 1];
                return res/2;
        }
        
        
    return ans[m]; 
        
        
        
    }
};