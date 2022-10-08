from subprocess import run

from workspace.config import ProjectNotFound, config


class OpenCommand:
    @classmethod
    def run(cls, project):
        try:
            proj_config = config.get_project_config(project)

            run([proj_config.editor, proj_config.root])
        except ProjectNotFound:
            print(f"Project {project} not found")
            return
