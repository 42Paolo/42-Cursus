/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pabrogi <pabrogi@student.42firenze.it>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/30 10:55:32 by pabrogi           #+#    #+#             */
/*   Updated: 2026/02/03 16:10:08 by pabrogi          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../include/push_swap.h"

static void	push_all_but_three(t_stack **stack_a, t_stack **stack_b)
{
	int	size;
	int	pushed;
	int	i;

	size = stack_size(*stack_a);
	pushed = 0;
	i = 0;
	while (size > 6 && i < size && pushed < size / 2)
	{
		if ((*stack_a)->index <= size / 2)
		{
			pb(stack_a, stack_b, 1);
			pushed++;
		}
		else
			ra(stack_a, 1);
		i++;
	}
	while (size - pushed > 3)
	{
		pb(stack_a, stack_b, 1);
		pushed++;
	}
}

static void	shift_stack(t_stack **stack_a)
{
	int	min_pos;
	int	size;

	size = stack_size(*stack_a);
	min_pos = get_min_index_pos(stack_a);
	if (min_pos <= size / 2)
	{
		while (min_pos-- > 0)
			ra(stack_a, 1);
	}
	else
	{
		while (min_pos++ < size)
			rra(stack_a, 1);
	}
}

void	sort(t_stack **stack_a, t_stack **stack_b)
{
	push_all_but_three(stack_a, stack_b);
	sort_three(stack_a);
	while (*stack_b)
	{
		get_target_position(stack_a, stack_b);
		get_cost(stack_a, stack_b);
		do_cheapest_move(stack_a, stack_b);
	}
	if (!is_sorted(*stack_a))
		shift_stack(stack_a);
}
