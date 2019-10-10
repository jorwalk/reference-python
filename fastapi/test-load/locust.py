from locust import HttpLocust, TaskSet

import resource
resource.setrlimit(resource.RLIMIT_NOFILE, (10240, 9223372036854775807))

# def login(l):
#     l.client.post("/login", {"username":"ellen_key", "password":"education"})
#
# def logout(l):
#     l.client.post("/logout", {"username":"ellen_key", "password":"education"})

def index(l):
    l.client.get("/")

# def profile(l):
#     l.client.get("/profile")

class UserBehavior(TaskSet):
    tasks = {
        index: 2,
        # profile: 1
    }

    def on_start(self):
        print("on start")
        # login(self)

    def on_stop(self):
        print("on stop")

        # logout(self)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000