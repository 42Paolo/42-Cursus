/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   utils_1.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pabrogi <pabrogi@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/01 16:06:03 by pabrogi           #+#    #+#             */
/*   Updated: 2025/12/21 19:14:17 by pabrogi          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_printunsigned(unsigned int n)
{
	int	count;

	count = 0;
	if (n >= 10)
		count += ft_printunsigned(n / 10);
	count += ft_printchar(n % 10 + '0');
	return (count);
}

int	ft_printhex(unsigned int n, char format)
{
	int		count;
	char	*lower;
	char	*upper;
	char	*base;

	count = 0;
	lower = "0123456789abcdef";
	upper = "0123456789ABCDEF";
	if (format == 'x')
		base = lower;
	else
		base = upper;
	if (n >= 16)
		count += ft_printhex(n / 16, format);
	count += ft_printchar(base[n % 16]);
	return (count);
}

int	ft_printpercent(void)
{
	return (ft_printchar('%'));
}

int	ft_putptr_hex(unsigned long n)
{
	int		count;
	char	*base;

	count = 0;
	base = "0123456789abcdef";
	if (n >= 16)
		count += ft_putptr_hex(n / 16);
	count += ft_printchar(base[n % 16]);
	return (count);
}

int	ft_printptr(void *ptr)
{
	int	count;

	count = 0;
	if (!ptr)
		return (ft_printstr("(nil)"));
	count += ft_printstr("0x");
	count += ft_putptr_hex((unsigned long)ptr);
	return (count);
}
