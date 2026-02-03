/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pabrogi <pabrogi@student.42firenze.it>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/20 11:44:18 by pabrogi           #+#    #+#             */
/*   Updated: 2026/01/31 18:22:55 by pabrogi          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../include/push_swap.h"

static void	push_all_but_three(t_stack **stack_a, t_stack **stack_b)
{
	int	sz;
	int	pushed;
	int	i;

	sz = stack_size(*stack_a);
	pushed = 0;
	i = 0;
	while (sz > 6 && i < sz && pushed < sz / 2)
	{
		if ((*stack_a)->index <= sz / 2)
		{
			pb(stack_a, stack_b, 1);
			pushed++;
		}
		else
			ra(stack_a, 1);
		i++;
	}
	while (sz - pushed > 3)
	{
		pb(stack_a, stack_b, 1);
		pushed++;
	}
}

static void	shift_stack(t_stack **stack_a)
{
	int	pos;
	int	sz;

	sz = stack_size(*stack_a);
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
