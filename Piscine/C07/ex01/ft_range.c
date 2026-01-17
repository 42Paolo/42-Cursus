/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_range.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pabrogi <pabrogi@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/21 17:33:31 by pabrogi           #+#    #+#             */
/*   Updated: 2025/10/21 17:50:34 by pabrogi          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <stdlib.h>

int	*ft_range(int min, int max)
{
	int	x;
	int	i;
	int	*nums;

	if (max > min)
	{
		x = 0;
		nums = (int *)malloc(sizeof(int) * ((max - min)));
		i = min;
		while (i < max)
		{
			nums[x] = i;
			x++;
			i++;
		}
		return (nums);
	}
	return (NULL);
}
