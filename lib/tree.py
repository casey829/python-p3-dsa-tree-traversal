class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    return  self._bfs(self.root, id)
  
  def _bfs(self, root, id):
    if root is None:
      return None
    queue = [root]
    while queue:
      node = queue.pop(0)
      if node.get('id') == id:
        return node
      queue.extend(node.get('children', []))
    return None
     