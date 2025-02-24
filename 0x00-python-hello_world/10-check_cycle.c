#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a a cycle in it
 * @list: the head pointer of the linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = slow->next;

	if (list == NULL || fast == NULL)
		return (0);

	while (fast && slow && fast->next)
	{
		if (slow == fast)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
