#include <iostream>

using namespace std;

int main() {
    size_t sample_size = 111;

    for (size_t cut_position = 0; cut_position < sample_size; cut_position++) {
        int total = 0, current_value = 1;
        for (size_t _ = 0; _ < sample_size; _++) {
            if (_ == cut_position) 
                current_value = 1;

            total += current_value;
            current_value++;
        }

        cout << cut_position << " " << total << endl;
    }
}
