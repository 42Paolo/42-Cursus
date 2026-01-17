/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pabrogi <pabrogi@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/15 19:21:10 by pabrogi           #+#    #+#             */
/*   Updated: 2025/10/16 14:50:31 by pabrogi          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_strlen(char *str)
{
	int	i;

	i = 0;
	while (str[i])
		i++;
	return (i);
}

unsigned int	ft_strlcat(char *dest, char *src, unsigned int size)
{
	unsigned int	dest_len;
	unsigned int	tot_len;
	unsigned int	space;

	dest_len = ft_strlen(dest);
	tot_len = dest_len + ft_strlen(src);
	if (size <= dest_len)
		return (size + ft_strlen(src));
	space = size - dest_len - 1;
	while (*dest)
		dest++;
	while (*src && space > 0)
	{
		*dest = *src;
		dest++;
		src++;
		space--;
	}
	*dest = '\0';
	return (tot_len);
}
