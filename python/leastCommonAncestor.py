def checkPath(root, p, q):
    # while root.left != None and root.right != None:
    #global output
    if root.val == p or root.val == q:
        here = True
    if root.left:
        left = checkPath(root.left, p, q)
    if root.right:
        right = checkPath(root.right, p, q)
    if (left and right) or (left and here) or (right and here):
        global output
        output = root.val

    return left or here or right


checkPath([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 1)
