/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr_base.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pabrogi <pabrogi@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/16 18:29:07 by pabrogi           #+#    #+#             */
/*   Updated: 2025/11/06 17:12:18 by pabrogi          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

int	ft_strcmp(char *s1, char *s2)
{
	while (*s1 == *s2 && *s1)
	{
		s1++;
		s2++;
	}
	return ((unsigned char)*s1 - (unsigned char)*s2);
}

void	ft_putnbr(int nb)
{
	char	c;

	if (nb == -2147483648)
	{
		write(1, "-2147483648", 11);
		return ;
	}
	if (nb < 0)
	{
		write(1, "-", 1);
		nb = -nb;
	}
	if (nb >= 10)
		ft_putnbr(nb / 10);
	c = (nb % 10) + '0';
	write(1, &c, 1);
}

int	store_digits(unsigned int num, int div, int *resto)
{
	int	i;

	i = 0;
	while (num > 0)
	{
		resto[i] = num % div;
		num /= div;
		i++;
	}
	return (i);
}

void	convert_base(int nb, int div, char *base)
{
	int				resto[32];
	int				i;
	unsigned int	num;

	if (nb == 0)
	{
		write(1, &base[0], 1);
		return ;
	}
	if (nb < 0)
	{
		write(1, "-", 1);
		num = -((unsigned int)nb);
	}
	else
		num = nb;
	i = store_digits(num, div, resto);
	while (i > 0)
	{
		i--;
		write(1, &base[resto[i]], 1);
	}
}

void	ft_putnbr_base(int nbr, char *base)
{
	if (ft_strcmp(base, "0123456789") == 0)
		ft_putnbr(nbr);
	else if (ft_strcmp(base, "01") == 0)
		convert_base(nbr, 2, base);
	else if (ft_strcmp(base, "0123456789abcdef") == 0)
		convert_base(nbr, 16, base);
	else if (ft_strcmp(base, "poneyvif") == 0)
		convert_base(nbr, 8, base);
	else
		return ;
}
