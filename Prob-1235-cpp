class Solution {
public:
    int numberOfBeams(vector<string>& bank) {
        vector<int> arr;
        int n = bank.size();
        int answer=0;
        int x=0;
        for(int i =0;i<n;i++){
            string R= bank[i];
            int C =count(R.begin(), R.end(), '1');
            if(C>0){
                x++;
                arr.push_back(C);
                if (x>1){
                    answer+=arr[x-1]*arr[x-2];
                }
            }
        }
        return answer;
    }
};
