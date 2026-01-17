/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_calloc.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pabrogi <pabrogi@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/24 10:41:18 by pabrogi           #+#    #+#             */
/*   Updated: 2025/11/26 12:07:04 by pabrogi          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_calloc(size_t count, size_t size)
{
	void	*tmp_v;

	tmp_v = malloc(count * size);
	if (!tmp_v)
		return (NULL);
	ft_memset(tmp_v, 0, count * size);
	return (tmp_v);
}
