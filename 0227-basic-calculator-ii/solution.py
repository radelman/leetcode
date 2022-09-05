class Solution:
    def calculate(self, s: str) -> int:
        s += "+"

        current_overall = 0
        last_overall_operator = "+"

        current_term = 1
        last_term_operator = "*"

        current_number = ""

        for c in s:
            if c != " ":
                if c in ["*", "/", "+", "-"]:
                    current_number = int(current_number)

                    if c in ["*", "/"]:
                        if last_term_operator == "*":
                            current_term *= current_number
                        elif last_term_operator == "/":
                            current_term //= current_number

                        last_term_operator = c

                    else:
                        if last_term_operator == "*":
                            current_term *= current_number
                        elif last_term_operator == "/":
                            current_term //= current_number

                        if last_overall_operator == "+":
                            current_overall += current_term
                        elif last_overall_operator == "-":
                            current_overall -= current_term

                        last_overall_operator = c

                        current_term = 1
                        last_term_operator = "*"

                    current_number = ""

                else:
                    current_number += c

        return current_overall

def main() -> None:
    test_cases = [
        "3+2*2",
        " 3/2 ",
        " 3+5 / 2 ",
    ]

    solution = Solution();

    for inputs in test_cases:
        s = inputs

        test = solution.calculate(s)

        print(test)

if __name__ == '__main__':
    main()
