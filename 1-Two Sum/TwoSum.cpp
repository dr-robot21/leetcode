#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;


vector<int> twoSum(vector<int> &list , int target) {
    unordered_map<int , int> map;
    vector<int> output;
    for (int i = 0 ; i < list.size() ; i++) {
        int x = target - list[i];
        if(map.find(x) != map.end()) {
            return {map[x],i};
        }
        map[list[i]] = i;
    }

    return {};
}




int main()
{

    vector<int> arr = {7,6,3,7,9,12,34,5,7};
    vector<int> rslt = twoSum(arr,14);

    cout << rslt[0] << rslt[1] ;
    
    return 0;
}

