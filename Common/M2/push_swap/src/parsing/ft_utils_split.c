/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_utils_split.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pabrogi <pabrogi@student.42firenze.it>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/02 14:51:06 by pabrogi           #+#    #+#             */
/*   Updated: 2026/02/02 14:52:29 by pabrogi          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../include/push_swap.h"

char const	*skip_delimiters(char const *s, char c)
{
	while (*s && *s == c)
		s++;
	return (s);
}

char const	*skip_word(char const *s, char c)
{
	while (*s && *s != c)
		s++;
	return (s);
}
