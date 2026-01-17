/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_find_next_prime.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pabrogi <pabrogi@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/21 13:49:29 by pabrogi           #+#    #+#             */
/*   Updated: 2025/10/21 13:57:30 by pabrogi          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

int	ft_is_prime(int nb)
{
	int	n;

	n = 1;
	if (nb < 0 || nb == 0 || nb == 1)
		return (0);
	while (n <= nb)
	{
		if (nb % n == 0 && n != 1 && n != nb)
			return (0);
		n++;
	}
	return (1);
}

int	ft_find_next_prime(int nb)
{
	while ((ft_is_prime(nb) == 0))
		nb++;
	return (nb);
}
