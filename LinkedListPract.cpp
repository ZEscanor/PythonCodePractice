#include <iostream>
#include <string>
using namespace std;

typedef struct node
{
	char name;
	struct node* next;
	int count;
	string text;
} node_t;

/*-----
 * Function to take a name and add a new node to the list given by node_t* head. 
 * It returns back the updated list.
 * -----
 */
node_t* add_to_end(char name_to_add, node_t* head)
{
	node_t* newNode = new node_t;
	newNode->name = name_to_add;
	newNode->next = NULL;
	if(head == NULL) // If the list is empty
	{
		head = newNode;
	}
	else // If the list is already populated, traverse to the end of the list and add newNode there.
	{
		node_t* p = head;
		while(p->next!=NULL)
		{
			p = p->next;
		}
		p->next = newNode;
	}
	return head;
}


// Function to remove the text string
node_t* remove(node_t* head,string input){
	node_t* p = head;
	if(head == NULL) // If the list is empty
	{
		return head;
	}
		if(p->text == input){   
		   head->text = "";
		  	while(p->next!=NULL)
		{
			p = p->next;
			delete p;
			p->name = ' ';
		} 
		  
		}
		else
		{
		cout<<"word not found"<<endl;
	}
return p;
}
// function to replace a word if it exists
node_t* replace(node_t* head,string input,string replace){
	node_t* p = head;
	int count = 0;
	if(head == NULL) // If the list is empty
	{
		return head;
	}
		if(p->text == input){   
		   head->text = replace;
		  	while(p->next!=NULL)
		{
			p->name = replace[count];
			p = p->next;
		    count = count+1;
		
		} 
		  
		}
		else
		{
		cout<<"word not found"<<endl;
	}
return p;
}
// function to reverse the input string
char reverse(node_t* head,int count){
 node_t* p = head;
  if(count==0){
  cout<<p->name;
  }
  else{
  
   reverse(p->next,count-1);
   cout<<p->name;
  }
}
// function to search for word
int search(string name,node_t* head){
	int counter = 0;
	int len = name.length();
	node_t* p = head;
	if(head == NULL) // If the list is empty
	{
		cout<<"List is Empty"<<endl;
	}
	else
	{
	do
	{
		if(p->text == name){    //we want to set a p as head because we dont want our original head to be modified by mistake
			return ++counter;  // a counter that will return position if name is found 
		}
		else
		{
		  return 0;
		
	}}while(p!=NULL);
	
     // since our loop will automatically return if person is found we assume if we get to this point the person wasnt found so return -1

	

}
delete p;
}

// Function to print the entire contents of the queue
void print(node_t* head)
{
	if(head == NULL)
	{
		cout << "List is empty!" << endl;
		return;
	}
	cout << "The current list is:\n";
	node_t* p = head;
	do
	{
		cout << p->name;
		p = p->next;
	}while(p!=NULL);
	cout<<endl;
}

int main()
{
	node_t* head = NULL;
	string input;
	string replacez;
    cout<<"What text would you like to enter?"<<endl;
	cin>>input;
	int len = input.length();
	for(int i=0; i<len;i++){
	head = add_to_end(input[i],head);
	head->count = head->count+1;
     }
   head->text = input;
   int count = head->count;
   cout<<"Reversing"<<endl;
   cout<<reverse(head,count)<<endl;
	cout << "Searching"<<endl; 
	cin>>input;
	int s = search(input, head);
	cout<< s<<endl;
	
	cout<<"deleting"<<endl;
	 cin>>input;
    head = remove(head,input);
 
 
	cout<<"printing queue"<<endl;
	print(head);

	cout<<endl;
	cout<<"replace"<<endl;
	cin>>input;
	cout<<"with"<<endl;
	cin>>replacez;
	replace(head,input,replacez);
	print(head);



return 0;
delete head;
}




