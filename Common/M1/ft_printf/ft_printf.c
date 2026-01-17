/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pabrogi <pabrogi@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/01 16:06:03 by pabrogi           #+#    #+#             */
/*   Updated: 2025/12/21 14:57:25 by pabrogi          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_printf(const char *format, ...)
{
	va_list	args;
	int		ret_count;
	int		i;

	va_start(args, format);
	i = 0;
	ret_count = 0;
	while (format[i])
	{
		if (format[i] == '%' && format[i + 1])
		{
			ret_count += ft_formats(&args, format[i + 1]);
			i += 2;
		}
		else
		{
			ret_count += ft_printchar(format[i]);
			i++;
		}
	}
	va_end(args);
	return (ret_count);
}
