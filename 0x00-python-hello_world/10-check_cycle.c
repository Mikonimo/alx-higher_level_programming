#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a a cycle in it
 * @list: the head pointer of the linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *first = list;
	listint_t *last = list->next;
c
	if (list == NULL || last == NULL                                         )
	{
		return (0);
	}
	while (first && last && last->next)
	{
		if (first == last)
		{
			return (1);
		}
		first = first->next;
		last = last->next->next;
	}
	return (0);
}
