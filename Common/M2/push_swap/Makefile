# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pabrogi <pabrogi@student.42firenze.it>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/17 16:26:28 by pabrogi           #+#    #+#              #
#    Updated: 2026/01/17 16:26:39 by pabrogi          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME = push_swap

SRC_DIR = src
OBJ_DIR = obj
INC_DIR = includes
LIBFT_DIR = libft

CC = cc
CFLAGS = -Wall -Wextra -Werror
INCLUDES = -I$(INC_DIR) -I$(LIBFT_DIR)/includes

LIBFT = $(LIBFT_DIR)/libft.a
LDFLAGS = -L$(LIBFT_DIR) -lft

MAIN_SRC = $(SRC_DIR)/main.c

STACK_SRCS = $(SRC_DIR)/stack/stack_init.c \
			 $(SRC_DIR)/stack/stack_operations.c \
			 $(SRC_DIR)/stack/stack_utils.c

OPS_SRCS = $(SRC_DIR)/operations/push.c \
		   $(SRC_DIR)/operations/swap.c \
		   $(SRC_DIR)/operations/rotate.c \
		   $(SRC_DIR)/operations/reverse_rotate.c

PARSER_SRCS = $(SRC_DIR)/parser/parse_input.c \
			  $(SRC_DIR)/parser/validate.c \
			  $(SRC_DIR)/parser/convert.c

SOLVER_SRCS = $(SRC_DIR)/solver/small_sort.c \
			  $(SRC_DIR)/solver/large_sort.c \
			  $(SRC_DIR)/solver/chunk_sort.c \
			  $(SRC_DIR)/solver/optimize_moves.c

UTILS_SRCS = $(SRC_DIR)/utils/errors.c \
			 $(SRC_DIR)/utils/memory.c \
			 $(SRC_DIR)/utils/print.c

SRCS = $(MAIN_SRC) \
	   $(STACK_SRCS) \
	   $(OPS_SRCS) \
	   $(PARSER_SRCS) \
	   $(SOLVER_SRCS) \
	   $(UTILS_SRCS)

OBJS = $(SRCS:$(SRC_DIR)/%.c=$(OBJ_DIR)/%.o)

all: $(NAME)

$(NAME): $(LIBFT) $(OBJS)
	$(CC) $(CFLAGS) $(OBJS) $(LDFLAGS) -o $(NAME)

$(LIBFT):
	@if [ -d "$(LIBFT_DIR)" ]; then \
		$(MAKE) -C $(LIBFT_DIR); \
	fi

$(OBJ_DIR)/%.o: $(SRC_DIR)/%.c | $(OBJ_DIR)
	$(CC) $(CFLAGS) $(INCLUDES) -c $< -o $@

$(OBJ_DIR):
	mkdir -p $(OBJ_DIR)/stack
	mkdir -p $(OBJ_DIR)/operations
	mkdir -p $(OBJ_DIR)/parser
	mkdir -p $(OBJ_DIR)/solver
	mkdir -p $(OBJ_DIR)/utils

clean:
	rm -rf $(OBJ_DIR)
	@if [ -d "$(LIBFT_DIR)" ]; then \
		$(MAKE) -C $(LIBFT_DIR) clean; \
	fi

fclean: clean
	rm -f $(NAME)
	@if [ -d "$(LIBFT_DIR)" ]; then \
		$(MAKE) -C $(LIBFT_DIR) fclean; \
	fi

re: fclean all

.PHONY: all clean fclean re
