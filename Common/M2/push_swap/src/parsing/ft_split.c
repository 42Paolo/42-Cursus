/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pabrogi <pabrogi@student.42firenze.it>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/02 14:32:16 by pabrogi           #+#    #+#             */
/*   Updated: 2026/02/02 16:54:30 by pabrogi          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../include/push_swap.h"

static char const	*skip_delimiters(char const *s, char c)
{
	while (*s && *s == c)
		s++;
	return (s);
}

static char const	*skip_word(char const *s, char c)
{
	while (*s && *s != c)
		s++;
	return (s);
}

static char	**fill_result(char const *s, char c, char **result)
{
	int	i;

	i = 0;
	while (*s)
	{
		s = skip_delimiters(s, c);
		if (*s)
		{
			result[i] = get_word(s, c);
			if (!result[i])
				return (free_split(result), NULL);
			i++;
			s = skip_word(s, c);
		}
	}
	result[i] = NULL;
	return (result);
}

char	**ft_split(char const *s, char c)
{
	char	**result;

	if (!s)
		return (NULL);
	result = (char **)malloc(sizeof(char *) * (count_words(s, c) + 1));
	if (!result)
		return (NULL);
	return (fill_result(s, c, result));
}
