#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: pointer the head of the linked list.
 * @number: The number to insert.
 * Return: ins_num
 **/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *ins_num;

	ins_num = malloc(sizeof(listint_t));
	if (ins_num == NULL)
		return (NULL);
	ins_num->n = number;

	if (node == NULL || node->n >= number)
	{
		ins_num->next = node;
		*head = ins_num;
		return (ins_num);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	ins_num->next = node->next;
	node->next = ins_num;

	return (ins_num);
}
