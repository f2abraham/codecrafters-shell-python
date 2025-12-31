import sys


def main():
        sys.stdout.write("$ ")
        command = input().strip()
        sys.stdout.write(f"{command}: command not found" + "\n")
        main()

if __name__ == "__main__":
    main()




