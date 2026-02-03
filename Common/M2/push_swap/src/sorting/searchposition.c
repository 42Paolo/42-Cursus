/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   searchposition.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pabrogi <pabrogi@student.42firenze.it>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/22 16:38:22 by pabrogi           #+#    #+#             */
/*   Updated: 2026/02/03 17:07:55 by pabrogi          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../include/push_swap.h"

void	get_position(t_stack **stack)
{
	t_stack	*tmp;
	int		pos;

	tmp = *stack;
	pos = 0;
	while (tmp)
	{
		tmp->pos = pos;
		pos++;
		tmp = tmp->next;
	}
}

static int	get_target(t_stack *stack_a, int idx_b, int tgt_idx, int tgt_pos)
{
	t_stack	*tmp;

	tmp = stack_a;
	while (tmp)
	{
		if (tmp->index > idx_b && tmp->index < tgt_idx)
		{
			tgt_idx = tmp->index;
			tgt_pos = tmp->pos;
		}
		tmp = tmp->next;
	}
	if (tgt_idx != INT_MAX)
		return (tgt_pos);
	tmp = stack_a;
	while (tmp)
	{
		if (tmp->index < tgt_idx)
		{
			tgt_idx = tmp->index;
			tgt_pos = tmp->pos;
		}
		tmp = tmp->next;
	}
	return (tgt_pos);
}

void	get_target_position(t_stack **stack_a, t_stack **stack_b)
{
	t_stack	*curr_b;
	int		tgt_pos;

	curr_b = *stack_b;
	get_position(stack_a);
	get_position(stack_b);
	tgt_pos = 0;
	while (curr_b)
	{
		tgt_pos = get_target(*stack_a, curr_b->index, INT_MAX, tgt_pos);
		curr_b->target_pos = tgt_pos;
		curr_b = curr_b->next;
	}
}
