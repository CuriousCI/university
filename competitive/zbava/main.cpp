#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
    int students_number, buildings_number, evictions_number;
    cin >> students_number >> buildings_number >> evictions_number;

    auto buildings = vector<int>();
    for (size_t _ = 0; _ < buildings_number; _++)
        buildings.push_back(0);

    for (size_t _ = 0; _ < students_number; _++) {
        int building;
        cin >> building;
        building--;
        buildings[building]++;
    }


    auto buildings_students_numbers = priority_queue<int>();

    for (auto building : buildings)
        buildings_students_numbers.push(building);
    
    while (evictions_number-- && buildings_students_numbers.size() > 0) {
        auto students = buildings_students_numbers.top();
        cout << students << endl;
        buildings_students_numbers.pop();

        if (students % 2 == 0) {
            buildings_students_numbers.push(students / 2);
            buildings_students_numbers.push(students / 2);
        } else {
            buildings_students_numbers.push((students - 1) / 2);
            buildings_students_numbers.push((students + 1) / 2);
        }
    }

    int noise_level = 0;
    cout << endl;
    while (buildings_students_numbers.size()) {
        auto students = buildings_students_numbers.top();
        cout << students << endl;
        buildings_students_numbers.pop();
        noise_level += (students * (students + 1)) / 2;
    }

    cout << noise_level << endl;
}
