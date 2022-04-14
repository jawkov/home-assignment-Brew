# Test file. Ideally all entities should be covered

import copy
import datetime

from entities import Event, Company, Webinar, CompanyForWebinar, CRAWLING_STATUSES
from main import notify

COMPANY_TEST = Company(
    employees_min=1,
    employees_max=100,
    link="link",
    name="name 1"
)

EVENT_TEST = Event(
    start_date=datetime.datetime(2022, 4, 14),
    link="link",
    name="name 1"
)

WEBINAR_TEST = Webinar(
    start_date=datetime.datetime(2022, 4, 14),
    link="link",
    name="name 1"
)

COMPANY_FOR_WEBINAR_TEST = CompanyForWebinar(
    webinar=WEBINAR_TEST,
    company=COMPANY_TEST
)


def test_no_notifiers():
    print("Test no notifiers")
    entity_obj = copy.deepcopy(COMPANY_TEST)
    original_entity_obj = copy.deepcopy(COMPANY_TEST)
    entity_type = "Sth"

    notify(entity_obj, original_entity_obj, entity_type)
    print("\n")


def test_notify_success(entity_obj, original_entity_obj, entity_type, changed_items, test_name, change_new_entity=True):
    """

    :param entity_obj: new entity
    :param original_entity_obj: original entity
    :param entity_type:
    :param changed_items: attrs to change
    :param test_name:
    :param change_new_entity: flag to show which entity should be change(new by default)
    :return:
    """
    print(test_name)
    for attr, new_value in changed_items:
        setattr(entity_obj, attr, new_value)
        changed_entity = entity_obj if change_new_entity else original_entity_obj
        notify(changed_entity, original_entity_obj, entity_type)

    notify(None, original_entity_obj, entity_type)
    notify(entity_obj, None, entity_type)
    print("\n")


def test_notify_failure(entity_obj, original_entity_obj, entity_type, changed_items, test_name, change_new_entity=True):
    print(test_name)
    for attr, new_value in changed_items:
        setattr(entity_obj, attr, new_value)
        changed_entity = entity_obj if change_new_entity else original_entity_obj
        notify(changed_entity, original_entity_obj, entity_type)

    print("\n")


test_no_notifiers()
test_notify_success(
    entity_obj=copy.deepcopy(COMPANY_TEST),
    original_entity_obj=copy.deepcopy(COMPANY_TEST),
    entity_type="Company",
    changed_items=(
        ("is_deleted", True),
        ("crawling_status", CRAWLING_STATUSES.TEXT_ANALYZED),
    ),
    test_name="Test company notify"
)
test_notify_success(
    entity_obj=copy.deepcopy(EVENT_TEST),
    original_entity_obj=copy.deepcopy(EVENT_TEST),
    entity_type="Event",
    changed_items=(
        ("is_deleted", True),
        ("crawling_status", CRAWLING_STATUSES.TEXT_ANALYZED),
    ),
    test_name="Test event notify",
)
test_notify_success(
    entity_obj=copy.deepcopy(COMPANY_FOR_WEBINAR_TEST),
    original_entity_obj=copy.deepcopy(COMPANY_FOR_WEBINAR_TEST),
    entity_type="CompanyForWebinar",
    changed_items=(
        ("is_deleted", True),
        ("is_blacklisted", True),
    ),
    test_name="Test company for webinar notify"
)

test_notify_failure(
    entity_obj=copy.deepcopy(WEBINAR_TEST),
    original_entity_obj=copy.deepcopy(WEBINAR_TEST),
    entity_type="Webinar",
    changed_items=(
        ("start_date", datetime.datetime(2022, 4, 12)),
        ("crawling_status", CRAWLING_STATUSES.TEXT_ANALYZED),
    ),
    test_name="Test webinar notify failed",
    change_new_entity=False
)