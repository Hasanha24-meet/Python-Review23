def create_youtube_video(title, description):
  youtubeVideo = {"title": title, "description": description, "likes": 0, "dislikes": 0, "comments": {}}
  return youtubeVideo

def like(youtubeVideo):
  if "likes" in youtubeVideo:
    youtubeVideo["likes"] += 1
  return youtubeVideo

def dislike(youtubeVideo):
  if "dislikes" in youtubeVideo:
    youtubeVideo["dislikes"] += 1
  return youtubeVideo

def add_comment(youtubeVideo, username, comment_text):
  if "comments" not in youtubeVideo:
    youtubeVideo["comments"] = {}
  youtubeVideo["comments"][username] = comment_text
  return youtubeVideo

youtubeVideo = create_youtube_video("My First Video", "This is my first video on YouTube.")

print(youtubeVideo)

youtubeVideo = like(youtubeVideo)
print(youtubeVideo)

youtubeVideo = dislike(youtubeVideo)
print(youtubeVideo)

youtubeVideo = add_comment(youtubeVideo, "Hellooo!", "This is a great video!")
print(youtubeVideo)

youtubeVideo = int(youtubeVideo["likes"]) + 494
print(youtubeVideo)
