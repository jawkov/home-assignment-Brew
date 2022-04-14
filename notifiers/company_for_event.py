from typing import Optional
from entities import CompanyForEvent
from notifiers.base import BaseNotifier


class CompanyForEventNotifier(BaseNotifier):

    def __init__(self, entity_obj: Optional[CompanyForEvent], original_entity_obj: Optional[CompanyForEvent]):
        super().__init__(entity_obj, original_entity_obj)

        # Use new entity as a place to notify, if new entity is None then use old entity
        if entity_obj is not None:
            self.notify_on = entity_obj.event
        else:
            self.notify_on = original_entity_obj.event

        # Conditions list, new items could be added, also kwargs could be added if needed
        self.conditions = (
            (self.check_if_entity_existence_changed, {}),
            (self.check_is_deleted_status, {}),
            (self.check_is_blacklisted_status, {}),
        )
