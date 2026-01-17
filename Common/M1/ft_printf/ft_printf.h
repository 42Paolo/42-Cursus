/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pabrogi <pabrogi@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/01 16:05:45 by pabrogi           #+#    #+#             */
/*   Updated: 2025/12/21 14:44:24 by pabrogi          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PRINTF_H
# define FT_PRINTF_H

# include <unistd.h>
# include <stdarg.h>

int		ft_printf(const char *format, ...);
int		ft_formats(va_list *args, char c);
int		ft_printchar(char c);
int		ft_printstr(char *s);
int		ft_printptr(void *ptr);
int		ft_printnbr(int n);
int		ft_printunsigned(unsigned int n);
int		ft_printhex(unsigned int n, char format);
int		ft_printpercent(void);

#endif