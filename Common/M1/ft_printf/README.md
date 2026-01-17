_This project has been created as part of the 42 curriculum by pabrogi._

# Description:

ft_printf is a project where my goal is to recreate the same behavior of the stdio.h function printf().
This function allows you to print text to the terminal, but not only that. One of its main features is the ability to print different types of variables as text:

– %c → single character
– %s → string of characters
– %p → void* pointer in hexadecimal format
– %d → decimal number
– %i → integer
– %u → unsigned decimal number
– %x → number in lowercase hexadecimal format
– %X → number in uppercase hexadecimal format

You can print each variable by writing % followed by the type you want to print inside the format string.
At this point, a perfectly valid question may come to mind: how does the function know which variable I want to print?
Simple, every variable you want to print must be passed right after the format string, in the same order as they appear in the text.

⸻

# Instructions:

Here is a brief explanation on how to use it:

1 - Clone the ft_printf repository inside your project folder:
 	
	"git clone (repository link)"

2 - Enter the folder you just cloned and compile it using:
 	
	"make re"

3 - Include the ft_printf.h header in your project:
	
	"#include "./ft_printf.h" "

4 - Link the compiled library when compiling your own project.

⸻

# Resources:

Most of the resources for this project were taken from GitHub and ChatGPT.
For the conversion methods I mainly asked ChatGPT, while for the structure and the general code organization I looked at previously completed projects uploaded on GitHub.
This helped me avoid writing unnecessary lines of code and kept the project more concise.

⸻

Example of usage:

Assuming that all the setup steps are done. To use the function, just call it in your code: the first parameter is the string you want to print (with the variable formats inside), and the following parameters are the actual variables you want to print.

Example:

int main()
{
	int   age;
	char *name;

	name = "Paolo";
	age = 21;

	ft_printf("Hello, my name is %s and I am %d years old.", name, age);
}
