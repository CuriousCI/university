#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

typedef enum { Red, Black } Color;

struct RBTree {
  int value;
  Color color;
  struct RBTree *left, *right, *parent;
};

typedef struct RBTree RBTree;

RBTree *FAKE_LEAF = &(RBTree){0, Black, NULL, NULL, NULL};

// void fix(RBTree *tree) {
//     if (tree->parent == NULL
// }

void insert(RBTree **tree, int value) {
  if (*tree == FAKE_LEAF) {
    *tree = malloc(sizeof(RBTree));
    **tree = (RBTree){value, Red, FAKE_LEAF, FAKE_LEAF, parent};
  } else if (value < (*tree)->value)
    insert(&(*tree)->left, value);
  else
    insert(&(*tree)->right, value);
}

void visit(RBTree *tree, int layer) {
  if (tree == FAKE_LEAF)
    return;

  for (int _ = 0; _ < layer; _++)
    printf(" ");

  if (tree->color == Red)
    printf("\x1b[1;31m");
  else
    printf("\x1b[1;30m\x1b[1;47m");
  printf("%d (%p)\x1b[0m\n", tree->value, tree->parent);
  visit(tree->left, layer + 1);
  visit(tree->right, layer + 1);
}

void rotate_left(RBTree *x) {
  RBTree *parent = x->parent, *y = x->right, *alpha = x->left, *beta = y->left,
         *gamma = x->right;

  if (parent->left == x)
    parent->left = y;
  else
    parent->right = y;
  y->parent = parent;

  y->left = alpha;
  y->right = beta;
  y->left->parent = y;
  y->right->parent = y;

  x->left = beta;
  x->right = gamma;
  x->left->parent = x;
  x->right->parent = x;
}

void rotate_right(RBTree *x) {
  RBTree *parent = x->parent, *y = x->left, *alpha = y->left, *beta = y->right,
         *gamma = x->right;

  if (parent->left == x)
    parent->left = y;
  else
    parent->right = y;
  y->parent = parent;

  y->left = alpha;
  y->right = x;
  y->left->parent = y;
  y->right->parent = y;

  x->left = beta;
  x->right = gamma;
  x->left->parent = y;
  x->right->parent = x;
}

int main() {
  // RBTree *tree = &(RBTree){200, Black, FAKE_LEAF, FAKE_LEAF, NULL};
  RBTree *tree = FAKE_LEAF;
  insert(&tree, 200);
  insert(&tree, 199);
  insert(&tree, 222);
  insert(&tree, 901);
  insert(&tree, 29);
  insert(&tree, 48);
  insert(&tree, 90198);
  insert(&tree, 257);
  visit(tree, 0);
}
