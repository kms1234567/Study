#include "rbtree.h"
#include <stdlib.h>
#include <stdio.h>

node_t *find_key(node_t *root, node_t *nil, const key_t key);
void free_rbtree(node_t *root, node_t *nil);
void left_rotate(rbtree *t, node_t *x);
void right_rotate(rbtree *t, node_t *x);
void rbtree_insert_fixup(rbtree *t, node_t *z);
void rbtree_erase_fixup(rbtree *t, node_t *x);
void rb_transplant(rbtree *t, node_t *u, node_t *v);
void make_array(node_t *root, node_t *nil, key_t *arr, const size_t n);

rbtree *new_rbtree(void) {
  rbtree *p = (rbtree *)calloc(1, sizeof(rbtree));
  p->nil = (node_t *)calloc(1, sizeof(node_t));
  p->root = p->nil;
  p->nil->color = RBTREE_BLACK;
  return p;
}
void delete_rbtree(rbtree *t) {
  free_rbtree(t->root, t->nil);
  free(t->nil);
  free(t);
  t = NULL;
}
void free_rbtree(node_t *root, node_t *nil) {
  if (root == nil)
    return;
  free_rbtree(root->left, nil);
  free_rbtree(root->right, nil);
  free(root);
  root = NULL;
}

// 좌회전 함수
void left_rotate(rbtree *t, node_t *x) {
  node_t *y = x->right;
  x->right = y->left;
  
  if (y->left != t->nil)
      y->left->parent = x;
  y->parent = x->parent; 
  if (x->parent == t->nil)
      t->root = y; 
  else if (x == x->parent->left)
      x->parent->left = y;
  else
      x->parent->right = y;
  y->left = x;
  x->parent = y;
}

// 우회전 함수
void right_rotate(rbtree *t, node_t *x) {
  node_t *y = x->left;
  x->left = y->right;
  if (y->right != t->nil)
      y->right->parent = x;
  y->parent = x->parent;
  if (x->parent == t->nil)
      t->root = y;
  else if (x == x->parent->right)
      x->parent->right = y;
  else
      x->parent->left = y;
  y->right = x;
  x->parent = y;
}
/*
z : 삽입할 새로운 노드
x : z를 삽입할 위치
y : x의 부모노드. 용이한 연결을 위해 한 칸위인 부모노드를 y로 둠.
*/
node_t *rbtree_insert(rbtree *t, const key_t key) {

  node_t *z = (node_t *)calloc(1, sizeof(node_t));
  node_t *y = t->nil;
  node_t *x = t->root;
  z->key = key;
  // 새 노드 z 삽입할 위치 찾기
  while (x != t->nil) {
    y = x;
    if (key < x->key)
      x = x->left;
    else
      x = x->right;
  }
  z->parent = y;
  // 빈 트리여서 z가 루트일 경우
  if (y == t->nil)
    t->root = z;  
  // 키 삽입할 위치 찾기
  else if (key < y->key)
    y->left = z;
  else
    y->right = z;
  z->left = z->right = t->nil;
  z->color = RBTREE_RED; // 삽입할 노드는 처음에 RED여야 한다.
  rbtree_insert_fixup(t, z);

  return z; 
}

/*
" 루트노드는 BLACK이어야 한다. "
-> 루트노드를 항상 BLACK으로 변경하면 됨. 
BLACK->BLACK, RED->BLACK 두 경우 모두 상관없다.
" RED가 연속해서는 안된다 " 
사실상 double-red 를 수정하기 위한 함수
*/
void rbtree_insert_fixup(rbtree *t, node_t *z) {
  // y는 z의 삼촌(형제)노드이다.
  node_t *y;
    
  while (z->parent->color == RBTREE_RED) {
    // 부모노드가 조상노드의 왼쪽 자식이면 (case 1,2,3)
    if (z->parent == z->parent->parent->left) 
    {
      y = z->parent->parent->right; 
      // case 1: 삼촌노드가 RED인 경우
      if (y->color == RBTREE_RED)
      {
        z->parent->color = RBTREE_BLACK;  
        y->color = RBTREE_BLACK;          
        z->parent->parent->color = RBTREE_RED;  
        z = z->parent->parent;           
      }
      else{
        /*  
        case 2,3: 삼촌노드가 BLACK인 경우
        case 2는 z가 오른쪽 자식인 경우이며 case 3는 왼쪽 자식인 경우이다.
        case 2를 case 3으로 변경시켜주기 위해 left-rotation을 진행한다.
        */
        if (z == z->parent->right) {  
          z = z->parent;              
          left_rotate(t, z);
        }
        // case 3
        z->parent->color = RBTREE_BLACK;        
        z->parent->parent->color = RBTREE_RED;  
        right_rotate(t, z->parent->parent);
      }
    }
    // 부모노드가 조상노드의 오른쪽 자식이면 (case 4,5,6) -> case 1,2,3 과 대칭
    else {
      y = z->parent->parent->left;
      if (y->color == RBTREE_RED)
      {
        z->parent->color = RBTREE_BLACK;
        y->color = RBTREE_BLACK;
        z->parent->parent->color = RBTREE_RED;
        z = z->parent->parent;
      }
      else{
        if (z == z->parent->left) {
          z = z->parent;
          right_rotate(t, z);
        }
        z->parent->color = RBTREE_BLACK;
        z->parent->parent->color = RBTREE_RED;
        left_rotate(t, z->parent->parent);
      }
    }
  }
  t->root->color = RBTREE_BLACK;
}


node_t *rbtree_find(const rbtree *t, const key_t key) {
  return find_key(t->root, t->nil, key);
}
node_t *find_key(node_t *root, node_t *nil, const key_t key) {
  if (root == nil)
    return NULL;
  if (root->key == key)
    return root;
  else if (root->key > key)
    return find_key(root->left, nil, key);
  else
    return find_key(root->right, nil, key);
}

// 왼쪽 최하단 노드를 찾는다.
node_t *rbtree_min(const rbtree *t) {
  node_t *p = t->root;
  while (p->left != t->nil)
    p = p->left;
  return p;
}

// 오른쪽 최하단 노드를 찾는다.
node_t *rbtree_max(const rbtree *t) {
  node_t *p = t->root;
  while (p->right != t->nil)
    p = p->right;
  return p;
}


int rbtree_erase(rbtree *t, node_t *z) {
  node_t *y = z;    
  node_t *x;       
  color_t y_ori_color = y->color;

  if (z->left == t->nil) {
    x = z->right;
    rb_transplant(t, z, z->right);
  }

  else if (z->right == t->nil) {
    x = z->left;
    rb_transplant(t, z, z->left);
  }

  else{
    y = z->right;
    while (y->left != t->nil){
      y = y->left;
    }
    y_ori_color = y->color;
    x = y->right;
    if (y->parent == z)
      x->parent = y;
    else{
      rb_transplant(t, y, y->right);
      y->right = z->right;
      y->right->parent = y;
    }
    rb_transplant(t, z, y);
    y->left = z->left;
    y->left->parent = y;
    y->color = z->color;
  }

  free(z);
  z = NULL;
  if (y_ori_color == RBTREE_BLACK) 
    rbtree_erase_fixup(t, x);
  return 0;
}

/*
double-black 을 수정하기 위한 함수
*/
void rbtree_erase_fixup(rbtree *t, node_t *x) {
  node_t *w; 
  while (x != t->root && x->color == RBTREE_BLACK) {
    if (x == x->parent->left){
      w = x->parent->right;
      
      if (w->color == RBTREE_RED){
        w->color = RBTREE_BLACK;
        x->parent->color = RBTREE_RED;
        left_rotate(t, x->parent);
        w = x->parent->right;
      }
      
      if (w->left->color == RBTREE_BLACK && w->right->color == RBTREE_BLACK) {
        w->color = RBTREE_RED;
        x = x->parent;
      }
      else {
      
        if (w->right->color == RBTREE_BLACK) {
          w->left->color = RBTREE_BLACK;
          w->color = RBTREE_RED;
          right_rotate(t, w);
          w = x->parent->right;
        }

        w->color = x->parent->color;
        x->parent->color = RBTREE_BLACK;
        w->right->color = RBTREE_BLACK;
        left_rotate(t, x->parent);
        x = t->root;
      }
    }

    else {
      w = x->parent->left;
      if (w->color == RBTREE_RED){
        w->color = RBTREE_BLACK;
        x->parent->color = RBTREE_RED;
        right_rotate(t, x->parent);
        w = x->parent->left;
      }
      if (w->right->color == RBTREE_BLACK && w->left->color == RBTREE_BLACK) {
        w->color = RBTREE_RED;
        x = x->parent;
      }
      else {
        if (w->left->color == RBTREE_BLACK) {
          w->right->color = RBTREE_BLACK;
          w->color = RBTREE_RED;
          left_rotate(t, w);
          w = x->parent->left;
        }
        w->color = x->parent->color;
        x->parent->color = RBTREE_BLACK;
        w->left->color = RBTREE_BLACK;
        right_rotate(t, x->parent);
        x = t->root;
      }
    }
  }
  x->color = RBTREE_BLACK;
}

// 기존 u노드위치에 v노드를 대입
void rb_transplant(rbtree *t, node_t *u, node_t *v) {
  if (u->parent == t->nil)
    t->root = v;
  else if (u == u->parent->left)
    u->parent->left = v;
  else
    u->parent->right = v;
  v->parent = u->parent;
}


int idx = 0;
int rbtree_to_array(const rbtree *t, key_t *arr, const size_t n) {
  make_array(t->root, t->nil, arr, n);
  idx = 0;
  return 0;
}
void make_array(node_t *root, node_t *nil, key_t *arr, const size_t n) {
  if (root == nil)
    return;
  if (idx == n)
    return;
  make_array(root->left, nil, arr, n);
  arr[idx] = root->key;
  idx++;
  make_array(root->right, nil, arr, n);
}
