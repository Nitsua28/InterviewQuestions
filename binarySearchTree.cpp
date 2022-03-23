#include <iostream>
using namespace std;
#include <stdio.h>
#include <stdlib.h>

struct node {
    int key;
    struct node *leftChild, *rightChild; //everynode has two pointers
};


struct node* newNode(int item)
{
    struct node* temp = (struct node*)malloc(sizeof(struct node));
    //every new node is a root with two empty childs
    temp->key = item;
    temp->leftChild = NULL;
    temp->rightChild = NULL;
    return temp;
}


void inorder(struct node* root)
{ //in order is Left->Root->Right
    if (root != NULL) {
        inorder(root->leftChild);
        cout << root->key << endl;
        inorder(root->rightChild);
    }
}

void postorder(struct node* root)
{ //Left -> Right -> root
    if (root != NULL) {
        postorder(root->leftChild);
        postorder(root->rightChild);
        cout << root->key << endl;
    }
}
void preorder(struct node* root)
{ //root -> left -> right
    if (root != NULL) {
        cout << root->key << endl;
        preorder(root->leftChild);
        preorder(root->rightChild);
    }
}
struct node* insert(struct node* node, int input)
{
    //basecase if node is just empty
    if (node == NULL)
        return newNode(input);
    //if key is less than root put to left otherwise right
    if (input < node->key)
        node->leftChild = insert(node->leftChild, input);
    else if (input > node->key)
        node->rightChild = insert(node->rightChild, input);

    return node;
}
struct node* deletion(struct node* root, int key)
{
    // base case
    if (root == NULL)
        return root;
    //find the value by seeing if less than or greater than
    if (key < root->key)
        root->leftChild = deletion(root->leftChild, key);

    else if (key > root->key)
        root->rightChild = deletion(root->rightChild, key);
    //found it
    else {
        // one child
        if (root->leftChild == NULL) {// if right child only
            struct node* temp = root->rightChild;//change pointer to child
            free(root);//deallocates memory of deleted
            return temp;
        }
        else if (root->rightChild == NULL) {//if left child only
            struct node* temp = root->leftChild;
            free(root);//deallocates memory
            return temp;
        }
        //two childs
        struct node* current = root->rightChild;
        //check most min value
        while (current && current->leftChild != NULL)
            current = current->leftChild;
        struct node* temp = current;

        root->key = temp->key;

        root->rightChild = deletion(root->rightChild, temp->key);
    }
    return root;
}
int main()
{
  struct node* BStree = NULL;
  short stoploop = 0;
  while (stoploop == 0)
  {

    string command;
    cin >> command;

    if(command == "i")
        {
            int input;
            cin >> input;
            BStree = insert(BStree, input);
        }
    else if (command == "d")
        {
            int input;
            cin >> input;
            BStree = deletion(BStree,input);
        }
    else if (command == "pre")
            {preorder(BStree);
            cout << "++++++++++++++++++++" << endl;}

    else if (command == "post")
            {postorder(BStree);
            cout << "++++++++++++++++++++" << endl;}
    else if (command == "in")
            {inorder(BStree);
            cout << "++++++++++++++++++++" << endl;}
    else
        stoploop = 1;
  }

    return 0;
}
