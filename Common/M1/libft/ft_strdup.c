/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pabrogi <pabrogi@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/24 10:41:18 by pabrogi           #+#    #+#             */
/*   Updated: 2025/11/26 12:02:16 by pabrogi          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strdup(const char *s1)
{
	char	*ptr_s1_cpy;
	char	*tmp;

	ptr_s1_cpy = (char *)malloc(ft_strlen(s1) + 1);
	if (!ptr_s1_cpy)
		return (NULL);
	tmp = ptr_s1_cpy;
	while (*s1)
	{
		*tmp = *s1;
		tmp++;
		s1++;
	}
	*tmp = '\0';
	return (ptr_s1_cpy);
}
