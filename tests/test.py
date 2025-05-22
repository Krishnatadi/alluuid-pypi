from alluuid import (
    generate_uuid1,
    generate_uuid4,
    generate_uuid7,
    generate_nil_uuid,
    generate_guid,
    generate_uuid_for_email,
    validate_uuid_for_email,
    generate_custom_uuid,
    generate_multiple_uuids

)


print("UUIDv1:", generate_uuid1())
print("UUIDv4:", generate_uuid4())
print("UUIDv7:", generate_uuid7())
print("Nil UUID:", generate_nil_uuid())
print("GUID:", generate_guid())
createdEmailUUID = generate_uuid_for_email("user@bank.com")
print("UUID from Email:", createdEmailUUID)
print(validate_uuid_for_email(createdEmailUUID, 'user@bank.com'))
print("Pattern UUID:", generate_custom_uuid("xxxx-xxxx-BANK-yyyy"))
print("Batch UUIDs:", generate_multiple_uuids(4, 5))

