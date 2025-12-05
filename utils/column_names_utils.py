class ColumnNames:
    """
    Golden Copy Column names required for analysis grouped by type
    """

    ESSENTIAL_COLUMNS = [
        "LEI",
        "Entity.LegalName",
        "Registration.RegistrationStatus"
    ]

    REGISTRATION_COLUMNS = [
        "Registration.InitialRegistrationDate",
        "Registration.ManagingLOU",
        "Registration.NextRenewalDate",
        "Registration.LastUpdateDate"   
    ]

    EVENT_COLUMNS = [
        "Entity.LegalEntityEvents.LegalEntityEvent.1.LegalEntityEventType",
        "Entity.LegalEntityEvents.LegalEntityEvent.1.event_status",
        "Entity.LegalEntityEvents.LegalEntityEvent.1.LegalEntityEventEffectiveDate",
        "Entity.LegalEntityEvents.LegalEntityEvent.1.LegalEntityEventRecordedDate",
        "Entity.LegalEntityEvents.LegalEntityEvent.2.LegalEntityEventType",
        "Entity.LegalEntityEvents.LegalEntityEvent.2.event_status",
        "Entity.LegalEntityEvents.LegalEntityEvent.2.LegalEntityEventEffectiveDate",
        "Entity.LegalEntityEvents.LegalEntityEvent.2.LegalEntityEventRecordedDate",
        "Entity.LegalEntityEvents.LegalEntityEvent.3.LegalEntityEventType",
        "Entity.LegalEntityEvents.LegalEntityEvent.3.event_status",
        "Entity.LegalEntityEvents.LegalEntityEvent.3.LegalEntityEventEffectiveDate",
        "Entity.LegalEntityEvents.LegalEntityEvent.3.LegalEntityEventRecordedDate",
        "Entity.LegalEntityEvents.LegalEntityEvent.4.LegalEntityEventType",
        "Entity.LegalEntityEvents.LegalEntityEvent.4.event_status",
        "Entity.LegalEntityEvents.LegalEntityEvent.4.LegalEntityEventEffectiveDate",
        "Entity.LegalEntityEvents.LegalEntityEvent.4.LegalEntityEventRecordedDate",
        "Entity.LegalEntityEvents.LegalEntityEvent.5.LegalEntityEventType",
        "Entity.LegalEntityEvents.LegalEntityEvent.5.event_status",
        "Entity.LegalEntityEvents.LegalEntityEvent.5.LegalEntityEventEffectiveDate",
        "Entity.LegalEntityEvents.LegalEntityEvent.5.LegalEntityEventRecordedDate",
    ]

    SUCCESSOR_COLUMNS = [
        "Entity.SuccessorEntity.1.SuccessorEntityName",
        "Entity.SuccessorEntity.1.SuccessorLEI",
        "Entity.SuccessorEntity.2.SuccessorEntityName",
        "Entity.SuccessorEntity.2.SuccessorLEI",
        "Entity.SuccessorEntity.3.SuccessorEntityName",
        "Entity.SuccessorEntity.3.SuccessorLEI",
        "Entity.SuccessorEntity.4.SuccessorEntityName",
        "Entity.SuccessorEntity.4.SuccessorLEI",
        "Entity.SuccessorEntity.5.SuccessorEntityName",
        "Entity.SuccessorEntity.5.SuccessorLEI",
    ]

