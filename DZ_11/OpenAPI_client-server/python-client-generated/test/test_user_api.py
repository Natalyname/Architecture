# coding: utf-8

"""
    Robot service 3.0

    API сервис управления роботом - пылесосом.  # noqa: E501

    OpenAPI spec version: 1.0.11
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.user_api import UserApi  # noqa: E501
from swagger_client.rest import ApiException


class TestUserApi(unittest.TestCase):
    """UserApi unit test stubs"""

    def setUp(self):
        self.api = UserApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_user(self):
        """Test case for add_user

        Добавить пользователя  # noqa: E501
        """
        pass

    def test_delete_user(self):
        """Test case for delete_user

        Удаляет пользователя  # noqa: E501
        """
        pass

    def test_get_user_by_id(self):
        """Test case for get_user_by_id

        Найти пользователя по ID  # noqa: E501
        """
        pass

    def test_update_user(self):
        """Test case for update_user

        обновляет информацию о пользователе по ID  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
