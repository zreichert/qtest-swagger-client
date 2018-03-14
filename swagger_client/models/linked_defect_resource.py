# coding: utf-8

"""
    qTest Manager API Version 8.6 - 9.0

    qTest Manager API Version 8.6 - 9.0

    OpenAPI spec version: 8.6 - 9.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class LinkedDefectResource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, links=None, id=None, external_defect_id=None, connection_id=None, external_project_id=None, summary=None, status=None, pid=None, web_url=None, description=None):
        """
        LinkedDefectResource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'links': 'list[Link]',
            'id': 'int',
            'external_defect_id': 'str',
            'connection_id': 'int',
            'external_project_id': 'str',
            'summary': 'str',
            'status': 'str',
            'pid': 'str',
            'web_url': 'str',
            'description': 'str'
        }

        self.attribute_map = {
            'links': 'links',
            'id': 'id',
            'external_defect_id': 'external_defect_id',
            'connection_id': 'connection_id',
            'external_project_id': 'external_project_id',
            'summary': 'summary',
            'status': 'status',
            'pid': 'pid',
            'web_url': 'web_url',
            'description': 'description'
        }

        self._links = links
        self._id = id
        self._external_defect_id = external_defect_id
        self._connection_id = connection_id
        self._external_project_id = external_project_id
        self._summary = summary
        self._status = status
        self._pid = pid
        self._web_url = web_url
        self._description = description

    @property
    def links(self):
        """
        Gets the links of this LinkedDefectResource.

        :return: The links of this LinkedDefectResource.
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this LinkedDefectResource.

        :param links: The links of this LinkedDefectResource.
        :type: list[Link]
        """

        self._links = links

    @property
    def id(self):
        """
        Gets the id of this LinkedDefectResource.
        ID of Defect

        :return: The id of this LinkedDefectResource.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this LinkedDefectResource.
        ID of Defect

        :param id: The id of this LinkedDefectResource.
        :type: int
        """

        self._id = id

    @property
    def external_defect_id(self):
        """
        Gets the external_defect_id of this LinkedDefectResource.
        External ID of Defect

        :return: The external_defect_id of this LinkedDefectResource.
        :rtype: str
        """
        return self._external_defect_id

    @external_defect_id.setter
    def external_defect_id(self, external_defect_id):
        """
        Sets the external_defect_id of this LinkedDefectResource.
        External ID of Defect

        :param external_defect_id: The external_defect_id of this LinkedDefectResource.
        :type: str
        """

        self._external_defect_id = external_defect_id

    @property
    def connection_id(self):
        """
        Gets the connection_id of this LinkedDefectResource.
        ID of the external Integration Connection

        :return: The connection_id of this LinkedDefectResource.
        :rtype: int
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        """
        Sets the connection_id of this LinkedDefectResource.
        ID of the external Integration Connection

        :param connection_id: The connection_id of this LinkedDefectResource.
        :type: int
        """

        self._connection_id = connection_id

    @property
    def external_project_id(self):
        """
        Gets the external_project_id of this LinkedDefectResource.
        ID of external Project

        :return: The external_project_id of this LinkedDefectResource.
        :rtype: str
        """
        return self._external_project_id

    @external_project_id.setter
    def external_project_id(self, external_project_id):
        """
        Sets the external_project_id of this LinkedDefectResource.
        ID of external Project

        :param external_project_id: The external_project_id of this LinkedDefectResource.
        :type: str
        """

        self._external_project_id = external_project_id

    @property
    def summary(self):
        """
        Gets the summary of this LinkedDefectResource.
        Summary of external Defect

        :return: The summary of this LinkedDefectResource.
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """
        Sets the summary of this LinkedDefectResource.
        Summary of external Defect

        :param summary: The summary of this LinkedDefectResource.
        :type: str
        """

        self._summary = summary

    @property
    def status(self):
        """
        Gets the status of this LinkedDefectResource.
        Status of external Defect

        :return: The status of this LinkedDefectResource.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this LinkedDefectResource.
        Status of external Defect

        :param status: The status of this LinkedDefectResource.
        :type: str
        """

        self._status = status

    @property
    def pid(self):
        """
        Gets the pid of this LinkedDefectResource.
        PID of external Defect

        :return: The pid of this LinkedDefectResource.
        :rtype: str
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        """
        Sets the pid of this LinkedDefectResource.
        PID of external Defect

        :param pid: The pid of this LinkedDefectResource.
        :type: str
        """

        self._pid = pid

    @property
    def web_url(self):
        """
        Gets the web_url of this LinkedDefectResource.
        Web url to external Defect

        :return: The web_url of this LinkedDefectResource.
        :rtype: str
        """
        return self._web_url

    @web_url.setter
    def web_url(self, web_url):
        """
        Sets the web_url of this LinkedDefectResource.
        Web url to external Defect

        :param web_url: The web_url of this LinkedDefectResource.
        :type: str
        """

        self._web_url = web_url

    @property
    def description(self):
        """
        Gets the description of this LinkedDefectResource.
        Description of external Defect

        :return: The description of this LinkedDefectResource.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this LinkedDefectResource.
        Description of external Defect

        :param description: The description of this LinkedDefectResource.
        :type: str
        """

        self._description = description

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, LinkedDefectResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other