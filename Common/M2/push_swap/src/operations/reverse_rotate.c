/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   reverse_rotate.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pabrogi <pabrogi@student.42firenze.it>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/25 10:20:16 by pabrogi           #+#    #+#             */
/*   Updated: 2026/02/03 16:14:39 by pabrogi          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../include/push_swap.h"

static void	reverse_rotate(t_stack **stack)
{
	t_stack	*last;
	t_stack	*before_last;

	if (!*stack || !(*stack)->next)
		return ;
	last = get_bottom(*stack);
	before_last = get_before_bottom(*stack);
	last->next = *stack;
	*stack = last;
	before_last->next = NULL;
}

void	rra(t_stack **stack_a, int print)
{
	reverse_rotate(stack_a);
	if (print)
		ft_putstr("rra\n");
}

void	rrb(t_stack **stack_b, int print)
{
	reverse_rotate(stack_b);
	if (print)
		ft_putstr("rrb\n");
}

void	rrr(t_stack **stack_a, t_stack **stack_b, int print)
{
	reverse_rotate(stack_a);
	reverse_rotate(stack_b);
	if (print)
		ft_putstr("rrr\n");
}
