class ColumnNames:
    """
    Golden Copy Column names required for analysis grouped by type
    """

    ESSENTIAL_COLUMNS = [
        "LEI",
        "Entity.LegalName",
        "Entity.LegalName.xmllang",
        "Registration.RegistrationStatus",
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

    LEGAL_ADDRESS_COLUMNS = [
    "Entity.LegalAddress.xmllang",
        "Entity.LegalAddress.FirstAddressLine",
        "Entity.LegalAddress.AddressNumber",
        "Entity.LegalAddress.AddressNumberWithinBuilding",
        "Entity.LegalAddress.MailRouting",
        "Entity.LegalAddress.AdditionalAddressLine.1",
        "Entity.LegalAddress.AdditionalAddressLine.2",
        "Entity.LegalAddress.AdditionalAddressLine.3",
        "Entity.LegalAddress.City",
        "Entity.LegalAddress.Region",
        "Entity.LegalAddress.Country",
        "Entity.LegalAddress.PostalCode",
    ]

    OTHER_NAMES_COLUMNS = [
        "Entity.OtherEntityNames.OtherEntityName.1",
        "Entity.OtherEntityNames.OtherEntityName.1.xmllang",
        "Entity.OtherEntityNames.OtherEntityName.1.type",
        "Entity.OtherEntityNames.OtherEntityName.2",
        "Entity.OtherEntityNames.OtherEntityName.2.xmllang",
        "Entity.OtherEntityNames.OtherEntityName.2.type",
        "Entity.OtherEntityNames.OtherEntityName.3",
        "Entity.OtherEntityNames.OtherEntityName.3.xmllang",
        "Entity.OtherEntityNames.OtherEntityName.3.type",
        "Entity.OtherEntityNames.OtherEntityName.4",
        "Entity.OtherEntityNames.OtherEntityName.4.xmllang",
        "Entity.OtherEntityNames.OtherEntityName.4.type",
        "Entity.OtherEntityNames.OtherEntityName.5",
        "Entity.OtherEntityNames.OtherEntityName.5.xmllang",
        "Entity.OtherEntityNames.OtherEntityName.5.type"
    ]

    TRANSLITERATED_OTHER_NAMES_COLUMNS = [
        "Entity.TransliteratedOtherEntityNames.TransliteratedOtherEntityName.1",
        "Entity.TransliteratedOtherEntityNames.TransliteratedOtherEntityName.1.xmllang",
        "Entity.TransliteratedOtherEntityNames.TransliteratedOtherEntityName.1.type",
        "Entity.TransliteratedOtherEntityNames.TransliteratedOtherEntityName.2",
        "Entity.TransliteratedOtherEntityNames.TransliteratedOtherEntityName.2.xmllang",
        "Entity.TransliteratedOtherEntityNames.TransliteratedOtherEntityName.2.type",
        "Entity.TransliteratedOtherEntityNames.TransliteratedOtherEntityName.3",
        "Entity.TransliteratedOtherEntityNames.TransliteratedOtherEntityName.3.xmllang",
        "Entity.TransliteratedOtherEntityNames.TransliteratedOtherEntityName.3.type",
        "Entity.TransliteratedOtherEntityNames.TransliteratedOtherEntityName.4",
        "Entity.TransliteratedOtherEntityNames.TransliteratedOtherEntityName.4.xmllang",
        "Entity.TransliteratedOtherEntityNames.TransliteratedOtherEntityName.4.type",
        "Entity.TransliteratedOtherEntityNames.TransliteratedOtherEntityName.5",
        "Entity.TransliteratedOtherEntityNames.TransliteratedOtherEntityName.5.xmllang",
        "Entity.TransliteratedOtherEntityNames.TransliteratedOtherEntityName.5.type"
    ]
    
    
    OTHER_ADDRESS_COLUMNS = [
    "Entity.OtherAddresses.OtherAddress.1.xmllang",
        "Entity.OtherAddresses.OtherAddress.1.type",
        "Entity.OtherAddresses.OtherAddress.1.FirstAddressLine",
        "Entity.OtherAddresses.OtherAddress.1.AddressNumber",
        "Entity.OtherAddresses.OtherAddress.1.AddressNumberWithinBuilding",
        "Entity.OtherAddresses.OtherAddress.1.MailRouting",
        "Entity.OtherAddresses.OtherAddress.1.AdditionalAddressLine.1",
        "Entity.OtherAddresses.OtherAddress.1.AdditionalAddressLine.2",
        "Entity.OtherAddresses.OtherAddress.1.AdditionalAddressLine.3",
        "Entity.OtherAddresses.OtherAddress.1.City",
        "Entity.OtherAddresses.OtherAddress.1.Region",
        "Entity.OtherAddresses.OtherAddress.1.Country",
        "Entity.OtherAddresses.OtherAddress.1.PostalCode",
        "Entity.OtherAddresses.OtherAddress.2.xmllang",
        "Entity.OtherAddresses.OtherAddress.2.type",
        "Entity.OtherAddresses.OtherAddress.2.FirstAddressLine",
        "Entity.OtherAddresses.OtherAddress.2.AddressNumber",
        "Entity.OtherAddresses.OtherAddress.2.AddressNumberWithinBuilding",
        "Entity.OtherAddresses.OtherAddress.2.MailRouting",
        "Entity.OtherAddresses.OtherAddress.2.AdditionalAddressLine.1",
        "Entity.OtherAddresses.OtherAddress.2.AdditionalAddressLine.2",
        "Entity.OtherAddresses.OtherAddress.2.AdditionalAddressLine.3",
        "Entity.OtherAddresses.OtherAddress.2.City",
        "Entity.OtherAddresses.OtherAddress.2.Region",
        "Entity.OtherAddresses.OtherAddress.2.Country",
        "Entity.OtherAddresses.OtherAddress.2.PostalCode",
    ]

    TRANSLITERATED_OTHER_ADDRESS_COLUMNS = [
        "Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.1.xmllang",
        "Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.1.type",
        "Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.1.FirstAddressLine",
        "Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.1.AddressNumber",
        "Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.1.AddressNumberWithinBuilding",
        "Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.1.MailRouting",
        "Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.1.AdditionalAddressLine.1",
        "Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.1.AdditionalAddressLine.2",
        "Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.1.AdditionalAddressLine.3",
        "Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.1.City",
        "Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.1.Region",
        "Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.1.Country",
        "Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.1.PostalCode",
        "Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.2.xmllang",
        "Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.2.type",
        "Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.2.FirstAddressLine",
        "Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.2.AddressNumber",
        "Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.2.AddressNumberWithinBuilding",
        "Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.2.MailRouting",
        "Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.2.AdditionalAddressLine.1",
        "Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.2.AdditionalAddressLine.2",
        "Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.2.AdditionalAddressLine.3",
        "Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.2.City",
        "Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.2.Region",
        "Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.2.Country",
        "Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.2.PostalCode",
    ]
