---
title: "Getting Started"
layout: page
date: 2099-06-02 00:00
---

```cpp
// 递归
class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if(root == NULL) return root;
        std::swap(root->left, root->right);
        invertTree(root->left);
        invertTree(root->right);
        return root;
    }
};

// 非递归
```