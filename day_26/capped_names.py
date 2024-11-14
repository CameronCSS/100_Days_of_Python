
def main() -> None:
    names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie", "Greg", "Harold"]


    short_names = [name for name in names if len(name) < 5]

    long_names = [name.upper() for name in names if len(name) >= 5]

    print(f"short names: {short_names}")
    print(f"long names: {long_names}")



if __name__ == '__main__':
    main()
