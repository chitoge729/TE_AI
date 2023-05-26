#include <iostream>
using namespace std;

// class Node {
// public:
//     int data;
//     Node* left;
//     Node* right;
// };

// Node* newNode(int data) {
//     Node* node = new Node();
//     node->data = data;
//     node->left = NULL;
//     node->right = NULL;
//     return (node);
// }

// Node* buildBinaryTree() {
//     int data;
//     cout << "Enter the value of the node (or -1 to indicate NULL): ";
//     cin >> data;

//     if (data == -1)
//         return NULL;

//     Node* node = newNode(data);

//     cout << "Enter the left child of " << data << ":" << endl;
//     node->left = buildBinaryTree();

//     cout << "Enter the right child of " << data << ":" << endl;
//     node->right = buildBinaryTree();

//     return node;
// }

// int height(Node* node) {
//     if (node == NULL)
//         return 0;
//     else {
//         int lheight = height(node->left);
//         int rheight = height(node->right);

//         if (lheight > rheight) {
//             return (lheight + 1);
//         }
//         else {
//             return (rheight + 1);
//         }
//     }
// }

// void printLevel(Node* root, int level) {
//     if (root == NULL)
//         return;
//     if (level == 1)
//         cout << root->data << " ";
//     else if (level > 1) {
//         printLevel(root->left, level - 1);
//         printLevel(root->right, level - 1);
//     }
// }

// void printLevelOrder(Node* root) {
//     int h = height(root);
//     for (int i = 1; i <= h; i++)
//         printLevel(root, i);
// }

// void printPreorder(Node* node) {
//     if (node == NULL)
//         return;

//     cout << node->data << " ";
//     printPreorder(node->left);
//     printPreorder(node->right);
// }

// int main() {
//     cout << "Binary Tree Construction\n";
//     Node* root = buildBinaryTree();

//     cout << "\nLevel Order traversal of binary tree is:\n";
//     printLevelOrder(root);

//     cout << "\nPreorder traversal of binary tree is:\n";
//     printPreorder(root);

//     return 0;
// }








class Node
{
	public:
		int data;
		Node* left;
		Node* right;
};

Node* newNode(int data)
{
	Node* node = new Node();
	node->data = data;
	node->left = NULL;
	node->right = NULL;

	return node;
}

Node* buildBinaryTree()
{
	int data;

	cout<<"Enter the node : (-1 for exit)";
	cin>>data;

	if(data == -1)
	{
		return NULL;
	}

	Node* node = newNode(data);

	cout<<"Enter left node of "<<data<<" : "<<endl;
	node->left = buildBinaryTree();

	cout<<"Enter right node of "<<data<<" : "<<endl;
	node->right = buildBinaryTree();

	return node;
}

void Preorder(Node* node)
{
	if(node == NULL)
	{
		return ;
	}	

	cout<<node->data<<"\t";
	
	Preorder(node->left);

	Preorder(node->right);
}

int height(Node* node)
{
	if(node == NULL)
	{
		return 0;
	}
	else
	{
		int lheight = height(node->left);
		int rheight = height(node->right);

		if(lheight > rheight)
		{
			return (lheight + 1);
		}
		else
		{
			return (rheight + 1);
		}
	}
}

void printLevel(Node* node, int level)
{
	if(node == NULL)
	{
		return;
	}

	if(level == 1)
	{
		cout<<node->data<<"\t";
	}
	else if(level > 1)
	{
	printLevel(node->left, level - 1);

	printLevel(node->right, level - 1);
	}
}

void printLevelOrder(Node* node)
{
	int h = height(node);
	for(int i = 1 ; i <= h ; i++)
	{
		printLevel(node, i);
	}
}

int main()
{
	Node* root = buildBinaryTree();
	cout<<"DFS"<<endl;
	Preorder(root);

	cout<<"\nBFS"<<endl;
	printLevelOrder(root);
}