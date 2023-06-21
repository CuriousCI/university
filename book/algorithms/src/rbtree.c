#include <stdio.h>
#include <stdlib.h>

typedef enum { Red, Black } Color;
typedef struct RBTree RBTree;

struct RBTree {
  int value;
  Color color;
  struct RBTree *left, *right, *parent;
};

RBTree *FAKE_LEAF = &(RBTree){0, Black, NULL, NULL, NULL};

void rotate_left(RBTree *x) {
  RBTree *parent = x->parent, *y = x->right;
  RBTree *alpha = x->left, *beta = y->left, *gamma = x->right;

  if (parent != NULL) {
    if (parent->left == x)
      parent->left = y;
    else
      parent->right = y;
  }
  y->parent = parent;

  y->left = x;
  x->parent = y;
  x->left = alpha;
  x->right = beta;
  alpha->parent = x;
  beta->parent = x;
}

void rotate_right(RBTree *x) {
  RBTree *parent = x->parent, *y = x->left;
  RBTree *alpha = y->left, *beta = y->right, *gamma = x->right;

  if (parent != NULL) {
    if (parent->left == x)
      parent->left = y;
    else
      parent->right = y;
  }
  y->parent = parent;

  y->left = alpha;
  y->right = x;
  alpha->parent = y;
  x->parent = y;
  x->left = beta;
  x->left->parent = y;
}

void fix(RBTree *tree) {
  if (tree->parent == NULL) {
    tree->color = Black;
    return;
  }

  if (tree->parent->parent == NULL || tree->parent->color == Black)
    return;

  RBTree *grandpa = tree->parent->parent, *father = tree->parent;
  RBTree *uncle = grandpa->left == father ? grandpa->right : grandpa->left;

  if (uncle->color == Red) {
    father->color = Black;
    uncle->color = Black;
    grandpa->color = Red;
    fix(grandpa);
  } else if (father->right == tree) {
    rotate_left(father);
    fix(father);
  } else if (father->left == tree) {
    if (grandpa->left == father) {
      rotate_right(grandpa);
      grandpa->color = Red;
      father->color = Black;
    } else {
      rotate_left(grandpa);
      grandpa->color = Red;
      father->color = Black;
      fix(tree);
    }
  }
}

void insert_with_parent(RBTree **tree, RBTree *parent, int value) {
  if (*tree == FAKE_LEAF) {
    *tree = malloc(sizeof(RBTree));
    **tree = (RBTree){value, Red, FAKE_LEAF, FAKE_LEAF, parent};
    fix(*tree);
  } else if (value < (*tree)->value)
    insert_with_parent(&(*tree)->left, *tree, value);
  else
    insert_with_parent(&(*tree)->right, *tree, value);
}

void insert(RBTree **tree, int value) {
  insert_with_parent(tree, NULL, value);
  if ((*tree)->parent != NULL)
    *tree = (*tree)->parent;
}

void visit(RBTree *tree, int layer) {
  for (int _ = 0; _ < layer; _++)
    printf(" ");

  if (tree == FAKE_LEAF) {
    printf("\x1b[1;30m\x1b[1;47m-\x1b[0m\n");
    return;
  }

  if (tree->color == Red)
    printf("\x1b[1;31m");
  else
    printf("\x1b[1;30m\x1b[1;47m");
  printf("%d\x1b[0m\n", tree->value);
  visit(tree->left, layer + 1);
  visit(tree->right, layer + 1);
}

int main() {
  RBTree *tree = FAKE_LEAF;

  int values[] = {11, 14, 15, 2, 1, 7, 5, 8, 4};
  int SIZE = 9;

  for (int *value = values; value < values + SIZE; value++)
    insert(&tree, *value);

  visit(tree, 0);
}
