/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: pabrogi <pabrogi@student.42firenze.it>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/02 14:32:16 by pabrogi           #+#    #+#             */
/*   Updated: 2026/02/02 17:40:22 by pabrogi          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

# include <unistd.h>
# include <stdlib.h>
# include <limits.h>

typedef struct s_stack
{
	int				value;
	int				index;
	int				pos;
	int				target_pos;
	int				cost_a;
	int				cost_b;
	struct s_stack	*next;
}	t_stack;

void	error_exit(void);
void	free_stack(t_stack **stack);
void	free_split(char **split);

int		is_number(char *str);
int		has_duplicates(t_stack *stack);
int		count_words(char const *s, char c);
char	*get_word(char const *s, char c);
void	parse_arguments(int argc, char **argv, t_stack **stack_a);
char	**ft_split(char const *s, char c);

void	sa(t_stack **stack_a, int print);
void	sb(t_stack **stack_b, int print);
void	ss(t_stack **stack_a, t_stack **stack_b, int print);
void	pa(t_stack **stack_a, t_stack **stack_b, int print);
void	pb(t_stack **stack_a, t_stack **stack_b, int print);
void	ra(t_stack **stack_a, int print);
void	rb(t_stack **stack_b, int print);
void	rr(t_stack **stack_a, t_stack **stack_b, int print);
void	rra(t_stack **stack_a, int print);
void	rrb(t_stack **stack_b, int print);
void	rrr(t_stack **stack_a, t_stack **stack_b, int print);

t_stack	*get_bottom(t_stack *stack);
t_stack	*get_before_bottom(t_stack *stack);
t_stack	*stack_new(int value);
void	stack_add_bottom(t_stack **stack, t_stack *new_);
int		stack_size(t_stack *stack);
int		is_sorted(t_stack *stack);

void	assign_index(t_stack *stack_a, int stack_size);
int		get_min_index_pos(t_stack **stack);

void	sort_small(t_stack **stack_a, t_stack **stack_b);
void	sort_three(t_stack **stack_a);
void	sort(t_stack **stack_a, t_stack **stack_b);

void	get_position(t_stack **stack);
void	get_target_position(t_stack **stack_a, t_stack **stack_b);
void	get_cost(t_stack **stack_a, t_stack **stack_b);
void	do_cheapest_move(t_stack **stack_a, t_stack **stack_b);

long	ft_atol(const char *str);
void	ft_putstr(char *str);
int		ft_abs(int n);
int		get_highest_index(t_stack *stack);

#endif
