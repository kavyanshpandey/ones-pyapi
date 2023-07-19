"""
Copyright (c) 2023, Aviz Networks

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from endpoints import *
from exceptions import *
from constants import *
from utils import get_request_handler, post_request_handler


class FMClient(object):
    # FMClient will use for all Orchestration/ 
    # Configuration related operations

    # Since FM APIs is not returning any status
    # Directly sending response

    def __init__(self, url=None):
        self.url = url


    def get_controller_version(self):
        """
        Input params -> None
        Output -> return controller version
        """
        return get_request_handler(self.url, controller_version_endpoint, CONTROLLER_VERSION_INFO_ERROR, None)


    def get_intent_status(self, intent_name_file):
        """
        Api to retrieve over all status for the given intent yaml file. 
        This provides data to data grid which shows sub intent specific status single tick 
        and double tick \

        Query pararms - > intentName= .yamlfile
        """
        return get_request_handler(self.url, intent_status_endpoint, INTENT_STATUS_ERROR, intent_name_file)


    def reboot(self, list_of_ips):
        """
        To trigger the reboot request

        Method -> Post
        Payload -> list of IPs -> ["10.x.x.1","11.x.x.2"]
        """
        return post_request_handler(self.url, reboot_endpoint, REBOOT_ERROR, list_of_ips)
        

    def ztp_enable(self, list_of_ips):
        """
        Trigger the ZTP, it take one more device IPs as input

        Method -> Post 
        Payload -> list of IPs -> ["10.x.x.1","11.x.x.2"]
        """
        return post_request_handler(self.url, ztp_enable_endpoint, ZTP_ENABLE_ERROR, list_of_ips)


    def controller_fm_version(self, list_of_ips):
        """
        To get the Controller version and FM agent version
        Method -> Post 
        Payload -> list of IPs -> ["10.x.x.1","11.x.x.2"]
        """
        return post_request_handler(self.url, controller_fm_version_endpoint, CONTROLLER_VERSION_INFO_ERROR, list_of_ips)


    def get_image_mgmnt_status(self, list_of_ips):
        """
        Get ongoing reboot and image upgrade status, 
        this will help in selecting particular device from grid.
        Method -> Post
        Payload -> list of IPs -> ["10.x.x.1","11.x.x.2"]
        """
        return post_request_handler(self.url, image_mgmnt_status_endpoint, IMG_MGMNT_ERROR, list_of_ips)


    def custom_image_upgrade(self, payload):
        """
        To Trigger custom Image upgrade request
        Method -> Post
        payload -> [{"ip":"1.x.x.x","pathToImage":"path_of_image"}]
        """
        return post_request_handler(self.url, custom_image_upgrade_endpoint, payload)


    def get_config_diff(self, ip_address):
        """
        To get the data to show in config diff in UI, this getting called
        payload -> { "ip": "10.x.x.x"}
        """
        return post_request_handler(self.url, config_diff_endpoint, CONFIG_DIFF_ERROR, ip_address)