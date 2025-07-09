import os
import json
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.OpenAction import OpenAction
from ulauncher.api.shared.action.DoNothingAction import DoNothingAction

class ObsidianVaultExtension(Extension):
    def __init__(self):
            super().__init__()
            self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        path = os.path.expanduser(extension.preferences["obsidian_config"])
        try:
            with open(path, 'r') as file:
                data = json.loads(file.read())
                print(data["vaults"].values())
                items = []
                argument = event.get_argument()
                for (id, vault) in data["vaults"].items():
                    path = vault["path"]
                    name = os.path.basename(path)
                    item = ExtensionResultItem(icon="images/icon.png",
                                               name=name,
                                               description=path,
                                               on_enter=OpenAction(f"obsidian://open?vault={id}"))
                    if event.get_argument() == None or argument.lower() in name.lower():
                        items.append(item)

                if len(items) == 0:
                    items.append(ExtensionResultItem(icon="images/error.png",
                                                     name="Error",
                                                     description="No vaults found!",
                                                     on_enter=DoNothingAction()))
        except IOError as error:
            items = [
                        ExtensionResultItem(icon="images/error.png",
                                            name="Error",
                                            description="Failed to load obsidian.json. Check the plugin configuration settings.",
                                            on_enter=DoNothingAction())
                    ]

        return RenderResultListAction(items)

if __name__ == '__main__':
    ObsidianVaultExtension().run()
