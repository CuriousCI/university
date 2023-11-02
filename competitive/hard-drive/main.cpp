#include <iostream>
#include <vector>

using namespace std;

int main() {
  int bits_number, desired_changes, broken_number;
  cin >> bits_number >> desired_changes >> broken_number;

  vector<int> bits;
  vector<bool> broken;

  for (int i = 0; i < bits_number; i++) {
    bits.push_back(0);
    broken.push_back(false);
  }

  for (int i = 0; i < broken_number; i++) {
    int index;
    cin >> index;
    broken[index - 1] = true;
  }

  if (desired_changes == 1) {
    bits[0] = 1;
  } else if (desired_changes % 2 == 0) {
    int changes = 0, index = 1;
    bool prev_changed = false;

    while (changes < desired_changes && index < bits_number) {
      if (!broken[index] && !prev_changed) {
        bits[index] = 1;
        changes += 2;
        prev_changed = true;
      } else
        prev_changed = false;

      index++;
    }
  } else {
    int changes = 1, index = 1;
    bool prev_changed = true;
    bits[0] = 1;

    while (changes < desired_changes && index < bits_number) {
      if (!broken[index] && !prev_changed) {
        bits[index] = 1;
        changes += 2;
        prev_changed = true;
      } else
        prev_changed = false;

      index++;
    }
  }

  for (int i = 0; i < bits_number; i++)
    cout << bits[i];
}
