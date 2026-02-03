/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parse_input.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pabrogi <pabrogi@student.42firenze.it>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/11 11:35:48 by pabrogi           #+#    #+#             */
/*   Updated: 2026/01/18 21:07:33 by pabrogi          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../include/push_swap.h"

static void	add_to_stack(t_stack **stack, int value)
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

static void	process_number(char *str, t_stack **stack, char **nums)
{
	long	num;

	if (!is_number(str))
	{
		free_split(nums);
		free_stack(stack);
		error_exit();
	}
	num = ft_atol(str);
	if (num > INT_MAX || num < INT_MIN)
	{
		free_split(nums);
		free_stack(stack);
		error_exit();
	}
	add_to_stack(stack, (int)num);
}

static void	parse_string(char *str, t_stack **stack)
{
	char	**nums;
	int		i;

	nums = ft_split(str, ' ');
	if (!nums)
		error_exit();
	i = 0;
	while (nums[i])
	{
		process_number(nums[i], stack, nums);
		i++;
	}
	free_split(nums);
}

static void	parse_multiple_args(int argc, char **argv, t_stack **stack_a)
{
	int		i;
	long	num;

	i = 1;
	while (i < argc)
	{
		if (!is_number(argv[i]))
		{
			free_stack(stack_a);
			error_exit();
		}
		num = ft_atol(argv[i]);
		if (num > INT_MAX || num < INT_MIN)
		{
			free_stack(stack_a);
			error_exit();
		}
		add_to_stack(stack_a, (int)num);
		i++;
	}
}

void	parse_arguments(int argc, char **argv, t_stack **stack_a)
{
	if (argc == 2)
		parse_string(argv[1], stack_a);
	else
		parse_multiple_args(argc, argv, stack_a);
	if (has_duplicates(*stack_a))
	{
		free_stack(stack_a);
		error_exit();
	}
}
