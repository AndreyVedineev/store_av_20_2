BEGIN;
SELECT setval(pg_get_serial_sequence('"catalog_category"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "catalog_category";
SELECT setval(pg_get_serial_sequence('"catalog"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "catalog";
COMMIT;
