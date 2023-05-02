#include <cstddef>
#include <cstdint>
#include <iostream>
#include <math.h>
#include <vector>

using namespace std;

struct Coordinate {
  int32_t x, y;
  Coordinate(int32_t x = 0, int32_t y = 0) : x(x), y(y) {}

  int32_t distance(Coordinate coordinate) {
    return sqrt(pow((coordinate.x - this->x), 2) +
                pow((coordinate.y - this->y), 2));
  }
};

int main() {
  int32_t width, height, possible_positions, max_radius;
  cin >> width >> height >> possible_positions >> max_radius;

  auto cranes = vector<Coordinate>(possible_positions);

  for (auto crane : cranes)
    cin >> crane.x >> crane.y;

  vector<Coordinate> walls_centers = {
      {width / 2, 0},
      {0, height / 2},
      {width / 2, height},
      {width, height / 2},
  };

  auto covered_centers = vector<vector<bool>>(possible_positions);
  for (auto cover : covered_centers)
    cover = vector<bool>(4, false);

  for (size_t crane = 0; crane < cranes.size(); crane++)
    for (size_t center = 0; center < walls_centers.size(); center++)
      covered_centers[crane][center] =
          cranes[crane].distance(walls_centers[center]);

  // auto total = vector<int32_t>(4, 0);
  // for (auto centers : covered_centers) {
  //   for (size_t center = 0; center < centers.size(); center++)
  //     if (centers[center])
  //       total[center]++;
  // }
  //
  // cout << min(min(total[0], total[1]), min(total[2], total[3]));
}
