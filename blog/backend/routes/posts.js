const express = require('express');
const router = express.Router();
const Post = require('../models/Post');

router.get('/:id', async (req, res) => {
  try {
    const post = await Post.findById(req.params.id);
    if (post == null) {
      return res.status(404).json({ message: 'Post not found' });
    }
    res.json(post);
  } catch (err) {
    return res.status(500).json({ message: err.message });
  }
});
router.get('/:id/preview', async (req, res) => {
  try {
    const post = await Post.findById(req.params.id);
    if (post == null) {
      return res.status(404).json({ message: 'Post not found' });
    }
    // 미리보기용 간단한 데이터만 전송
    const preview = {
      title: post.title,
      content: post.content.substring(0, 200) + '...' // 처음 200자만 전송
    };
    res.json(preview);
  } catch (err) {
    return res.status(500).json({ message: err.message });
  }
});

router.post('/', async (req, res) => {
  const post = new Post({
    title: req.body.title,
    content: req.body.content,
    category: req.body.category
  });

  try {
    const newPost = await post.save();
    res.status(201).json(newPost);
  } catch (err) {
    res.status(400).json({ message: err.message });
  }
});

module.exports = router;