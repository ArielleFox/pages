#include <stdio.h>

int main(int argc, char * argv[])
{
	FILE *file = fopen("thursday.txt", "r");
	if (file != NULL)
	{
		char c;
		while (fread(&c, sizeof(char), 1, file))
		{
			printf("%c", c);
		}
		fclose(file);
	}
}
