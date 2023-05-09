#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a linked list have cycle or not
 * @list: pointer to the linked list
 *
 * Return: 0 if have no cycle, 1 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *node;

	if (list == NULL || list->next == NULL)
		return (0);
	for (node = list->next; node; node = node->next)
	{
		if (node->next && node <= node->next)
			return (1);
	}
	return (0);
}
