/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_comb2.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pabrogi <pabrogi@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/14 10:47:33 by pabrogi           #+#    #+#             */
/*   Updated: 2025/10/14 14:44:41 by pabrogi          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	ft_print_num(int n)
{
	char	c;

	if (n >= 10)
		ft_print_num(n / 10);
	c = (n % 10) + '0';
	write(1, &c, 1);
}

void	ft_print_comb2_num(int d1, int u1, int d2, int u2)
{
	if ((d1 * 10 + u1) < (d2 * 10 + u2))
	{
		ft_print_num(d1);
		ft_print_num(u1);
		write(1, " ", 1);
		ft_print_num(d2);
		ft_print_num(u2);
		if (!(d1 == 9 && u1 == 8 && d2 == 9 && u2 == 9))
			write(1, ", ", 2);
	}
}

void	ft_print_second(int d1, int u1)
{
	int	d2;
	int	u2;

	d2 = 0;
	while (d2 <= 9)
	{
		u2 = 0;
		while (u2 <= 9)
		{
			ft_print_comb2_num(d1, u1, d2, u2);
			u2++;
		}
		d2++;
	}
}

void	ft_print_comb2(void)
{
	int	d1;
	int	u1;

	d1 = 0;
	while (d1 <= 9)
	{
		u1 = 0;
		while (u1 <= 9)
		{
			ft_print_second(d1, u1);
			u1++;
		}
		d1++;
	}
}
