from notifiers import NOTIFIERS


def notify(entity_obj, original_entity_obj, entity_type):
    """
    Method that is used
    :param entity_obj:
    :param original_entity_obj:
    :param entity_type:
    :return:
    """
    notifier_class = NOTIFIERS.get(entity_type)
    if notifier_class is None:
        print("No such notifier")
        return
    notifier_class(entity_obj, original_entity_obj).make_notification()
