/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memmove.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pabrogi <pabrogi@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/24 10:41:18 by pabrogi           #+#    #+#             */
/*   Updated: 2025/11/24 14:13:04 by pabrogi          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	copy_forward(unsigned char *d, const unsigned char *s, size_t n)
{
	while (n--)
	{
		*d = *s;
		d++;
		s++;
	}
}

void	*ft_memmove(void *dest, const void *src, size_t n)
{
	unsigned char	*ptr_d;
	unsigned char	*ptr_s;

	if (!dest && !src)
		return (NULL);
	ptr_d = (unsigned char *)dest;
	ptr_s = (unsigned char *)src;
	if (ptr_d > ptr_s)
	{
		ptr_d = ptr_d + n;
		ptr_s = ptr_s + n;
		while (n--)
		{
			ptr_d--;
			ptr_s--;
			*ptr_d = *ptr_s;
		}
	}
	else
		copy_forward(ptr_d, ptr_s, n);
	return (dest);
}
