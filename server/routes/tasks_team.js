const express = require('express');
const router = express.Router();
const taskController = require('../controller/tasks_team');
const isMember = require('../middlewares/isMember');
const authMiddleware = require('../middlewares/auth-middleware');

// 팀 일정 생성
router.post(
  '/task/team/:workSpaceName',
  authMiddleware,
  isMember,
  taskController.teamTaskUpload
);

// 팀 전체 일정 조회
router.get(
  '/task/team/:workSpaceName',
  authMiddleware,
  isMember,
  taskController.teamTaskAll
);

// 팀 일정 상세 조회
router.get(
  '/task/team/:workSpaceName/:taskId',
  authMiddleware,
  isMember,
  taskController.teamTaskDetail
);

// 팀 일정 수정
router.put(
  '/task/team/:workSpaceName/:taskId',
  authMiddleware,
  isMember,
  taskController.teamTaskEdit
);

// 팀 일정 삭제
router.delete(
  '/task/team/:workSpaceName/:taskId',
  authMiddleware,
  isMember,
  taskController.teamTaskRemove
);

module.exports = router;
