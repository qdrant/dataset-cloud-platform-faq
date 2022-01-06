import os
import requests


if not os.path.exists("../../data/raw/azure/faq"):
    os.mkdir("../../data/raw/azure/faq")

links_required = [
"azure_active_directory_domain_services_synchronization",
"azure_mysql_single_server_overview",
"azure_sphere_product_overview_whats_new",
"azure_storsimple_storsimple_data_manager_overview",
"azure_cognitive_services_anomaly_detector_whats_new",
"azure_site_recovery_site_recovery_overview",
"azure_devops_artifacts_concepts_symbols_view_azure_devops",
"azure_azure_sql_virtual_machines_windows_doc_changes_updates_release_notes_whats_new",
"azure_logic_apps_azure_arc_enabled_logic_apps_overview",
"azure_frontdoor_front_door_rules_engine",
"azure_azure_app_configuration_concept_feature_management",
"azure_azure_sql_database_elastic_pool_overview",
"azure_spatial_anchors_overview",
"azure_cognitive_services_personalizer_where_can_you_use_personalizer",
"azure_rtos_guix_overview_guix",
"azure_analysis_services_analysis_services_overview",
"azure_cloud_services_extended_support_overview",
"azure_automation_overview",
"azure_azure_functions_functions_overview",
"azure_hdinsight_kafka_apache_kafka_introduction",
"azure_rtos_threadx_overview_threadx",
"azure_azure_resource_manager_managed_applications_overview",
"azure_rtos_filex_overview_filex",
"azure_postgresql_hyperscale_concepts_nodes",
"azure_iot_hub_about_iot_hub",
"azure_active_directory_external_identities_self_service_sign_up_overview",
"azure_azure_netapp_files_whats_new",
"azure_app_service_overview",
"azure_kinect_dk_about_azure_kinect_dk",
"azure_aks_intro_kubernetes",
"azure_rtos_levelx_chapter1",
"azure_migrate_migrate_services_overview",
"azure_rtos_usbx_overview_usbx",
"azure_migrate_whats_new",
"azure_active_directory_authentication_overview_authentication",
"azure_api_management_api_management_key_concepts",
"azure_active_directory_identity_protection_overview_identity_protection",
"azure_applied_ai_services_metrics_advisor_overview",
"azure_applied_ai_services_form_recognizer_whats_new",
"azure_object_anchors_overview",
"azure_mysql_flexible_server_overview",
"azure_container_registry_container_registry_intro",
"azure_expressroute_expressroute_global_reach",
"azure_rtos_netx_duo_overview_netx_duo",
"azure_postgresql_flexible_server_overview",
"azure_sentinel_whats_new",
"azure_cosmos_db_change_feed",
"azure_rtos_tracex_overview_tracex",
"azure_azure_monitor_overview",
"azure_search_search_indexer_overview",
"azure_azure_sql_virtual_machines_linux_sql_server_on_linux_vm_what_is_iaas_overview",
"azure_hdinsight_interactive_query_apache_interactive_query_get_started",
"azure_cognitive_services_anomaly_detector_overview_multivariate",
"azure_cognitive_services_luis_whats_new",
"azure_frontdoor_front_door_geo_filtering",
"azure_azure_cache_for_redis_cache_overview",
"azure_healthcare_apis_azure_api_for_fhir_overview_azure_iot_connector_for_fhir_preview",
"azure_azure_maps_about_azure_maps",
"azure_media_services_latest_release_notes",
"azure_cosmos_db_introduction",
"azure_search_cognitive_search_concept_intro",
"azure_stack_hci_whats_new",
"azure_cognitive_services_cognitive_services_container_support",
"azure_container_apps_overview",
"azure_defender_for_cloud_security_center_os_coverage",
"azure_expressroute_expressroute_erdirect_about",
"azure_logic_apps_connect_virtual_network_vnet_isolated_environment_overview",
"azure_stack_operator____hci_overview_view_azs_2108",
"azure_data_lake_analytics_data_lake_analytics_whats_new",
"azure_defender_for_cloud_get_started",
"azure_cosmos_db_graph_graph_introduction",
"azure_time_series_insights_overview_what_is_tsi",
"azure_service_bus_messaging_service_bus_messaging_overview",
"azure_azure_monitor_logs_data_platform_logs",
"azure_cognitive_services_translator_translator_overview",
"azure_cosmos_db_mongodb_mongodb_introduction",
"azure_azure_video_analyzer_video_analyzer_for_media_docs_release_notes",
"azure_azure_netapp_files_azure_netapp_files_introduction",
"azure_healthcare_apis_azure_api_for_fhir_overview",
"azure_postgresql_overview",
"azure_event_hubs_event_hubs_capture_overview",
"azure_rtos_netx_overview_netx",
"azure_remote_rendering_overview_about",
"azure_stack_hci_overview",
]

with open("../../data/raw/azure/azure_article_links.txt", "r") as fd:
    link = fd.readline().strip()
    while link:
        if 'azure' not in link:
            link = fd.readline().strip()
            continue
        page = requests.get(link)
        truncated_link = (
            link.replace("https://docs.microsoft.com/en-us/", "")
            .replace("/", "_")
        )
        if truncated_link[-1] == "_":
            truncated_link = truncated_link[:-1]
        normalized_link = "".join(x if x.isalnum() else '_' for x in truncated_link)
        # print(normalized_link)
        if normalized_link in links_required:
            print(link)
        # with open(
        #     "../../data/raw/azure/faq/" + normalized_link + ".html", "w"
        # ) as n_fd:
        #     n_fd.write(page.text)
        link = fd.readline().strip()
