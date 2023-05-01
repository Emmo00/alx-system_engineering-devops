#include <stdio.h>
#include <unistd.h>
/**
 * infinit_while - infinit loop
 * Return: 0
 */
int infinit_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - entry point
 * Return: 0 (success)
 */
int main(void)
{
	pid_t child_pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		child_pid = fork();
		if (child_pid == 0)
		{
			printf("Zombie process created, PID: %u\n", getpid());
			break;
		}
	}
	if (child_pid != 0)
		infinit_while();
	return (0);
}
