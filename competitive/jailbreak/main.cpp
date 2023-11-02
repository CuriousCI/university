#include <iostream>
#include <vector>

using namespace std;

int main() {
  int test_cases;
  cin >> test_cases;

  while (test_cases--) {
    int height, width;
    cin >> height >> width;

    vector<string> map;
    for (int i = 0; i < height; i++) {
      string line;
      cin >> line;
      map.push_back(line);
    }

    vector<int> starts;
    vector<int> objectives;
    vector<int> adj_list;

    cout << "Test" << endl;

    // vector<vector<int>> adj_list;
    // for (int i = 0; i < height; i++) {
    //   vector<int> vec;
    //   adj_list.push_back(vec);
    // }
  }
}
