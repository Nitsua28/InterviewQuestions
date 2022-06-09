'''
/*
2. IntegerReductionCount
Given a number N and two reduction operations, count the number of operations required to reduce
N to 0.

You are given a string S of length N which encodes a non-negative number V in a binary form. Two types of operations may be performed on it to
modify its value:
if V is odd, subtract 1 from it;
if V is even, divide it by 2.
These operations are performed until the value of V becomes 0.
For example, if string S = "011100", its value V initially is 28. The value of V would change as follows:
V = 28, which is even: divide by 2 to obtain 14;
V = 14, which is even: divide by 2 to obtain 7;
V = 7, which is odd: subtract 1 to obtain 6;
V = 6, which is even: divide by 2 to obtain 3;
V = 3, which is odd: subtract 1 to obtain 2;
V = 2, which is even: divide by 2 to obtain 1;
V = 1, which is odd: subtract 1 to obtain 0..
Seven operations were required to reduce the value of V to 0.
Write a function:
class Solution { public int solution(string S); }
that, given a string S consisting of N characters containing a binary representation of the initial value V, returns the number of operations after
which its value will become 0.
Examples:
1. Given S = "011100", the function should return 7. String S represents the number 28, which becomes 0 after seven operations, as explained
above.
2. Given S = "111", the function should return 5. String S encodes the number V = 7. Its value will change over the following
*/
'''

using System;

public class Program
{
	public void Main()
	{
		Console.WriteLine("Hello World");

		//string S = "1111010101111";
		string S = "11111111111111111111111111111111111111";
		Console.WriteLine("Input:" + S);

		int result = solution(S);
		Console.WriteLine("Result:" + result);
	}

	public int solution(string S)
	{
		int counter = 0;

		//int V = Convert.ToInt32(S,2);
		long V = Convert.ToInt64(S,2);
		while(V > 0)
		{
			if(V%2 == 0)
			{
				V = V/2;
			}
			else
			{
				V = V -1;
			}
			counter++;
		}

	 	return counter;
	}
}
