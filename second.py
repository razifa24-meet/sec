def createytvids(title1, description1):
  ytvid = {"title" : title1, "description" : description1, "likes" : 0, "dislikes" : 0, "comments":{}}
  return ytvid
  
def Likes(ytvid):
  if "likes" in ytvid:
    ytvid["likes"] += 1
  return ytvid


def disLikes(ytvid):
  if "dislikes" in ytvid:
    ytvid["dislikes"] += 1
  return ytvid

def addcom(ytvid, username, actcomment):
  ytvid["comments"].update({username: actcomment})


vid = createytvids("hi","welcome")

Likes(vid)
disLikes(vid)
addcom(vid,"razi","amazing")











