/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pabrogi <pabrogi@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/21 17:22:01 by pabrogi           #+#    #+#             */
/*   Updated: 2025/10/21 17:32:34 by pabrogi          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <stdlib.h>

int	ft_strlen(char *str)
{
	int	i;

	i = 0;
	while (str[i])
		i++;
	return (i);
}

char	*ft_strdup(char *src)
{
	char	*str_copy;
	char	*tmp_p;
	int		len;
	int		i;

	i = 0;
	len = ft_strlen(src);
	str_copy = (char *)malloc(sizeof(char) * (len + 1));
	tmp_p = str_copy;
	while (i < len)
	{
		str_copy[i] = src[i];
		i++;
	}
	str_copy[i] = '\0';
	return (tmp_p);
}
