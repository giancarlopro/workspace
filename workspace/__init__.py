from workspace.commands import OpenCommand


class App:
    def open(self, workspace):
        OpenCommand.run(workspace)

    def cmd(self):
        print("cmd")


app = App()
