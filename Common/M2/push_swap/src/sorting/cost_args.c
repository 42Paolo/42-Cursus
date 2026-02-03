/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   cost_args.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pabrogi <pabrogi@student.42firenze.it>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/23 13:11:45 by pabrogi           #+#    #+#             */
/*   Updated: 2026/01/30 23:28:17 by pabrogi          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../include/push_swap.h"

void	get_cost(t_stack **stack_a, t_stack **stack_b)
{
	t_stack	*tmp_a;
	t_stack	*curr_b;
	int		sz_a;
	int		sz_b;

	tmp_a = *stack_a;
	curr_b = *stack_b;
	sz_a = stack_size(tmp_a);
	sz_b = stack_size(curr_b);
	while (curr_b)
	{
		curr_b->cost_b = curr_b->pos;
		if (curr_b->pos > sz_b / 2)
			curr_b->cost_b = (sz_b - curr_b->pos) * -1;
		curr_b->cost_a = curr_b->target_pos;
		if (curr_b->target_pos > sz_a / 2)
			curr_b->cost_a = (sz_a - curr_b->target_pos) * -1;
		curr_b = curr_b->next;
	}
}

static void	do_move(t_stack **stack_a, t_stack **stack_b, int ca, int cb)
{
	while (ca > 0 && cb > 0)
	{
		rr(stack_a, stack_b, 1);
		ca--;
		cb--;
	}
	while (ca < 0 && cb < 0)
	{
		rrr(stack_a, stack_b, 1);
		ca++;
		cb++;
	}
	while (ca > 0 && ca--)
		ra(stack_a, 1);
	while (ca < 0 && ca++)
		rra(stack_a, 1);
	while (cb > 0 && cb--)
		rb(stack_b, 1);
	while (cb < 0 && cb++)
		rrb(stack_b, 1);
	pa(stack_a, stack_b, 1);
}

void	do_cheapest_move(t_stack **stack_a, t_stack **stack_b)
{
	t_stack	*tmp;
	int		cheapest;
	int		ca;
	int		cb;

	tmp = *stack_b;
	cheapest = INT_MAX;
	while (tmp)
	{
		if (ft_abs(tmp->cost_a) + ft_abs(tmp->cost_b) < cheapest)
		{
			cheapest = ft_abs(tmp->cost_a) + ft_abs(tmp->cost_b);
			ca = tmp->cost_a;
			cb = tmp->cost_b;
		}
		tmp = tmp->next;
	}
	do_move(stack_a, stack_b, ca, cb);
}
