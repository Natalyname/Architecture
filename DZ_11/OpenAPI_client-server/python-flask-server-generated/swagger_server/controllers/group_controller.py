import connexion
import six

from swagger_server.models.group import Group  # noqa: E501
from swagger_server import util


def add_group(body):  # noqa: E501
    """Добавить группу

    Добавить группу в базу # noqa: E501

    :param body: Создание новой группы в базе
    :type body: dict | bytes

    :rtype: Group
    """
    if connexion.request.is_json:
        body = Group.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def add_group(id, user_id):  # noqa: E501
    """Добавить группу

    Добавить группу в базу # noqa: E501

    :param id: 
    :type id: int
    :param user_id: 
    :type user_id: int

    :rtype: Group
    """
    return 'do some magic!'


def delete_group(group_id, group_id=None):  # noqa: E501
    """Удаляет пользователя

    Удаляет пользователя # noqa: E501

    :param group_id: ID пользователя
    :type group_id: int
    :param group_id: 
    :type group_id: str

    :rtype: None
    """
    return 'do some magic!'


def get_group_by_id(group_id):  # noqa: E501
    """Найти группу по ID

    вернуть группу # noqa: E501

    :param group_id: Идентификатор группы
    :type group_id: int

    :rtype: Group
    """
    return 'do some magic!'


def update_group(body):  # noqa: E501
    """Обновить группу

    Обновить группу # noqa: E501

    :param body: Обновить существующую группу в базе
    :type body: dict | bytes

    :rtype: Group
    """
    if connexion.request.is_json:
        body = Group.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_group(id, user_id):  # noqa: E501
    """Обновить группу

    Обновить группу # noqa: E501

    :param id: 
    :type id: int
    :param user_id: 
    :type user_id: int

    :rtype: Group
    """
    return 'do some magic!'
