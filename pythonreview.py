def create_youtube_video("title", "description"):
	youtubeVideo = {"title": title, "description": description, "likes":0, "dislikes":0, "comments":{}}
	return youtubeVideo

def like(youtubeVideo):
	youtubeVideo["likes"] +=1
	return youtubeVideo

def dislike(youtubeVideo):
	youtubeVideo["dislikes"] +=1
	return youtubeVideo

def add_comment():
	 

