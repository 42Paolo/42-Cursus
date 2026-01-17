/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strnstr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pabrogi <pabrogi@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/24 10:41:18 by pabrogi           #+#    #+#             */
/*   Updated: 2025/11/24 16:41:15 by pabrogi          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strnstr(const char *haystack, const char *needle, size_t len)
{
	const char	*ptr_haystack;
	const char	*ptr_needle;
	size_t		i;

	if (*needle == '\0')
		return ((char *)haystack);
	while (*haystack && len > 0)
	{
		ptr_haystack = haystack;
		ptr_needle = needle;
		i = len;
		while (*ptr_haystack == *ptr_needle && *ptr_needle && i > 0)
		{
			ptr_haystack++;
			ptr_needle++;
			i--;
		}
		if (*ptr_needle == '\0')
			return ((char *)haystack);
		haystack++;
		len--;
	}
	return (NULL);
}
