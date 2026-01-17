/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_sort_int_tab.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pabrogi <pabrogi@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/14 18:25:32 by pabrogi           #+#    #+#             */
/*   Updated: 2025/10/15 09:44:44 by pabrogi          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	check_sort(int *tab, int size)
{
	int	i;

	i = 0;
	while (i < size - 1)
	{
		if (tab[i] > tab[i + 1])
			return (1);
		i++;
	}
	return (0);
}

void	ft_sort_arr(int *tab, int size)
{
	int	temp;

	while (size > 0)
	{
		if (tab[size] < tab[size - 1])
		{
			temp = tab[size - 1];
			tab[size - 1] = tab[size];
			tab[size] = temp;
		}
		size--;
	}
}

void	ft_sort_int_tab(int *tab, int size)
{
	while (check_sort(tab, size))
		ft_sort_arr(tab, size - 1);
}
