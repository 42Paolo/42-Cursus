/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   index_argument.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pabrogi <pabrogi@student.42firenze.it>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/12 10:18:29 by pabrogi           #+#    #+#             */
/*   Updated: 2026/01/24 16:42:11 by pabrogi          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../include/push_swap.h"

static t_stack	*get_next_min(t_stack *stack)
{
	t_stack	*min;
	int		has_min;

	min = NULL;
	has_min = 0;
	while (stack)
	{
		if (stack->index == 0 && (!has_min || stack->value < min->value))
		{
			min = stack;
			has_min = 1;
		}
		stack = stack->next;
	}
	return (min);
}

void	assign_index(t_stack *stack_a, int stack_size)
{
	t_stack	*ptr;
	int		idx;

	idx = 1;
	while (idx <= stack_size)
	{
		ptr = get_next_min(stack_a);
		if (ptr)
			ptr->index = idx;
		idx++;
	}
}

int	get_min_index_pos(t_stack **stack)
{
	t_stack	*tmp;
	int		min_idx;
	int		min_pos;
	int		pos;

	tmp = *stack;
	min_idx = tmp->index;
	min_pos = 0;
	pos = 0;
	while (tmp)
	{
		if (tmp->index < min_idx)
		{
			min_idx = tmp->index;
			min_pos = pos;
		}
		pos++;
		tmp = tmp->next;
	}
	return (min_pos);
}

int	get_highest_index(t_stack *stack)
{
	int	max;

	max = stack->index;
	while (stack)
	{
		if (stack->index > max)
			max = stack->index;
		stack = stack->next;
	}
	return (max);
}
