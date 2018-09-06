Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Example 1:


Input: [1,3,null,null,2]

&nbsp;  1
&nbsp; /
&nbsp;3
&nbsp; \
&nbsp;  2

Output: [3,1,null,null,2]

&nbsp;  3
&nbsp; /
&nbsp;1
&nbsp; \
&nbsp;  2


Example 2:


Input: [3,1,4,null,null,2]

  3
 / \
1   4
&nbsp;  /
&nbsp; 2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
&nbsp;  /
 &nbsp;3


Follow up:


	A solution using O(n) space is pretty straight forward.
	Could you devise a constant space solution?

