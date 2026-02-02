/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   cost_args.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pabrogi <pabrogi@student.42firenze.it>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/02 14:32:16 by pabrogi           #+#    #+#             */
/*   Updated: 2026/02/02 17:32:45 by pabrogi          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../include/push_swap.h"

void	get_cost(t_stack **stack_a, t_stack **stack_b)
{
	t_stack	*current_a;
	t_stack	*current_b;
	int		size_a;
	int		size_b;

	current_a = *stack_a;
	current_b = *stack_b;
	size_a = stack_size(current_a);
	size_b = stack_size(current_b);
	while (current_b)
	{
		current_b->cost_b = current_b->pos;
		if (current_b->pos > size_b / 2)
			current_b->cost_b = (size_b - current_b->pos) * -1;
		current_b->cost_a = current_b->target_pos;
		if (current_b->target_pos > size_a / 2)
			current_b->cost_a = (size_a - current_b->target_pos) * -1;
		current_b = current_b->next;
	}
}


static void	do_move(t_stack **stack_a, t_stack **stack_b,
		int cost_a, int cost_b)
{
	while (cost_a > 0 && cost_b > 0)
	{
		rr(stack_a, stack_b, 1);
		cost_a--;
		cost_b--;
	}
	while (cost_a < 0 && cost_b < 0)
	{
		rrr(stack_a, stack_b, 1);
		cost_a++;
		cost_b++;
	}
	while (cost_a > 0 && cost_a--)
		ra(stack_a, 1);
	while (cost_a < 0 && cost_a++)
		rra(stack_a, 1);
	while (cost_b > 0 && cost_b--)
		rb(stack_b, 1);
	while (cost_b < 0 && cost_b++)
		rrb(stack_b, 1);
	pa(stack_a, stack_b, 1);
}

void	do_cheapest_move(t_stack **stack_a, t_stack **stack_b)
{
	t_stack	*current;
	int		cheapest;
	int		cost_a;
	int		cost_b;

	current = *stack_b;
	cheapest = INT_MAX;
	while (current)
	{
		if (ft_abs(current->cost_a) + ft_abs(current->cost_b) < cheapest)
		{
			cheapest = ft_abs(current->cost_a) + ft_abs(current->cost_b);
			cost_a = current->cost_a;
			cost_b = current->cost_b;
		}
		current = current->next;
	}
	do_move(stack_a, stack_b, cost_a, cost_b);
}
