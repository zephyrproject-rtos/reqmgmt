from strictdoc.api import ProjectConfig


def create_config() -> ProjectConfig:
    config = ProjectConfig(
        project_title="Zephyr Project Requirements",
        include_doc_paths=[
            "/docs/",
        ],
    )
    return config
