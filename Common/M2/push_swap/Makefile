# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pabrogi <pabrogi@student.42firenze.it>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/10 13:22:45 by pabrogi           #+#    #+#              #
#    Updated: 2026/01/31 22:20:33 by pabrogi          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

CC = cc
CFLAGS = -Wall -Wextra -Werror
NAME = push_swap

SRCS = src/main.c \
       src/operations/push.c \
       src/operations/swap.c \
       src/operations/rotate.c \
       src/operations/reverse_rotate.c \
       src/sorting/sort.c \
       src/sorting/sort_for_small.c \
       src/sorting/cost_args.c \
       src/sorting/searchposition.c \
       src/parsing/parse_input.c \
       src/parsing/ft_split.c \
       src/parsing/ft_utils.c \
       src/utils/utils_lib.c \
       src/utils/stack_utils.c \
       src/utils/error_in.c \
       src/utils/index_argument.c

OBJS = $(SRCS:.c=.o)

all: $(NAME)

$(NAME): $(OBJS)
	$(CC) $(CFLAGS) $(OBJS) -o $(NAME)

%.o: %.c
	$(CC) $(CFLAGS) -I./include -c $< -o $@

clean:
	rm -f $(OBJS)

fclean: clean
	rm -f $(NAME)

re: fclean all

.PHONY: all clean fclean re
