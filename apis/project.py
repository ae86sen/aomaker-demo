# --coding:utf-8--
from aomaker import aomaker

from apis.user import user_obj
from apis.base import MyBaseApi


class Project(MyBaseApi):
    def get_projects(self):
        """获取所有项目"""
        http_data = {
            'api_path': '/project/list',
            'method': 'get',
            'params': {'page': '1', 'size': '10'}
        }
        resp = self.send_http(http_data)
        return resp

    @aomaker.update("project_info")
    @aomaker.dependence(user_obj.get_users, "user_info")
    def create_project(self):
        """新增项目"""
        user_id = self.cache.get_by_jsonpath("user_info", jsonpath_expr="$..[?(@.name=='tester')].id")
        project_name = self.get_random_name("project")
        self.cache.set("project_name", project_name)
        http_data = {
            'api_path': '/project/insert',
            'method': 'post',
            'json': {
                "name": project_name,
                "app": "ad",
                "owner": user_id,
                "description": "a",
                "private": True
            }
        }
        resp = self.send_http(http_data)
        return resp


project_obj = Project()
