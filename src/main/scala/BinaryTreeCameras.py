class Solution:
    def minCameraCover(self, root) -> int:
        if not root:
            return 0

        def is_leaf(node):
            return not node.left and not node.right

        if is_leaf(root):
            return 1

        cameras = set()

        def place_camera(cameras, node):
            if not node or is_leaf(node):
                return
            place_camera(cameras, node.left)
            place_camera(cameras, node.right)
            if node.left in cameras and node.right in cameras or not node.left and node.right in cameras or not node.right and node.left in cameras:
                return
            cameras.add(node)

        place_camera(cameras, root)
        return len(cameras)