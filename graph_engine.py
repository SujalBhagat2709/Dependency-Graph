import json
import os


class DependencyGraph:

    def __init__(self):

        self.file_name = "dependencies.json"

        self.graph = {}

        self.load_graph()

    def load_graph(self):

        if os.path.exists(self.file_name):

            try:

                with open(

                    self.file_name,

                    "r",

                    encoding="utf-8"

                ) as file:

                    self.graph = json.load(file)

            except:

                self.graph = {}

    def save_graph(self):

        with open(

            self.file_name,

            "w",

            encoding="utf-8"

        ) as file:

            json.dump(

                self.graph,

                file,

                indent=4

            )

    def add_module(self):

        print("\nAdd New Module\n")

        module = input(

            "Module Name: "

        ).strip()

        if module == "":

            print("\nInvalid Name")

            return

        dependencies = []

        print(

            "\nEnter Dependencies"

        )

        print(

            "Type 'done' to finish.\n"

        )

        while True:

            dependency = input(

                f"Dependency {len(dependencies)+1}: "

            ).strip()

            if dependency.lower() == "done":

                break

            if dependency != "":

                dependencies.append(

                    dependency

                )

        self.graph[module] = dependencies

        self.save_graph()

        print(

            "\nModule Saved Successfully."

        )

    def view_modules(self):

        if not self.graph:

            print(

                "\nNo Modules Found."

            )

            return

        print("\nModules\n")

        for module in self.graph:

            print(

                f"- {module}"

            )

    def show_dependencies(self):

        if not self.graph:

            print(

                "\nNo Modules Found."

            )

            return

        module = input(

            "\nEnter Module Name: "

        ).strip()

        if module not in self.graph:

            print(

                "\nModule Not Found."

            )

            return

        print(

            f"\nDependency Graph for {module}\n"

        )

        print(module)

        dependencies = self.graph[module]

        if len(dependencies) == 0:

            print("└── No Dependencies")

            return

        for dependency in dependencies:

            print(

                f"└── {dependency}"

            )

    def delete_module(self):

        if not self.graph:

            print(

                "\nNo Modules Available."

            )

            return

        module = input(

            "\nModule Name: "

        ).strip()

        if module in self.graph:

            del self.graph[module]

            self.save_graph()

            print(

                "\nModule Deleted."

            )

        else:

            print(

                "\nModule Not Found."

            )