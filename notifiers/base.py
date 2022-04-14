from entities import CRAWLING_STATUSES


class BaseNotifier:
    """
    Base Notifier class. New class should be created for each entity
    """

    def __init__(self, entity_obj, original_entity_obj):
        self.entity_obj = entity_obj
        self.original_entity_obj = original_entity_obj

        self.notify_on = None
        self.conditions = None

    # Condition methods
    def check_if_entity_existence_changed(self):
        return self.entity_obj is None or self.original_entity_obj is None

    def check_is_deleted_status(self):
        return self.entity_obj.is_deleted != self.original_entity_obj.is_deleted

    def check_is_blacklisted_status(self):
        return self.entity_obj.is_blacklisted != self.original_entity_obj.is_blacklisted

    def check_crawling_status(self):
        previous_crawling_status = self.original_entity_obj.crawling_status
        current_crawling_status = self.entity_obj.crawling_status
        return (
                current_crawling_status != previous_crawling_status and
                current_crawling_status in (CRAWLING_STATUSES.TEXT_ANALYZED, CRAWLING_STATUSES.TEXT_UPLOADED)
        )

    def _check_conditions(self):
        """
        Check conditions here, if any of the conditions is true - return true
        :return:
        """
        for condition, kwargs in self.conditions:
            if condition(**kwargs):
                return True
        return False

    def make_notification(self):
        """
        General make notifications method
        :return:
        """
        notification_needed = self._check_conditions()
        if notification_needed:
            print(f"Notify on {self.notify_on}")
        else:
            print("No notification needed")
