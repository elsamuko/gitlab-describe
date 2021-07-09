#!/usr/bin/env python3
# python3 -m pip install python-gitlab

import gitlab
import os

token = "" # os.environ["GITLAB_TOKEN"]
gl = gitlab.Gitlab("https://gitlab.com", private_token=token)

gimp = gl.projects.get("elsamuko/test")
tags = gimp.tags.list()
last_tag = tags[0]
# print(f"{last_tag.name} => {last_tag.commit['created_at']}")

commits = gimp.commits.list(since=last_tag.commit['created_at'])
since = len(commits) - 1
last_commit = commits[0]

# https://github.com/git/git/blob/49f38e2de47a401fc2b0f4cce38e9f07fb63df48/builtin/describe.c#L299
print(f"{last_tag.name}-{since}-g{last_commit.short_id}")
