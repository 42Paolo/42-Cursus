/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strupcase.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pabrogi <pabrogi@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/15 10:55:20 by pabrogi           #+#    #+#             */
/*   Updated: 2025/10/15 13:17:27 by pabrogi          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

char	*ft_strupcase(char *str)
{
	char	*start_str;

	start_str = str;
	while (*str)
	{
		if (!(*str >= 97 && *str <= 122))
			str++;
		else
		{
			*str -= 32;
			str++;
		}
	}
	return (start_str);
}
