#include "lists.h"

/**
 * insert_node - function that inserts a node into a singly linked list
 * @head: linked list head
 * @number: value for the new node that will be inserted
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));
	listint_t *current_node = *head;

	if (new_node)
	{
		new_node->n = number;
		new_node->next = NULL;

		if (*head == NULL || (*head)->n >= new_node->n)
		{
			new_node->next = *head;
			*head = new_node;
		}
		else
		{
			while (current_node->next && current_node->next->n < new_node->n)
			{
				current_node = current_node->next;
			}
			new_node->next = current_node->next;
			current_node->next = new_node;
		}
		return (new_node);
	}
	return (NULL);
}
