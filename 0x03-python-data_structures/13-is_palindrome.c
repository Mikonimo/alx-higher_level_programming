#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: the head pointer of the list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	int i, size = 0;
	int arr[10000];

	if (!*head || !(*head)->next)
		return (1);

	while (fast && fast->next)
	{
		arr[size++] = slow->n;
		slow = slow->next;
		fast = fast->next->next;
	}
	if (fast)
		slow = slow->next;

	for (i = size - 1; i >= 0; i--)
	{
		if (arr[i] != slow->n)
			return (0);
		slow = slow->next;
	}

	return (1);
}
