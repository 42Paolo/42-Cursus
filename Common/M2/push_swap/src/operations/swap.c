/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   swap.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pabrogi <pabrogi@student.42firenze.it>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/25 10:20:15 by pabrogi           #+#    #+#             */
/*   Updated: 2026/02/03 16:14:14 by pabrogi          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../include/push_swap.h"

static void	swap(t_stack **stack)
{
	t_stack	*first;
	t_stack	*second;
	int		tmp_value;
	int		tmp_index;

	if (!*stack || !(*stack)->next)
		return ;
	first = *stack;
	second = first->next;
	tmp_value = first->value;
	tmp_index = first->index;
	first->value = second->value;
	first->index = second->index;
	second->value = tmp_value;
	second->index = tmp_index;
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
