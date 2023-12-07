class Solution {
public:
    void reverseString(vector<char>& s) {
        std::vector<char> reverse;
        int n = s.size();
        
        while (n--) {
            reverse.push_back(s[n]);
        }

        s = reverse;
    }
};