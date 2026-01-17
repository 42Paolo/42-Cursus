/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strtrim.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pabrogi <pabrogi@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/24 10:41:18 by pabrogi           #+#    #+#             */
/*   Updated: 2025/11/24 19:13:39 by pabrogi          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static int	is_present(char c, const char *set)
{
	while (*set)
	{
		if (*set == c)
			return (1);
		set++;
	}
	return (0);
}

char	*ft_strtrim(char const *s1, char const *set)
{
	const char	*start;
	const char	*end;
	char		*res;
	char		*tmp;

	if (!s1 || !set)
		return (NULL);
	start = s1;
	while (*start && is_present(*start, set))
		start++;
	end = s1 + ft_strlen(s1);
	while (end > start && is_present(*(end - 1), set))
		end--;
	res = (char *)malloc((end - start) + 1);
	if (!res)
		return (NULL);
	tmp = res;
	while (start < end)
		*tmp++ = *start++;
	*tmp = '\0';
	return (res);
}
