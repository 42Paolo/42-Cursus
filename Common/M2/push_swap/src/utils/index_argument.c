/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   index_argument.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pabrogi <pabrogi@student.42firenze.it>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/05 14:49:16 by pabrogi           #+#    #+#             */
/*   Updated: 2026/02/03 16:18:13 by pabrogi          ###   ########.fr       */
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
	t_stack	*current;
	int		index;

	index = 1;
	while (index <= stack_size)
	{
		current = get_next_min(stack_a);
		if (current)
			current->index = index;
		index++;
	}
}

int	get_min_index_pos(t_stack **stack)
{
	t_stack	*current;
	int		min_index;
	int		min_pos;
	int		pos;

	current = *stack;
	min_index = current->index;
	min_pos = 0;
	pos = 0;
	while (current)
	{
		if (current->index < min_index)
		{
			min_index = current->index;
			min_pos = pos;
		}
		pos++;
		current = current->next;
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
