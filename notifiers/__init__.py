from notifiers.event import EventNotifier
from notifiers.company import CompanyNotifier
from notifiers.company_competitor import CompanyCompetitorNotifier
from notifiers.company_for_event import CompanyForEventNotifier
from notifiers.company_for_webinar import CompanyForWebinarNotifier
from notifiers.content_item import ContentNotifier
from notifiers.webinar import WebinarNotifier

# If new Entity is added then add it here
NOTIFIERS = {
    "Event": EventNotifier,
    "Company": CompanyNotifier,
    "Webinar": WebinarNotifier,
    "ContentItem": ContentNotifier,
    "CompanyForEvent": CompanyForEventNotifier,
    "CompanyForWebinar": CompanyForWebinarNotifier,
    "CompanyCompetitor": CompanyCompetitorNotifier
}