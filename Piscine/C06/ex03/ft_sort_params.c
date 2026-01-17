/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_sort_params.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pabrogi <pabrogi@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/21 14:28:05 by pabrogi           #+#    #+#             */
/*   Updated: 2025/10/21 17:01:03 by pabrogi          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	ft_print_str(char *str)
{
	while (*str)
		write(1, str++, 1);
	write(1, "\n", 1);
}

int	ft_strcmp(char *s1, char *s2)
{
	while (*s1 == *s2 && *s1)
	{
		s1++;
		s2++;
	}
	return ((unsigned char)*s1 - (unsigned char)*s2);
}

int	arr_sorted(char **argv, int size)
{
	int	i;

	i = 1;
	while (i < size - 1)
	{
		if (ft_strcmp(argv[i], argv[i + 1]) > 0)
			return (1);
		i++;
	}
	return (0);
}

int	main(int argc, char **argv)
{
	int		x;
	char	*temp_str;

	while (arr_sorted(argv, argc))
	{
		x = 1;
		while (x < argc - 1)
		{
			if (ft_strcmp(argv[x], argv[x + 1]) > 0)
			{
				temp_str = argv[x];
				argv[x] = argv[x + 1];
				argv[x + 1] = temp_str;
			}
			x++;
		}
	}
	x = 1;
	while (x < argc)
		ft_print_str(argv[x++]);
}
