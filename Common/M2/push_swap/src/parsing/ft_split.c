/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pabrogi <pabrogi@student.42firenze.it>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/02 14:32:16 by pabrogi           #+#    #+#             */
/*   Updated: 2026/02/02 14:32:17 by pabrogi          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../include/push_swap.h"

static int	count_words(char const *s, char c)
{
	int	count;
	int	in_word;

	count = 0;
	in_word = 0;
	while (*s)
	{
		if (*s != c && !in_word)
		{
			in_word = 1;
			count++;
		}
		else if (*s == c)
			in_word = 0;
		s++;
	}
	return (count);
}

static char	*get_word(char const *s, char c)
{
	int		len;
	int		i;
	char	*word;

	len = 0;
	while (s[len] && s[len] != c)
		len++;
	word = (char *)malloc(sizeof(char) * (len + 1));
	if (!word)
		return (NULL);
	i = 0;
	while (i < len)
	{
		word[i] = s[i];
		i++;
	}
	word[i] = '\0';
	return (word);
}

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
