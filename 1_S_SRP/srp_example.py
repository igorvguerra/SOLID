class Process:
    def handle(self, username: str, password: str) -> None:
        if self.__verify_input_data(username, password):
            self.__verify_input_in_database(username)
        else:
            self.__raise_error("Invalid data")
    
    def __verify_input_data(self, username: str, password: str) -> bool:
        return isinstance(username, str) and isinstance(password, str)

    def __verify_input_in_database(self, username: str) -> None:
        print("Acessing the database...")
        print("Verifying username...")

    def insert_new_user(self, username: str, password: str) -> None:
        print("User was sucessfully added!")

    def __raise_error(self, message: str) -> Exception:
        raise Exception(message)