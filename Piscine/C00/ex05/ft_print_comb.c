/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_comb.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pabrogi <pabrogi@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/14 09:07:32 by pabrogi           #+#    #+#             */
/*   Updated: 2025/10/14 14:44:40 by pabrogi          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	ft_print_num(int n)
{
	char	c;

	if (n == -2147483648)
	{
		write(1, "-2147483648", 11);
		return ;
	}
	if (n < 0)
	{
		write(1, "-", 1);
		n = -n;
	}
	if (n >= 10)
		ft_print_num(n / 10);
	c = (n % 10) + '0';
	write(1, &c, 1);
}

void	ft_print_num_comb(int u, int d, int c)
{
	ft_print_num(c);
	ft_print_num(d);
	ft_print_num(u);
	if (!(c * 100 + d * 10 + u == 789))
		write(1, ", ", 2);
}

void	ft_print_comb(void)
{
	int	u;
	int	d;
	int	c;

	u = 0;
	d = 0;
	c = 0;
	while (c <= 9)
	{
		while (d <= 9)
		{
			while (u <= 9)
			{
				if ((c < d) && (d < u))
					ft_print_num_comb(u, d, c);
				u++;
			}
			u = 0;
			d++;
		}
		d = 0;
		c++;
	}
}
