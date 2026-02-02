/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pabrogi <pabrogi@student.42firenze.it>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/02 14:32:16 by pabrogi           #+#    #+#             */
/*   Updated: 2026/02/02 14:32:17 by pabrogi          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/push_swap.h"

int	main(int argc, char **argv)
{
	t_stack	*stack_a;
	t_stack	*stack_b;

	if (argc < 2)
		return (0);
	stack_a = NULL;
	stack_b = NULL;
	parse_arguments(argc, argv, &stack_a);
	if (is_sorted(stack_a))
	{
		free_stack(&stack_a);
		return (0);
	}
	assign_index(stack_a, stack_size(stack_a));
	if (stack_size(stack_a) == 2)
		sa(&stack_a, 1);
	else if (stack_size(stack_a) == 3)
		sort_three(&stack_a);
	else if (stack_size(stack_a) <= 5)
		sort_small(&stack_a, &stack_b);
	else
		sort(&stack_a, &stack_b);
	free_stack(&stack_a);
	free_stack(&stack_b);
	return (0);
}
