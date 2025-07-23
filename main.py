from dotenv import load_dotenv

from app.ui.app import mainUI


def main():
    load_dotenv()
    mainUI()


if __name__ == "__main__":
    main()
