/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_rev_int_tab.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pabrogi <pabrogi@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/14 15:45:16 by pabrogi           #+#    #+#             */
/*   Updated: 2025/10/14 19:49:43 by pabrogi          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	ft_rev_int_tab(int *tab, int size)
{
	int	x;
	int	y;
	int	temp;

	x = 0;
	y = size - 1;
	while (x < y)
	{
		temp = tab[x];
		tab[x] = tab[y];
		tab[y] = temp;
		x++;
		y--;
	}
}
