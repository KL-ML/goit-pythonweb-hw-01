from src.task_one_fabric_pattern import task_one
from src.task_two_solid import task_two
from src.logger_config import Logger

def main():

    while True:
        command = input("Choose task to review: task 1, task 2 or exit) [1 / 2 / exit]: ").strip().lower()

        match command:
            case "1":
                task_one()
            case "2":
                task_two()
            case "exit":
                break
            case _:
                logger = Logger()
                logger.info("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
