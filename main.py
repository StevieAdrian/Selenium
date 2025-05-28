from tester import BinusmayaTester
from gherkin_tc import gherkin_tc

def main():
    tester = BinusmayaTester()
    for tc in gherkin_tc:
        tester.run_test_case(tc)

if __name__ == "__main__":
    main()
