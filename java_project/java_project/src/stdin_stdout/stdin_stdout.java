package stdin_stdout;

import java.util.Scanner;

class Test
{
	int n;
	float f;
	String s;
	
	void input()
	{
		Scanner scan1 = new Scanner(System.in);
		Scanner scan2 = new Scanner(System.in);
		System.out.printf("Please enter the int number= ");
		n = scan2.nextInt();
		System.out.printf("Please enter the float number= ");
		f = scan2.nextFloat();
		System.out.printf("Please enter the string= ");
		s = scan1.nextLine();
	}
	void display()
	{
		System.out.println(s);
		System.out.println(f);
		System.out.println(n);

	}
}


public class stdin_stdout
{
	public static void main(String[] args)
	{

		Test c = new Test();
		c.input();
		c.display();

	}
}