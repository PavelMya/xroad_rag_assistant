import os
import re
import requests
from pathlib import Path
from urllib.parse import urlparse
from typing import List

def download_markdown(url: str) -> str:
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def extract_title(md_text: str) -> str:
    match = re.search(r"^#\s*(.+)", md_text, re.MULTILINE)
    if not match:
        return "untitled"
    title = match.group(1)
    title = re.sub(r"<!--.*?-->", "", title)  # Удалить HTML-комментарии
    title = re.sub(r"[^\w\s-]", "", title)    # Удалить запрещённые символы
    title = title.strip().lower().replace(" ", "_").replace("__", "_")
    return title

def extract_section_from_url(url: str) -> str:
    match = re.search(r"/doc/([^/]+)/", url)
    return match.group(1).strip().capitalize() if match else "Other"

def split_by_toc(md_text: str) -> List[tuple[str, str]]:
    pattern = r"^(#{1,6})\s+(.+)"
    matches = list(re.finditer(pattern, md_text, re.MULTILINE))
    parts = []

    for i, match in enumerate(matches):
        title = match.group(2).strip()
        start = match.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(md_text)
        content = md_text[start:end].strip()
        safe_title = re.sub(r"[^\w\- ]", "", title.lower().replace(" ", "_"))
        parts.append((f"{i+1:02d}_{safe_title}.md", content))

    return parts

def save_parts(folder: Path, parts: List[tuple[str, str]]):
    folder.mkdir(parents=True, exist_ok=True)
    for filename, content in parts:
        with open(folder / filename, "w", encoding="utf-8") as f:
            f.write(content)

def process_markdown_url(url: str):
    print(f"🔽 Скачивание: {url}")
    try:
        md_text = download_markdown(url)
    except Exception as e:
        print(f"⚠️ Ошибка: {e}")
        return

    section = extract_section_from_url(url)  # Architecture / DataModels / etc.
    doc_title = extract_title(md_text)       # x-road_security_server_architecture
    base_folder = Path("xroad_documentation") / section / doc_title

    parts = split_by_toc(md_text)

    if parts:
        save_parts(base_folder, parts)
        print(f"✅ Разделено: {len(parts)} файлов в {base_folder}")
    else:
        print("⚠️ Не удалось найти разделы.")

def main():
    urls = [
        # "https://raw.githubusercontent.com/nordic-institute/X-Road/develop/doc/Architecture/arc-cs_x-road_central_server_architecture.md",
        # "https://raw.githubusercontent.com/nordic-institute/X-Road/develop/doc/Architecture/arc-cp_x-road_configuration_proxy_architecture.md",
        # "https://raw.githubusercontent.com/nordic-institute/X-Road/develop/doc/Architecture/arc-ss_x-road_security_server_architecture.md",
        # "https://raw.githubusercontent.com/nordic-institute/X-Road/develop/doc/Architecture/arc-tec_x-road_technologies.md",
        # "https://raw.githubusercontent.com/nordic-institute/X-Road/develop/doc/Architecture/spec-al_x-road_audit_log_events.md",
        # "https://raw.githubusercontent.com/nordic-institute/X-Road/develop/doc/Architecture/arc-g_x-road_arhitecture.md",
        # "https://raw.githubusercontent.com/nordic-institute/X-Road/develop/doc/Architecture/arc-sec_x_road_security_architecture.md",
        # "https://raw.githubusercontent.com/nordic-institute/X-Road/develop/doc/DataModels/dm-cs_x-road_central_server_configuration_data_model.md",
        # "https://raw.githubusercontent.com/nordic-institute/X-Road/develop/doc/DataModels/dm-ml_x-road_message_log_data_model.md",
        # "https://raw.githubusercontent.com/nordic-institute/X-Road/develop/doc/DataModels/dm-ss_x-road_security_server_configuration_data_model.md",
        # "https://raw.githubusercontent.com/nordic-institute/X-Road/develop/doc/Manuals/Utils/ug-autologin_x-road_v6_autologin_user_guide.md",
        # "https://raw.githubusercontent.com/nordic-institute/X-Road/develop/doc/Manuals/LoadBalancing/ig-xlb_x-road_external_load_balancer_installation_guide.md",
        # "https://raw.githubusercontent.com/nordic-institute/X-Road/develop/doc/Manuals/ig-cs_x-road_6_central_server_installation_guide.md",
        # "https://raw.githubusercontent.com/nordic-institute/X-Road/develop/doc/Manuals/ig-csha_x-road_6_ha_installation_guide.md",
        # "https://raw.githubusercontent.com/nordic-institute/X-Road/develop/doc/Manuals/ig-ss_x-road_v6_security_server_installation_guide.md",
        # "https://raw.githubusercontent.com/nordic-institute/X-Road/develop/doc/Manuals/ig-ss_x-road_v6_security_server_installation_guide_for_rhel.md",
        # "https://raw.githubusercontent.com/nordic-institute/X-Road/develop/doc/Manuals/ig-ss_x-road_v6_security_server_installation_guide_for_rhel7.md",
        # "https://raw.githubusercontent.com/nordic-institute/X-Road/develop/doc/Manuals/ug-cp_x-road_v6_configuration_proxy_manual.md",
        # "https://raw.githubusercontent.com/nordic-institute/X-Road/develop/doc/Manuals/ug-cs_x-road_6_central_server_user_guide.md",
        # "https://raw.githubusercontent.com/nordic-institute/X-Road/develop/doc/Manuals/ug-sc_x-road_signer-console_user_guide.md",
        # "https://raw.githubusercontent.com/nordic-institute/X-Road/develop/doc/Manuals/ug-sec_x_road_security_hardening.md",
        # "https://raw.githubusercontent.com/nordic-institute/X-Road/develop/doc/Manuals/ug-sigdoc_x-road_signed_document_download_and_verification_manual.md",
        # "https://raw.githubusercontent.com/nordic-institute/X-Road/develop/doc/Manuals/ug-ss_x-road_6_security_server_user_guide.md",
        # "https://raw.githubusercontent.com/nordic-institute/X-Road/develop/doc/Manuals/ug-syspar_x-road_v6_system_parameters.md",
        # "https://raw.githubusercontent.com/nordic-institute/X-Road/develop/doc/UseCases/uc-cp_x-road_configuration_proxy_use_case_model_1.2_Y-883-5.md",
        # "https://raw.githubusercontent.com/nordic-institute/X-Road/develop/doc/UseCases/uc-cs_x-road_use_case_model_for_central_server_management_1.2_Y-883-6.md",
        # "https://raw.githubusercontent.com/nordic-institute/X-Road/develop/doc/UseCases/uc-fed_x-road_use_case_model_for_federation_1.1_Y-883-7.md",
        # "https://raw.githubusercontent.com/nordic-institute/X-Road/develop/doc/UseCases/uc-gconf_x-road_use_case_model_for_global_configuration_distribution_1.4_Y-883-8.md",
        # "https://raw.githubusercontent.com/nordic-institute/X-Road/develop/doc/UseCases/uc-member_x-road_use_case_model_for_member_management.md",
        # "https://raw.githubusercontent.com/nordic-institute/X-Road/develop/doc/UseCases/uc-mess_x-road_member_communication_use_case_model.md",
        # "https://raw.githubusercontent.com/nordic-institute/X-Road/develop/doc/UseCases/uc-service_x-road_use_case_model_for_service_management_1.6_Y-883-3.md",
        # "https://raw.githubusercontent.com/nordic-institute/X-Road/develop/doc/UseCases/uc-ss_x-road_use_case_model_for_security_server_management_1.4_Y-883-4.md",
        # "https://raw.githubusercontent.com/nordic-institute/X-Road/develop/doc/UseCases/uc-trust_x-road_use_case_model_for_trust_service_management_1.1.1_Y-883-9.md",
        # "https://raw.githubusercontent.com/nordic-institute/X-Road/develop/doc/terms_x-road_docs.md",
        # "https://raw.githubusercontent.com/nordic-institute/X-Road/develop/doc/Protocols/pr-gconf_x-road_protocol_for_downloading_configuration.md",
        # "https://raw.githubusercontent.com/nordic-institute/X-Road/develop/doc/Protocols/pr-mess_x-road_message_protocol.md",
        # "https://raw.githubusercontent.com/nordic-institute/X-Road/develop/doc/Protocols/pr-messtransp_x-road_message_transport_protocol.md",
        # "https://raw.githubusercontent.com/nordic-institute/X-Road/develop/doc/Protocols/pr-meta_x-road_service_metadata_protocol.md",
        # "https://raw.githubusercontent.com/nordic-institute/X-Road/develop/doc/Protocols/pr-mrest_x-road_service_metadata_protocol_for_rest.md",
        # "https://raw.githubusercontent.com/nordic-institute/X-Road/develop/doc/Protocols/pr-mserv_x-road_protocol_for_management_services.md",
        # "https://raw.githubusercontent.com/nordic-institute/X-Road/develop/doc/Protocols/pr-rest_x-road_message_protocol_for_rest.md",
        # "https://raw.githubusercontent.com/nordic-institute/X-Road/develop/doc/Protocols/ThirdPartyRepresentationExtension/pr-third_party_representation_extension_for_the_x-road_protocol.md",
        # "https://raw.githubusercontent.com/nordic-institute/X-Road/develop/doc/Protocols/SecurityTokenExtension/pr-sectoken_security_token_extension_for_the_x-road_protocol.md",
        # "https://raw.githubusercontent.com/nordic-institute/X-Road/develop/doc/Protocols/SecurityServerExtension/pr-targetss_security_server_targeting_extension_for_the_x-road_protocol.md",
        "https://raw.githubusercontent.com/nordic-institute/X-Road/develop/doc/OperationalMonitoring/Testing/test-opmon_x-road_operational_monitoring_testing_plan_Y-1104-2.md",
        "https://raw.githubusercontent.com/nordic-institute/X-Road/develop/doc/OperationalMonitoring/Testing/test-opmonstrat_x-road_operational_monitoring_testing_strategy_Y-1104-1.md"
    ]
    for url in urls:
        process_markdown_url(url)

if __name__ == "__main__":
    main()