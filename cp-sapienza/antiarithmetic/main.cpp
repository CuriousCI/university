#include <cstddef>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <vector>

using namespace std;

int main() {
  uint32_t length;
  char colon;
  cin >> length;

  while (length) {
    cin >> colon;

    auto numbers = vector<int32_t>(length);
    for (auto &number : numbers)
      cin >> number;

    auto positions = vector<int32_t>(numbers.size());
    for (int32_t position = 0; position < numbers.size(); position++)
      positions[numbers[position]] = position;

    bool has_sequence = false;

    for (int32_t first = 0; first < numbers.size(); first++) {
      for (int32_t offset = 1; numbers[first] + offset * 2 < numbers.size();
           offset++) {

        if (positions[numbers[first]] > positions[numbers[first] + offset] &&
            positions[numbers[first] + offset] >
                positions[numbers[first] + 2 * offset]) {
          has_sequence = true;
          break;
        }

        if (positions[numbers[first]] < positions[numbers[first] + offset] &&
            positions[numbers[first] + offset] <
                positions[numbers[first] + 2 * offset]) {
          has_sequence = true;
          break;
        }
      }
      if (has_sequence)
        break;
    }

    cout << (has_sequence ? "no" : "yes") << endl;
    cin >> length;
  }
}
