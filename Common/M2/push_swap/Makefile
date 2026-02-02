# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pabrogi <pabrogi@student.42firenze.it>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/02 14:32:16 by pabrogi           #+#    #+#              #
#    Updated: 2026/02/02 14:32:17 by pabrogi          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

CC = cc
CFLAGS = -Wall -Wextra -Werror -I./include
NAME = push_swap

SRC_DIR = src
OBJ_DIR = obj
INC_DIR = include

OPERATIONS = $(SRC_DIR)/operations/push.c \
             $(SRC_DIR)/operations/swap.c \
             $(SRC_DIR)/operations/rotate.c \
             $(SRC_DIR)/operations/reverse_rotate.c

SORTING = $(SRC_DIR)/sorting/sort.c \
          $(SRC_DIR)/sorting/sort_small.c \
          $(SRC_DIR)/sorting/cost.c \
          $(SRC_DIR)/sorting/position.c

PARSING = $(SRC_DIR)/parsing/parse.c \
          $(SRC_DIR)/parsing/ft_split.c

UTILS = $(SRC_DIR)/utils/utils.c \
        $(SRC_DIR)/utils/stack_utils.c \
        $(SRC_DIR)/utils/error.c \
        $(SRC_DIR)/utils/index.c

SRCS = $(SRC_DIR)/main.c \
       $(OPERATIONS) \
       $(SORTING) \
       $(PARSING) \
       $(UTILS)

OBJS = $(SRCS:$(SRC_DIR)/%.c=$(OBJ_DIR)/%.o)

all: $(NAME)

$(NAME): $(OBJS)
	$(CC) $(CFLAGS) $(OBJS) -o $(NAME)

$(OBJ_DIR)/%.o: $(SRC_DIR)/%.c
	@mkdir -p $(dir $@)
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -rf $(OBJ_DIR)

fclean: clean
	rm -f $(NAME)

re: fclean all

.PHONY: all clean fclean re
