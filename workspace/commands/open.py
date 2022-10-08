from subprocess import run

from workspace.config import ProjectNotFound, config


class OpenCommand:
    @classmethod
    def run(cls, project):
        try:
            proj_config = config.get_project_config(project)
            cwd = proj_config.root

            list(
                map(lambda x: run(x, shell=True, cwd=cwd), proj_config.startup)
            )

            run([proj_config.editor, proj_config.root], cwd=cwd)
        except ProjectNotFound:
            print(f"Project {project} not found")
            return
