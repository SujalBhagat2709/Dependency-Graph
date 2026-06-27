from graph_engine import DependencyGraph


class DependencyGraphApp:

    def __init__(self):

        self.graph = DependencyGraph()

    def menu(self):

        while True:

            print("\n")

            print("=" * 40)

            print("       DEPENDENCY GRAPH")

            print("=" * 40)

            print("1. Add Module")

            print("2. View Modules")

            print("3. Show Dependency Graph")

            print("4. Delete Module")

            print("5. Exit")

            choice = input(

                "\nEnter Choice: "

            )

            if choice == "1":

                self.graph.add_module()

            elif choice == "2":

                self.graph.view_modules()

            elif choice == "3":

                self.graph.show_dependencies()

            elif choice == "4":

                self.graph.delete_module()

            elif choice == "5":

                print(

                    "\nThank You!"

                )

                break

            else:

                print(

                    "\nInvalid Choice."

                )


if __name__ == "__main__":

    app = DependencyGraphApp()

    app.menu()