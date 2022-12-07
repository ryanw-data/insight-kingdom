SELECT
dataset_collection_id,
dataset_id,
dataset_title,
dataset_description,
dataset_state,
TO_DATE(dataset_release_date,'YYYY-MM-DD') AS dataset_release_date,
dataset_next_release AS dataset_next_release_original,
CASE WHEN REPLACE(dataset_next_release,' ','') IN ('TBA','TBD','TBC','Tobeannounced','') THEN NULL
	 WHEN SPLIT_PART(dataset_next_release,' ',1) ~ '^\d+(\.\d+)?$' THEN TO_DATE(dataset_next_release,'DD Month YYYY')
	 ELSE TO_DATE('01 ' || dataset_next_release,'DD Month YYYY') END
	 dataset_next_release,
dataset_release_frequency,
dataset_national_stastic AS dataset_national_stastic_original, --need to convert to binary
CASE WHEN dataset_national_stastic IN ('True') THEN 1
     WHEN dataset_national_stastic IN ('False') THEN 0
	 ELSE NULL END dataset_national_stastic,
dataset_type,
dataset_editions_link,
dataset_latest_version_link,
CAST(dataset_latest_version_id AS INT) dataset_latest_version_id,
dataset_download_url,
dataset_self_link,
dataset_taxonomy_link,
dataset_quality_methodology_information_link,
dataset_publications,
dataset_unit_of_measure,
dataset_licence,
dataset_usage_notes
FROM {{ source('ons_raw','_datasets') }}