#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
/**
 * infinite_while - Run an infinite while loop
 *
 * Return: Always 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - make 5 zombies processes.
 *
 * Return: void
 */
int main(void)
{
	pid_t zombie;
	int q;

	for (q = 0; q < 5; q++)
	{
		zombie = fork();
		if (!zombie)
			return (0);
		printf("Zombie process created, PID: %d\n", zombie);
	}
	infinite_while();
	return (1);
}
