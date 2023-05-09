#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts node to a linked lsit
 * @head: head of the linked list
 * @number: number to insert
 *
 * Return: pointer to the new node, or NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *node = NULL, *prv_node = NULL;

	if (head == NULL)
		return (NULL);
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;
	for (node = *head; node && number >= node->n; node = node->next)
		prv_node = node;
	if (prv_node == NULL)
	{
		*head = new_node;
		new_node->next = node;
		return (new_node);
	}
	prv_node->next = new_node;
	new_node->next = node;
	return (new_node);
}
