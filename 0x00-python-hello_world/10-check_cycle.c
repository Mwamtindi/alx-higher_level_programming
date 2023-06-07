#include "lists.h"

/**
 * check_cycle - fxn that checks a cycle in singly linked list
 * @list: a pointer to the beginning of the node
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *curr, *chk;

	if (list == NULL || list->next == NULL)
		return (0);
	curr = list;
	chk = curr->next;

	while (curr != NULL && chk->next != NULL
		&& chk->next->next != NULL)
	{
		if (curr == chk)
			return (1);
		curr = curr->next;
		chk = chk->next->next;
	}
	return (0);
}
