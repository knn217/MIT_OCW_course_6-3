#include <stddef.h>
#include <stdlib.h>
#include "bintree.h"

///*** DO NOT CHANGE ANY FUNCTION DEFINITIONS ***///

// Recall node is defined in the header file
node *root = NULL;

// Insert a new node into the binary tree with node_id and data
void insert_node(int node_id, int data) {
    if (root == NULL)
    {
        // malloc root if null
        root = malloc(sizeof(node));
        root->id = node_id;
        root->data = data;
        root->left = NULL;
        root->right = NULL;
        return;
    }
    // this part is like the find node function, but we don't return anything here 
    // we also use pointer here to apply the changes to id and data 
    node* current_node = root;
    while(1)
    {

        if (current_node->id == node_id) // if the id already exist and found
        {
            current_node->data = data; // replace old data with new data
            return;
        }
        else if (current_node->id > node_id) 
        {
            if (current_node->left == NULL)
            {
                current_node->left = malloc(sizeof(node));
                current_node->left->id = node_id;
                current_node->left->data = data;
                current_node->left->left = NULL;
                current_node->left->right = NULL;
                return;
            }
            else current_node = current_node->left;
        }
        else if (current_node->id < node_id) 
        {
            if (current_node->right == NULL)
            {
                current_node->right = malloc(sizeof(node));
                current_node->right->id = node_id;
                current_node->right->data = data;
                current_node->right->left = NULL;
                current_node->right->right = NULL;
                return;
            }           
            else current_node = current_node->right;
        }
    }
    return;
}

// Find the node with node_id, and return its data
int find_node_data(int node_id) {
	node current_node = *root;
    while(1)
    {
        if (current_node.id == node_id) return current_node.data;
        else if (current_node.id > node_id) 
        {
            if (current_node.left == NULL) return 0;
            else current_node = *current_node.left;
        }
        else if (current_node.id < node_id) 
        {
            if (current_node.right == NULL) return 0;            
            else current_node = *current_node.right;
        }
    }
}

///***** OPTIONAL: Challenge yourself w/ deletion if you want ***///
//Find and remove a node in the binary tree with node_id. 
//Children nodes are fixed appropriately.
void remove_node(int node_id) { 
	// ideally, the function should take a pointer to current node 
    // to cut down on searching for nodes that are already found
    node* current_node = root;  
    while(1)
    {

        if (current_node->id == node_id) 
        {
            if (current_node->left != NULL)
            remove_node(current_node->left->id);
            current_node->left = NULL;
            if (current_node->right != NULL)
            remove_node(current_node->right->id);
            current_node->right = NULL;
            free(current_node);
            current_node = NULL;
            return;
        }
        else if (current_node->id > node_id) 
        {
            if (current_node->left == NULL) return;
            else current_node = current_node->left;
        }
        else if (current_node->id < node_id) 
        {
            if (current_node->right == NULL) return;
            else current_node = current_node->right;
        }
    }
    return;
}

