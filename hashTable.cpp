#include<bits/stdc++.h>
using namespace std;

class Hash
{
    int BUCKET;

    list<int> *table;
public:
    Hash(int V);


    void insertItem(int x);

    void searchItem(int x);


    void deleteItem(int key);


    int getIndex(int x) {
        return (x % BUCKET);
    }

    void displayHash();
};

Hash::Hash(int b)
{
    this->BUCKET = b;
    table = new list<int>[BUCKET];
}

void Hash::insertItem(int key)
{
    int index = getIndex(key);
    list <int> :: iterator i;
    i = table[index].begin();
    table[index].insert(i,key);
}

void Hash::deleteItem(int key)
{

  int index = getIndex(key);


  list <int> :: iterator i;
  for (i = table[index].begin(); i != table[index].end(); i++) {
        if (*i == key)
        break;
  }


  if (i != table[index].end())
    {
        table[index].erase(i);
        cout << key << " : DELETED" <<endl;
    }
  else
    {
        cout << key << " : DELETE FAILED" <<endl;
    }
}

void Hash::searchItem(int key)
{
    int index = getIndex(key);


  list <int> :: iterator i;
  int count = -1;
  for (i = table[index].begin(); i != table[index].end(); i++) {
        count++;
        if (*i == key)
            break;
  }
  if (i == table[index].end())
    cout << key <<" : NOT FOUND"<< endl;
  else
    {
    cout << key <<" : FOUND AT " << index << "," << count << endl;
    }
}

void Hash::displayHash() { // search O(1) Insertion O(1) Deletion O(1)
  //O(n) space complexity
  for (int i = 0; i < BUCKET; i++) {
    cout << i << " : ";
    cout << table[i][0];
    for (auto x : table[i])
    {
        cout << "->" << x;
    }
    cout << endl;
  }
}


int main()
{

  int size;
  cin >> size;

  short stoploop = 0;
  Hash hash_table(size);
  while (stoploop == 0)
  {

    char first_char;
    cin >> first_char;

    if(first_char == 'i')
        {
            int input;
            cin >> input;
            hash_table.insertItem(input);
        }
    else if (first_char == 'd')
        {
            int input;
            cin >> input;
            hash_table.deleteItem(input);
        }
    else if (first_char == 's')
        {
            int input;
            cin >> input;
            hash_table.searchItem(input);
        }
    else if (first_char == 'o')
        hash_table.displayHash();
    else
        stoploop = 1;
  }
  return 0;
}
