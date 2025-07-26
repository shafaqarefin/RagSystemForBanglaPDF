from pathlib import Path
from core.pipeline import RagPipeLine


def main():

    while True:
        query = input("Ask Question to RAG: ")
        if query.lower() == "exit" or query == '':
            break

        answer = RagPipeLine(query)
        print("Answer by RAG:", answer)
    print("-" * 50)


if __name__ == "__main__":
    main()
