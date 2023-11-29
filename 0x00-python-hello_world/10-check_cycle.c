#include "lists.h"

/**
 * check_cycle - Program that checks if a singly linked list has cycle in it
 * @list: pointer to the list
 *
 * Return: 0 if there is no cycle,1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *ck;
	listint_t *prev;

	ck = list;
	prev = list;
	while (list && ck && ck->next)
	{
		list = list->next;
		ck = ck->next->next;

		if (list == ck)
		{
			list = prev;
			prev =  ck;
			while (1)
			{
				ck = prev;
				while (ck->next != list && ck->next != prev)
				{
					ck = ck->next;
				}
				if (ck->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}
