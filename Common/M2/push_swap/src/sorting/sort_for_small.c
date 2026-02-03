/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_for_small.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pabrogi <pabrogi@student.42firenze.it>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/13 09:22:14 by pabrogi           #+#    #+#             */
/*   Updated: 2026/01/25 14:18:39 by pabrogi          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../include/push_swap.h"

static int	find_highest_index(t_stack *stack)
{
	int	highest;

	highest = stack->index;
	while (stack)
	{
		if (stack->index > highest)
			highest = stack->index;
		stack = stack->next;
	}
	return (highest);
}

void	sort_three(t_stack **stack_a)
{
	int	highest;

	if (is_sorted(*stack_a))
		return ;
	highest = find_highest_index(*stack_a);
	if ((*stack_a)->index == highest)
		ra(stack_a, 1);
	else if ((*stack_a)->next->index == highest)
		rra(stack_a, 1);
	if ((*stack_a)->index > (*stack_a)->next->index)
		sa(stack_a, 1);
}

void	sort_small(t_stack **stack_a, t_stack **stack_b)
{
	int	sz;
	int	pos;

	sz = stack_size(*stack_a);
	while (sz > 3)
	{
		pos = get_min_index_pos(stack_a);
		if (pos <= sz / 2)
		{
			while (pos-- > 0)
				ra(stack_a, 1);
		}
		else
		{
			while (pos++ < sz)
				rra(stack_a, 1);
		}
		pb(stack_a, stack_b, 1);
		sz--;
	}
	sort_three(stack_a);
	while (*stack_b)
		pa(stack_a, stack_b, 1);
}
