from glob import glob
from os import getenv
from os.path import abspath, basename, dirname, exists, join, splitext

from yaml import safe_load

WSP_HOME = join(dirname(abspath(__file__)), "..")
WSP_CONFIG = join(WSP_HOME, "config.yml")
WSP_PROJECTS = join(WSP_HOME, "projects")


class ProjectConfig:
    def __init__(self, name, config_file, root_config):
        self.name = name
        self.root_config = root_config

        with open(config_file) as f:
            self.config = safe_load(f) or {}

        if "root" not in self.config:
            raise Exception(f"{name} project config missing 'root'")

    @property
    def root(self):
        return self.config.get("root")

    @property
    def startup(self):
        return self.config.get("startup", [])

    @property
    def shutdown(self):
        return self.config.get("shutdown", [])

    @property
    def editor(self):
        return self.config.get("editor", self.root_config.editor)


class ProjectNotFound(Exception):
    pass


class Config:
    def __init__(self, config_file=WSP_CONFIG):
        if config_file and exists(config_file):
            with open(config_file) as f:
                self.config = safe_load(f) or {}

        self.projects = {}

        for project in glob(
            join(WSP_PROJECTS, "**", "*.y*ml"), recursive=True
        ):
            name, _ = splitext(basename(project))

            self.projects[name] = ProjectConfig(name, project, self)

    @property
    def home(self):
        return WSP_HOME

    @property
    def editor(self):
        return self.config.get("editor", getenv("EDITOR"))

    def get_project_config(self, name):
        if name not in self.projects:
            raise ProjectNotFound(f"project {name} not found")

        return self.projects[name]


config = Config()
