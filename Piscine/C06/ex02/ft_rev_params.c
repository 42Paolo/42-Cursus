/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_rev_params.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pabrogi <pabrogi@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/21 14:26:35 by pabrogi           #+#    #+#             */
/*   Updated: 2025/10/21 14:27:37 by pabrogi          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	ft_print_str(char *str)
{
	while (*str)
	{
		write(1, str, 1);
		str++;
	}
}

int	main(int argc, char **argv)
{
	int	i;

	i = argc -1;
	if (argc > 1)
	{
		while (i > 0)
		{
			ft_print_str(argv[i]);
			write(1, "\n", 1);
			i--;
		}
	}
	return (0);
}
