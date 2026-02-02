/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parse.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pabrogi <pabrogi@student.42firenze.it>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/02 14:32:16 by pabrogi           #+#    #+#             */
/*   Updated: 2026/02/02 14:32:17 by pabrogi          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../include/push_swap.h"

int	is_number(char *str)
{
	int	i;

	i = 0;
	if (str[i] == '-' || str[i] == '+')
		i++;
	if (!str[i])
		return (0);
	while (str[i])
	{
		if (str[i] < '0' || str[i] > '9')
			return (0);
		i++;
	}
	return (1);
}

int	has_duplicates(t_stack *stack)
{
	t_stack	*tmp;

	while (stack)
	{
		tmp = stack->next;
		while (tmp)
		{
			if (stack->value == tmp->value)
				return (1);
			tmp = tmp->next;
		}
		stack = stack->next;
	}
	return (0);
}

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

static void	process_number(char *str, t_stack **stack, char **numbers)
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

static void	parse_string(char *str, t_stack **stack)
{
	char	**numbers;
	int		i;

	numbers = ft_split(str, ' ');
	if (!numbers)
		error_exit();
	i = 0;
	while (numbers[i])
	{
		process_number(numbers[i], stack, numbers);
		i++;
	}
	free_split(numbers);
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
