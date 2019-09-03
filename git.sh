#!/bin/bash
# Created by wGodlike at 2019-09-03 10:38
# shellcheck disable=SC2045
# shellcheck disable=SC2006
# shellcheck disable=SC2086

# 1. 安装git
# 2. git创建远程仓库(Linux仓库机器)
git init --bare wGodlike.git
# 4. 本地仓库初始化
git init
# 5. 工作区提交到暂存区
git add -A
# 6. 暂存区提交代码到本地仓库
git commit -m
# 7. 建立远程跟踪
git remote add origin root@10.211.55.5:/opt/wGodlike.git
# 8. 本地仓库分支关联远程仓库master分支
git push --set-upstream origin master
# 9. 本地仓库提交到远程分支
git push origin master

# 11.查看已存在的分支名称
git branch
# 12.本地创建新分支
git branch test
# 13.本地切换分支
git checkout master
# 14.分支合并 test分支合并到master
git merge test master
# 15.本地仓库提交到远程仓库
git push

# 删除远程文件或文件夹
git rm -r -n --cached .idea  # -n 代表查看要删除的文件夹和文件名称
git rm -r --cached .idea  # 删除本地暂存区文件夹或文件(以及关联关系)
git commit -m '删除.idea'  # 删除本地仓库文件夹或文件
git push                  # 删除远程仓库文件夹或文件
