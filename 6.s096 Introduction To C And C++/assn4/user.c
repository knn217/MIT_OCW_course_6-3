#include <stdio.h>
#include "bintree.h"

int main() {
	/*
	Insert your test code here. Try inserting nodes then searching for them.

	When we grade, we will overwrite your main function with our own sequence of
	insertions and deletions to test your implementation. If you change the
	argument or return types of the binary tree functions, our grading code
	won't work!
	*/
	insert_node(5, 15);
	insert_node(4, 24);
	insert_node(0, 30);
	insert_node(3, 43);
	insert_node(9, 59);
	insert_node(7, 67);

	printf("%d", find_node_data(3));

	remove_node(5); // this should be the root node and will remove all nodes
	return 0;
}
