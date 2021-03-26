# Linked lists are mainly used in java because the user allocates ram for lists and such.
# LL have a head where the list begins and a tail where it ends, between are potentially an infinite number of 'nodes'
# A node contains an array element/item with a reference to the next node
# if adding/removing the first node (aka head) you can simply add a new node, point the head to it and refer that node to the rest of the LL. To delete, just point head to the second node
# Similarly with the Tail, just point to the second last 
# The head to remove/delete/update are O(1)
# Doing anything between including the tail will be O(n) since the LL could be 'n' length