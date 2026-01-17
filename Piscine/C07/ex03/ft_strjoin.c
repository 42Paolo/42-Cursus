/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pabrogi <pabrogi@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/22 10:36:04 by pabrogi           #+#    #+#             */
/*   Updated: 2025/10/22 10:59:12 by pabrogi          ###   ########.fr       */
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

char	*ft_strcpy(char *dst, char *src)
{
	while (*src)
		*dst++ = *src++;
	return (dst);
}

int	check_len(char **str, char *sep, int size)
{
	int	i;
	int	tot_len;

	tot_len = 0;
	i = 0;
	while (i < size)
	{
		tot_len += ft_strlen(str[i]);
		if (i < size -1)
			tot_len += ft_strlen(sep);
		i++;
	}
	return (tot_len);
}

char	*fill_str(char *str, char **strs, char *sep, int size)
{
	int	i;

	i = 0;
	while (i < size)
	{
		str = ft_strcpy(str, strs[i]);
		if (i < size - 1)
			str = ft_strcpy(str, sep);
		i++;
	}
	return (str);
}

char	*ft_strjoin(int size, char **strs, char *sep)
{
	int		tot_len;
	char	*str;
	char	*temp_p;

	if (size == 0)
	{
		str = malloc(1);
		if (!str)
			return (NULL);
		str[0] = '\0';
		return (str);
	}
	tot_len = check_len(strs, sep, size) + 1;
	str = (char *)malloc(sizeof(char) * tot_len);
	if (!str)
		return (NULL);
	temp_p = str;
	str = fill_str(str, strs, sep, size);
	*str = '\0';
	return (temp_p);
}
