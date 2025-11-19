#include <iostream>
#include <unordered_map>
using namespace std;

int lengthOfLongestSubstring(string s) {
    unordered_map<char,int> map;
    int rslt,left;
    rslt = left = 0;

    for(int right = 0 ; right < s.size() ; right++ ) {
        if(map.find(s[right]) != map.end() && map[s[right]] + 1 > left) {
            left = map[s[right]] = right;
        }
        map[s[right]] = right;

        rslt = max(rslt,right - left + 1);
    }

    return rslt;
}


int main() {

    cout << lengthOfLongestSubstring("abcabcbb");
    return 0;
}