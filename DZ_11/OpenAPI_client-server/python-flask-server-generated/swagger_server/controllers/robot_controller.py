import connexion
import six

from swagger_server.models.robot import Robot  # noqa: E501
from swagger_server import util


def add_robot(body):  # noqa: E501
    """Добавить робота

    Добавить робота в базу # noqa: E501

    :param body: Создание нового робота в базе
    :type body: dict | bytes

    :rtype: Robot
    """
    if connexion.request.is_json:
        body = Robot.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def add_robot(id, model, version, charge, garbage_container, robot_contamination, next_service, serial_number, ip_address, group_id):  # noqa: E501
    """Добавить робота

    Добавить робота в базу # noqa: E501

    :param id: 
    :type id: int
    :param model: 
    :type model: str
    :param version: 
    :type version: str
    :param charge: 
    :type charge: int
    :param garbage_container: 
    :type garbage_container: int
    :param robot_contamination: 
    :type robot_contamination: int
    :param next_service: 
    :type next_service: int
    :param serial_number: 
    :type serial_number: str
    :param ip_address: 
    :type ip_address: int
    :param group_id: 
    :type group_id: int

    :rtype: Robot
    """
    return 'do some magic!'


def delete_robot(robot_id, robot_id=None):  # noqa: E501
    """Удаляет робота

    Удаляет робота # noqa: E501

    :param robot_id: ID робота
    :type robot_id: int
    :param robot_id: 
    :type robot_id: str

    :rtype: None
    """
    return 'do some magic!'


def get_robot_by_id(robot_id):  # noqa: E501
    """Найти робота по ID

    вернуть робота # noqa: E501

    :param robot_id: Идентификатор робота
    :type robot_id: int

    :rtype: Robot
    """
    return 'do some magic!'


def update_robot(body):  # noqa: E501
    """Обновить робота

    Обновить робота # noqa: E501

    :param body: Обновить существующего робота в базе
    :type body: dict | bytes

    :rtype: Robot
    """
    if connexion.request.is_json:
        body = Robot.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_robot(id, model, version, charge, garbage_container, robot_contamination, next_service, serial_number, ip_address, group_id):  # noqa: E501
    """Обновить робота

    Обновить робота # noqa: E501

    :param id: 
    :type id: int
    :param model: 
    :type model: str
    :param version: 
    :type version: str
    :param charge: 
    :type charge: int
    :param garbage_container: 
    :type garbage_container: int
    :param robot_contamination: 
    :type robot_contamination: int
    :param next_service: 
    :type next_service: int
    :param serial_number: 
    :type serial_number: str
    :param ip_address: 
    :type ip_address: int
    :param group_id: 
    :type group_id: int

    :rtype: Robot
    """
    return 'do some magic!'
