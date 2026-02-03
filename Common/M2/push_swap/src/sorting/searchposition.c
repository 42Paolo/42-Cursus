/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   searchposition.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pabrogi <pabrogi@student.42firenze.it>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/31 20:52:55 by pabrogi           #+#    #+#             */
/*   Updated: 2026/02/03 16:11:29 by pabrogi          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../include/push_swap.h"

void	get_position(t_stack **stack)
{
	t_stack	*current;
	int		pos;

	current = *stack;
	pos = 0;
	while (current)
	{
		current->pos = pos;
		pos++;
		current = current->next;
	}
}

static int	get_target(t_stack *stack_a, int index_b,
		int target_index, int target_pos)
{
	t_stack	*current;

	current = stack_a;
	while (current)
	{
		if (current->index > index_b && current->index < target_index)
		{
			target_index = current->index;
			target_pos = current->pos;
		}
		current = current->next;
	}
	if (target_index != INT_MAX)
		return (target_pos);
	current = stack_a;
	while (current)
	{
		if (current->index < target_index)
		{
			target_index = current->index;
			target_pos = current->pos;
		}
		current = current->next;
	}
	return (target_pos);
}

void	get_target_position(t_stack **stack_a, t_stack **stack_b)
{
	t_stack	*current_b;
	int		target_pos;

	current_b = *stack_b;
	get_position(stack_a);
	get_position(stack_b);
	target_pos = 0;
	while (current_b)
	{
		target_pos = get_target(*stack_a, current_b->index,
				INT_MAX, target_pos);
		current_b->target_pos = target_pos;
		current_b = current_b->next;
	}
}
