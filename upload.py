from tiktok import TikTokApi

api = TikTokApi()

api.login(username='your_username', password='your_password')

video_path = './Video/test.mp4'

response = api.upload_video(video_path)
