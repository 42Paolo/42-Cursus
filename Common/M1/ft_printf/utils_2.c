/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   utils_2.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pabrogi <pabrogi@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/04 14:08:18 by pabrogi           #+#    #+#             */
/*   Updated: 2025/12/21 15:04:28 by pabrogi          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_printchar(char c)
{
	write(1, &c, 1);
	return (1);
}

int	ft_printstr(char *s)
{
	int	i;

	i = 0;
	if (!s)
		return (ft_printstr("(null)"));
	while (s[i])
	{
		ft_printchar(s[i]);
		i++;
	}
	return (i);
}

int	ft_printnbr(int n)
{
	long	num;
	int		count;

	num = n;
	count = 0;
	if (num < 0)
	{
		count += ft_printchar('-');
		num = -num;
	}
	if (num >= 10)
		count += ft_printnbr(num / 10);
	count += ft_printchar(num % 10 + '0');
	return (count);
}

int	ft_formats(va_list *args, char c)
{
	if (c == 'c')
		return (ft_printchar(va_arg(*args, int)));
	if (c == 's')
		return (ft_printstr(va_arg(*args, char *)));
	if (c == 'p')
		return (ft_printptr((void *)va_arg(*args, unsigned long)));
	if (c == 'd' || c == 'i')
		return (ft_printnbr(va_arg(*args, int)));
	if (c == 'u')
		return (ft_printunsigned(va_arg(*args, unsigned int)));
	if (c == 'x' || c == 'X')
		return (ft_printhex(va_arg(*args, unsigned int), c));
	if (c == '%')
		return (ft_printpercent());
	return (0);
}
