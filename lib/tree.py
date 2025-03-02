class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, id):
        """
        Traverse the tree using depth-first search to find the node with the given id.

        :param id: The id to search for.
        :return: The node with the matching id, or None if not found.
        """
        def dfs(node):
            # Base case: if the node is None, return None
            if not node:
                return None

            # Check if the current node's id matches
            if node.get('id') == id:
                return node

            # Recursively check each child node
            for child in node.get('children', []):
                result = dfs(child)
                if result:  # If a matching node is found, return it
                    return result

            return None  # Return None if no matching node is found in this branch

        # Start the DFS from the root of the tree
        return dfs(self.root)
