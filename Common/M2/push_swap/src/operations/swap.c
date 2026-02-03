/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   swap.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pabrogi <pabrogi@student.42firenze.it>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/11 09:45:22 by pabrogi           #+#    #+#             */
/*   Updated: 2026/01/11 10:12:38 by pabrogi          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../include/push_swap.h"

static void	swap(t_stack **stack)
{
	t_stack	*first;
	t_stack	*second;
	int		tmp_val;
	int		tmp_idx;

	if (!*stack || !(*stack)->next)
		return ;
	first = *stack;
	second = first->next;
	tmp_val = first->value;
	tmp_idx = first->index;
	first->value = second->value;
	first->index = second->index;
	second->value = tmp_val;
	second->index = tmp_idx;
}

void	sa(t_stack **stack_a, int print)
{
	swap(stack_a);
	if (print)
		ft_putstr("sa\n");
}

void	sb(t_stack **stack_b, int print)
{
	swap(stack_b);
	if (print)
		ft_putstr("sb\n");
}

void	ss(t_stack **stack_a, t_stack **stack_b, int print)
{
	swap(stack_a);
	swap(stack_b);
	if (print)
		ft_putstr("ss\n");
}
