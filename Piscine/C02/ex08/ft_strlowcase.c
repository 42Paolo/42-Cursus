/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlowcase.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pabrogi <pabrogi@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/15 11:38:23 by pabrogi           #+#    #+#             */
/*   Updated: 2025/10/15 13:50:15 by pabrogi          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

char	*ft_strlowcase(char *str)
{
	char	*start_str;

	start_str = str;
	while (*str)
	{
		if (!(*str >= 65 && *str <= 90))
			str++;
		else
		{
			*str += 32;
			str++;
		}
	}
	return (start_str);
}
