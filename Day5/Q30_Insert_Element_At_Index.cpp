
class Solution {
public:
    void insertAtIndex(vector<int> &arr, int index, int val) {
        int n = arr.size();

        // Create one extra position
        arr.push_back(0);

        // Shift elements one position to the right
        for (int i = n; i > index; i--) {
            arr[i] = arr[i - 1];
        }

        // Insert the new element
        arr[index] = val;
    }
};
