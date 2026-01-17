/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_ultimate_range.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pabrogi <pabrogi@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/21 17:48:03 by pabrogi           #+#    #+#             */
/*   Updated: 2025/10/22 10:16:17 by pabrogi          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <stdlib.h>

int	ft_ultimate_range(int **range, int min, int max)
{
	int	i;
	int	x;

	if (max > min)
	{
		i = 0;
		x = min;
		*range = (int *)malloc(sizeof(int) * (max - min - 1));
		if (!range)
		{
			*range = NULL;
			return (-1);
		}
		while (x < max)
		{
			(*range)[i] = x;
			i++;
			x++;
		}
		return (max - min);
	}
	*range = NULL;
	return (0);
}
