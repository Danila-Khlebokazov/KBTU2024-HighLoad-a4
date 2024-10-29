from locust import HttpUser, TaskSet, task
import uuid


class UserBehavior(TaskSet):

    @task(1)
    def common(self):
        site_user = str(uuid.uuid4())
        email = f"{site_user}@abc.df"
        password = "pa$$word123__"

        self.client.post("/api/auth/register/", json={
            "username": site_user,
            "email": email,
            "password": password
        })

        response = self.client.post("/api/auth/login/", json={
            "username": site_user,
            "password": password
        })
        token = response.json()["token"]
        self.client.post("/api/tasks/async", json={
            "send_to": email,
            "subject": f"Load Test {site_user}",
            "body": "This is a load test email."
        }, headers={
            "Authorization": f"Token {token}"
        })
        self.client.post("/api/auth/logout/", headers={
            "Authorization": f"Token {token}"
        })


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    min_wait = 1000
    max_wait = 3000
