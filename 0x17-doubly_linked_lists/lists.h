#ifndef LIST_H
#define LIST_H

#include <stddef.h>

/* Definition of the doubly linked list structure */
typedef struct dlistint_s
{
    int n;
    struct dlistint_s *prev;
    struct dlistint_s *next;
} dlistint_t;

/* Function prototypes */
size_t print_dlistint(const dlistint_t *h);

#endif /* LIST_H */

