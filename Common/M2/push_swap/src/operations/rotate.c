/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rotate.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pabrogi <pabrogi@student.42firenze.it>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/02 14:32:16 by pabrogi           #+#    #+#             */
/*   Updated: 2026/02/02 14:32:17 by pabrogi          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../include/push_swap.h"

static void	rotate(t_stack **stack)
{
	t_stack	*first;
	t_stack	*last;

	if (!*stack || !(*stack)->next)
		return ;
	first = *stack;
	last = get_bottom(*stack);
	*stack = first->next;
	first->next = NULL;
	last->next = first;
}

void	ra(t_stack **stack_a, int print)
{
	rotate(stack_a);
	if (print)
		ft_putstr("ra\n");
}

void	rb(t_stack **stack_b, int print)
{
	rotate(stack_b);
	if (print)
		ft_putstr("rb\n");
}

void	rr(t_stack **stack_a, t_stack **stack_b, int print)
{
	rotate(stack_a);
	rotate(stack_b);
	if (print)
		ft_putstr("rr\n");
}
