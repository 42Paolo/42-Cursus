/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strstr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pabrogi <pabrogi@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/15 19:02:27 by pabrogi           #+#    #+#             */
/*   Updated: 2025/10/15 19:20:38 by pabrogi          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

char	*ft_strstr(char *str, char *to_find)
{
	char	*temp_p;
	char	*temp_f;

	if (*to_find == '\0')
		return (str);
	temp_f = to_find;
	while (*str)
	{
		if (*str == *to_find)
		{
			temp_p = str;
			while (*str && *to_find && *str == *to_find)
			{
				str++;
				to_find++;
			}
			if (*to_find == '\0')
				return (temp_p);
			to_find = temp_f;
			str = temp_p + 1;
		}
		else
			str++;
	}
	return (NULL);
}
