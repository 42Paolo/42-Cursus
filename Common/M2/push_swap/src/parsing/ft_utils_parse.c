/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_utils_parse.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pabrogi <pabrogi@student.42firenze.it>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/02 14:56:32 by pabrogi           #+#    #+#             */
/*   Updated: 2026/02/02 14:57:46 by pabrogi          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../include/push_swap.h"

void	add_to_stack(t_stack **stack, int value)
{
	t_stack	*new;

	new = stack_new(value);
	if (!new)
	{
		free_stack(stack);
		error_exit();
	}
	stack_add_bottom(stack, new);
}

void	process_number(char *str, t_stack **stack, char **numbers)
{
	long	num;

	if (!is_number(str))
	{
		free_split(numbers);
		free_stack(stack);
		error_exit();
	}
	num = ft_atol(str);
	if (num > INT_MAX || num < INT_MIN)
	{
		free_split(numbers);
		free_stack(stack);
		error_exit();
	}
	add_to_stack(stack, (int)num);
}
