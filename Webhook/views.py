from django.shortcuts import render
from RestApi.response import RestResponse,ResponseStatus
from rest_framework import generics

import os

# Create your views here.


class OSChinaWebhook(generics.GenericAPIView):
    """
    OSChina webhook 功能
    """

    project_path = None
    password = None

    def post(self, request, *args, **kwargs):
        data = request.data
        hook_name = data.get('hook_name')
        password = data.get('password')

        if hook_name != "push_hooks":
            return RestResponse(data=None,status=ResponseStatus.UNSUPPORT_ACTION)
        
        if password != self.password:
            return RestResponse(data=None,status=ResponseStatus.PARAMS_ERROR)
        
        current_path = os.path.dirname(os.path.realpath(__file__))
        cmd = "sh "+ current_path+"/deploy.sh " + self.project_path
        os.system(cmd)
        return RestResponse(data=None,status=ResponseStatus.OK)



class SwaggerDocDeployView(OSChinaWebhook):
    """
    SwaggerDoc 自动部署
    """
    project_path = "/data/web/zh.1234tv.com/doc/swagger-ui/dist/swagger-doc"
    password = "swaggerdoc"