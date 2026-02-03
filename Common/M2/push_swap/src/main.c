/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pabrogi <pabrogi@student.42firenze.it>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/10 14:23:18 by pabrogi           #+#    #+#             */
/*   Updated: 2026/01/31 22:15:44 by pabrogi          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/push_swap.h"

int	main(int argc, char **argv)
{
	t_stack	*a;
	t_stack	*b;

	if (argc < 2)
		return (0);
	a = NULL;
	b = NULL;
	parse_arguments(argc, argv, &a);
	if (is_sorted(a))
	{
		free_stack(&a);
		return (0);
	}
	assign_index(a, stack_size(a));
	if (stack_size(a) == 2)
		sa(&a, 1);
	else if (stack_size(a) == 3)
		sort_three(&a);
	else if (stack_size(a) <= 5)
		sort_small(&a, &b);
	else
		sort(&a, &b);
	free_stack(&a);
	free_stack(&b);
	return (0);
}
