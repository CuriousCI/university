#include <algorithm>
#include <cstddef>
#include <cstdint>
#include <iostream>
#include <vector>

using namespace std;

size_t get_index(char gene) {
  switch (gene) {
  case 'A':
    return 0;
  case 'C':
    return 1;
  case 'G':
    return 2;
  };

  return 3;
}

int main() {
  string dna, swine_gene;
  auto costs = vector<int32_t>(4);

  cin >> dna >> swine_gene;
  for (auto &cost : costs)
    cin >> cost;

  int32_t swine_gene_cost = 0;
  for (auto gene : swine_gene)
    swine_gene_cost += costs[get_index(gene)];

  int32_t savings = 0, max_savings = 0, swine_index = 0;
  for (size_t index = 0; index < dna.size() && swine_index < swine_gene.size();
       index++) {
    if (dna[index] == swine_gene[swine_index]) {
      savings += costs[dna[index]];
      swine_index++;
      max_savings = max(savings, max_savings);
    } else if (index + 1 < dna.size() && swine_index + 1 < swine_gene.size()) {
      if (dna[index + 1] == swine_gene[swine_index + 1]) {
        swine_index++;
        savings += costs[get_index(dna[index + 1])];
        max_savings = max(savings, max_savings);
      }
    } else {
      swine_index = 0;
      savings = 0;
    }
  }

  cout << swine_gene_cost - max_savings;
}
