--
CREATE DATABASE development;

\connect development;

--
CREATE SCHEMA IF NOT EXISTS ons_raw;

CREATE TABLE IF NOT EXISTS ons_raw._datasets
(
	dataset_id VARCHAR,
	dataset_collection_id VARCHAR,
	dataset_title VARCHAR,
	dataset_description VARCHAR,
	dataset_state VARCHAR,
	dataset_release_date VARCHAR,
	dataset_next_release VARCHAR,
	dataset_release_frequency VARCHAR,
	dataset_national_stastic VARCHAR,
	dataset_type VARCHAR,
	dataset_editions_link VARCHAR,
	dataset_latest_version_link VARCHAR,
	dataset_latest_version_id VARCHAR,
	dataset_download_url VARCHAR,
	dataset_self_link VARCHAR,
	dataset_taxonomy_link VARCHAR,
	dataset_quality_methodology_information_link VARCHAR,
	dataset_publications VARCHAR,
	dataset_unit_of_measure VARCHAR,
	dataset_licence VARCHAR,
	dataset_usage_notes VARCHAR
);

CREATE TABLE IF NOT EXISTS ons_raw._dataset_contacts
(
    dataset_id VARCHAR,
    dataset_contact_email VARCHAR,
    dataset_contact_name VARCHAR,
    dataset_contact_telephone VARCHAR
);

CREATE TABLE IF NOT EXISTS ons_raw._dataset_keywords
(
    dataset_id VARCHAR,
    dataset_keyword VARCHAR
);

CREATE TABLE IF NOT EXISTS ons_raw._dataset_methodology
(
    dataset_id VARCHAR,
    dataset_methodology_url VARCHAR,
    dataset_methodology_title VARCHAR
);

CREATE TABLE IF NOT EXISTS ons_raw._dataset_relations
(
    dataset_id VARCHAR,
	related_dataset_url	VARCHAR,
	related_dataset_title VARCHAR
);

--
CREATE SCHEMA IF NOT EXISTS police_uk_raw;

CREATE TABLE IF NOT EXISTS police_uk_raw.forces
(
    id VARCHAR,
	name VARCHAR,
	description VARCHAR,
	url VARCHAR,
	telephone VARCHAR,
	_created_at VARCHAR
);

CREATE TABLE IF NOT EXISTS police_uk_raw.neighbourhoods
(
    force_id VARCHAR,
	id VARCHAR,
	name VARCHAR,
	description VARCHAR,
	url_force VARCHAR,
	population VARCHAR,
	locations VARCHAR,
	boundary VARCHAR,
	contact_details VARCHAR,
	_created_at VARCHAR
);