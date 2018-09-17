CREATE TABLE IF NOT EXISTS `user`(
   `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '用户ID',
   `delete_flag` tinyint(1) NOT NULL DEFAULT 0 COMMENT '删除标志',
   `name` VARCHAR(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '昵称',
   `phone` VARCHAR(11) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '电话',
   `email` VARCHAR(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '邮箱',
   `password` VARCHAR(16) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '密码',
   `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
   PRIMARY KEY ( `id` ),
   INDEX `email` (`email`) USING BTREE,
   INDEX `phone` (`phone`) USING BTREE
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8 COLLATE=utf8_general_ci
ROW_FORMAT=DYNAMIC
;


CREATE TABLE IF NOT EXISTS `question`(
   `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '问题ID',
   `delete_flag` tinyint(1) NOT NULL DEFAULT 0 COMMENT '删除标志',
   `user_id` INT(11) NOT NULL COMMENT '用户ID',
   `question_text` VARCHAR(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '问题内容',
   `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
   PRIMARY KEY ( `id` ),
   FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
   INDEX `user_id` (`user_id`) USING BTREE
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8 COLLATE=utf8_general_ci
ROW_FORMAT=DYNAMIC
;


CREATE TABLE IF NOT EXISTS `choice`(
   `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '选择ID',
   `delete_flag` tinyint(1) NOT NULL DEFAULT 0 COMMENT '删除标志',
   `choice_text` VARCHAR(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '选择内容',
   `votes` INT(11) NOT NULL COMMENT '得票数',
   `question_id` INT(11) NOT NULL COMMENT '问题ID',
   `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
   PRIMARY KEY ( `id` ),
   FOREIGN KEY (`question_id`) REFERENCES `question` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
   INDEX `question_id` (`question_id`) USING BTREE
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8 COLLATE=utf8_general_ci
ROW_FORMAT=DYNAMIC
;