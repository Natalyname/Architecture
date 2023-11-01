import connexion
import six

from swagger_server.models.schedule import Schedule  # noqa: E501
from swagger_server import util


def add_schedule(body):  # noqa: E501
    """Добавить расписание

    Добавить расписание в базу # noqa: E501

    :param body: Создать новое расписание в базе
    :type body: dict | bytes

    :rtype: Schedule
    """
    if connexion.request.is_json:
        body = Schedule.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def add_schedule(id, date_time, mode, robot_id):  # noqa: E501
    """Добавить расписание

    Добавить расписание в базу # noqa: E501

    :param id: 
    :type id: int
    :param date_time: 
    :type date_time: str
    :param mode: 
    :type mode: int
    :param robot_id: 
    :type robot_id: int

    :rtype: Schedule
    """
    return 'do some magic!'


def delete_schedule_by_id(schedule_id, schedule_id=None):  # noqa: E501
    """Удалить расписание по ID

    Удаляет расписание # noqa: E501

    :param schedule_id: 
    :type schedule_id: int
    :param schedule_id: Идентификатор расписания
    :type schedule_id: str

    :rtype: Schedule
    """
    return 'do some magic!'


def get_schedule_by_id(schedule_id):  # noqa: E501
    """Найти расписание по ID

    вернуть одно расписание # noqa: E501

    :param schedule_id: Идентификатор расписания
    :type schedule_id: int

    :rtype: Schedule
    """
    return 'do some magic!'


def update_schedule(body):  # noqa: E501
    """Обновить расписание

    Обновить расписание # noqa: E501

    :param body: Обновить существующее расписание в базе
    :type body: dict | bytes

    :rtype: Schedule
    """
    if connexion.request.is_json:
        body = Schedule.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_schedule(id, date_time, mode, robot_id):  # noqa: E501
    """Обновить расписание

    Обновить расписание # noqa: E501

    :param id: 
    :type id: int
    :param date_time: 
    :type date_time: str
    :param mode: 
    :type mode: int
    :param robot_id: 
    :type robot_id: int

    :rtype: Schedule
    """
    return 'do some magic!'
