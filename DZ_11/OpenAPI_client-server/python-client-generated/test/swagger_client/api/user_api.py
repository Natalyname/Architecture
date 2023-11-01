# coding: utf-8

"""
    Robot service 3.0

    API сервис управления роботом - пылесосом.  # noqa: E501

    OpenAPI spec version: 1.0.11
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class UserApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_user(self, body, **kwargs):  # noqa: E501
        """Добавить пользователя  # noqa: E501

        Добавить пользователя в базу  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_user(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param User body: Создание нового пользователя в базе (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_user_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.add_user_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def add_user_with_http_info(self, body, **kwargs):  # noqa: E501
        """Добавить пользователя  # noqa: E501

        Добавить пользователя в базу  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_user_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param User body: Создание нового пользователя в базе (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `add_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'id' in params:
            form_params.append(('id', params['id']))  # noqa: E501
        if 'email' in params:
            form_params.append(('email', params['email']))  # noqa: E501
        if 'pass_hash' in params:
            form_params.append(('passHash', params['pass_hash']))  # noqa: E501
        if 'robot_sn_hash' in params:
            form_params.append(('robotSNHash', params['robot_sn_hash']))  # noqa: E501

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/User', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='User',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def add_user(self, id, email, pass_hash, robot_sn_hash, **kwargs):  # noqa: E501
        """Добавить пользователя  # noqa: E501

        Добавить пользователя в базу  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_user(id, email, pass_hash, robot_sn_hash, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: (required)
        :param str email: (required)
        :param int pass_hash: (required)
        :param int robot_sn_hash: (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_user_with_http_info(id, email, pass_hash, robot_sn_hash, **kwargs)  # noqa: E501
        else:
            (data) = self.add_user_with_http_info(id, email, pass_hash, robot_sn_hash, **kwargs)  # noqa: E501
            return data

    def add_user_with_http_info(self, id, email, pass_hash, robot_sn_hash, **kwargs):  # noqa: E501
        """Добавить пользователя  # noqa: E501

        Добавить пользователя в базу  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_user_with_http_info(id, email, pass_hash, robot_sn_hash, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: (required)
        :param str email: (required)
        :param int pass_hash: (required)
        :param int robot_sn_hash: (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'email', 'pass_hash', 'robot_sn_hash']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `add_user`")  # noqa: E501
        # verify the required parameter 'email' is set
        if ('email' not in params or
                params['email'] is None):
            raise ValueError("Missing the required parameter `email` when calling `add_user`")  # noqa: E501
        # verify the required parameter 'pass_hash' is set
        if ('pass_hash' not in params or
                params['pass_hash'] is None):
            raise ValueError("Missing the required parameter `pass_hash` when calling `add_user`")  # noqa: E501
        # verify the required parameter 'robot_sn_hash' is set
        if ('robot_sn_hash' not in params or
                params['robot_sn_hash'] is None):
            raise ValueError("Missing the required parameter `robot_sn_hash` when calling `add_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'id' in params:
            form_params.append(('id', params['id']))  # noqa: E501
        if 'email' in params:
            form_params.append(('email', params['email']))  # noqa: E501
        if 'pass_hash' in params:
            form_params.append(('passHash', params['pass_hash']))  # noqa: E501
        if 'robot_sn_hash' in params:
            form_params.append(('robotSNHash', params['robot_sn_hash']))  # noqa: E501

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/User', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='User',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_user(self, user_id, **kwargs):  # noqa: E501
        """Удаляет пользователя  # noqa: E501

        Удаляет пользователя  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_user(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int user_id: ID пользователя (required)
        :param str user_id:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_user_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_user_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def delete_user_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """Удаляет пользователя  # noqa: E501

        Удаляет пользователя  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_user_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int user_id: ID пользователя (required)
        :param str user_id:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'user_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `delete_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'user_id' in params:
            header_params['userId'] = params['user_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/User/deleteById/{userId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_by_id(self, user_id, **kwargs):  # noqa: E501
        """Найти пользователя по ID  # noqa: E501

        вернуть одного пользователя  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_by_id(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int user_id: Идентификатор пользователя (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_by_id_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_by_id_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def get_user_by_id_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """Найти пользователя по ID  # noqa: E501

        вернуть одного пользователя  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_by_id_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int user_id: Идентификатор пользователя (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `get_user_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/User/findById/{userId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='User',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_user(self, user_id, **kwargs):  # noqa: E501
        """обновляет информацию о пользователе по ID  # noqa: E501

        обновляет информацию о пользователе  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_user(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int user_id: Идентификатор пользователя (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_user_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_user_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def update_user_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """обновляет информацию о пользователе по ID  # noqa: E501

        обновляет информацию о пользователе  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_user_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int user_id: Идентификатор пользователя (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `update_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/User/UpdateById/{userId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='User',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)