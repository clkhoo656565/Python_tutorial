from user import User
from post import Post

app_user_one = User("khoo@dxc.com", "Khoo, Chee Long", "pwd1", "DevOps Engineer")
app_user_one.get_user_info()

app_user_one.change_job_title("Tech Lead")
app_user_one.get_user_info()

app_user_two = User("khooYT@dxc.com", "Khoo, Yi Teng", "pwd9", "Son")
app_user_two.get_user_info()

new_post = Post("Hellow World from", app_user_one.name)
new_post.get_post_info()
