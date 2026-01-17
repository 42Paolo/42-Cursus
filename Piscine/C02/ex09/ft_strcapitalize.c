/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strcapitalize.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pabrogi <pabrogi@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/15 15:03:31 by pabrogi           #+#    #+#             */
/*   Updated: 2025/10/15 17:36:40 by pabrogi          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_str_is_alpha(char str)
{
	if (!((str >= 65 && str <= 90) || (str >= 97 && str <= 122)))
		return (0);
	return (1);
}

int	ft_str_is_uppercase(char str)
{
	if (!(str >= 65 && str <= 90))
		return (0);
	return (1);
}

int	ft_str_is_lowercase(char str)
{
	if (!(str >= 97 && str <= 122))
		return (0);
	return (1);
}

int	ft_str_is_numeric(char str)
{
	if (!(str >= 48 && str <= 57))
		return (0);
	return (1);
}

char	*ft_strcapitalize(char *str)
{
	char	*temp_str;
	int		flag_word;

	flag_word = 1;
	temp_str = str;
	while (*temp_str)
	{
		if (ft_str_is_alpha(*temp_str))
		{
			if (ft_str_is_lowercase(*temp_str) && flag_word)
				*temp_str -= 32;
			else if (ft_str_is_uppercase(*temp_str) && !flag_word)
				*temp_str += 32;
			flag_word = 0;
		}
		else if (ft_str_is_numeric(*temp_str))
			flag_word = 0;
		else
			flag_word = 1;
		temp_str++;
	}
	return (str);
}
