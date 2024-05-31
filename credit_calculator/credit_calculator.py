"""project credit calculator

Usage examples:
    Calculate annuity payment:
    python credit_calculator.py --type=annuity --principal=1000000 --periods=60 --interest=10

    Calculate loan principal:
    python credit_calculator.py --type=annuity --payment=8722 --periods=120 --interest=5.6

    Calculate number of payments:
    python credit_calculator.py --type=annuity --principal=500000 --payment=23000 --interest=7.8

    Calculate differentiated payments:
    python credit_calculator.py --type=diff --principal=1000000 --periods=10 --interest=10
"""

import math
import argparse


def calculate_annuity_payment(principal, periods, interest):
    """
    Calculates the annuity payment.

    :param principal: float, principal of the loan
    :param periods: int, periods of the loan
    :param interest: float, annual interest rate
    :return: int, the monthly annuity payment, rounded up.
    """
    i = interest / 12 / 100
    annuity_payment = principal * (i * (1 + i) ** periods) / ((1 + i) ** periods - 1)
    return math.ceil(annuity_payment)


def calculate_loan_principal(annuity_payment, periods, interest):
    """
    Calculates the annuity payment.

    :param annuity_payment: float, calculates the annuity payment.
    :param periods: int, calculates the amount of periods.
    :param interest: float, annual interest rate.
    :return: int, the principal amount of the loan, rounded down.
    """
    i = interest / 12 / 100
    principal = annuity_payment / ((i * (1 + i) ** periods) / ((1 + i) ** periods - 1))
    return math.floor(principal)


def calculate_number_of_payments(principal, annuity_payment, interest):
    """
     Calculate the number of monthly payments needed to repay the loan.

    :param principal: float, the principal amount of the loan.
    :param annuity_payment: float, the monthly annuity payment.
    :param interest: float, the annual interest rate
    :return: int, the number of monthly payments, rounded up.
    """
    i = interest / 12 / 100
    if annuity_payment <= i * principal:
        raise ValueError("The monthly payment is too small to cover the interest!")

    n = math.log(annuity_payment / (annuity_payment - i * principal)) / math.log(1 + i)
    return math.ceil(n)


def calculate_diff_payments(principal, periods, interest):
    """
    Calculate differentiated payments.

    :param principal: float, the principal amount of the loan.
    :param periods: int, calculates the amount of periods.
    :param interest: float, the annual interest rate.
    :return: list of monthly differentiated payments, each rounded up.
    """
    i = interest / 12 / 100
    payments = []
    for m in range(1, periods + 1):
        dm = math.ceil((principal / periods) + i * (principal - (principal * (m - 1) / periods)))
        payments.append(dm)
    return payments


def main():
    """
    The main function to parse arguments and perform calculations.

    """
    parser = argparse.ArgumentParser(description="Credit Calculator")
    parser.add_argument("--type", choices=["annuity", "diff"], required=True,
                        help="Type of payment: 'annuity' or 'diff'")
    parser.add_argument("--principal", type=float, help="The principal amount of the loan")
    parser.add_argument("--payment", type=float, help="The monthly payment amount")
    parser.add_argument("--periods", type=int, help="The number of months needed to repay the loan")
    parser.add_argument("--interest", type=float, required=True, help="The interest rate (without the percentage sign)")

    args = parser.parse_args()

    if args.interest <= 0:
        print("Incorrect parameters")
        return

    if args.type == "diff":
        if args.principal is None or args.periods is None:
            print("Incorrect parameters")
            return
        payments = calculate_diff_payments(args.principal, args.periods, args.interest)
        for month, payment in enumerate(payments, 1):
            print(f"Month {month}: payment is {payment}")
        overpayment = sum(payments) - args.principal
        print(f"Overpayment = {overpayment}")

    elif args.type == "annuity":
        if args.principal and args.periods:
            annuity_payment = calculate_annuity_payment(args.principal, args.periods, args.interest)
            print(f"Your annuity payment = {annuity_payment}!")
            overpayment = annuity_payment * args.periods - args.principal
            print(f"Overpayment = {overpayment}")

        elif args.payment and args.periods:
            principal = calculate_loan_principal(args.payment, args.periods, args.interest)
            print(f"Your loan principal = {principal}!")
            overpayment = args.payment * args.periods - principal
            print(f"Overpayment = {overpayment}")

        elif args.principal and args.payment:
            try:
                periods = calculate_number_of_payments(args.principal, args.payment, args.interest)
                years = periods // 12
                months = periods % 12
                if years > 0:
                    if months > 0:
                        print(f"It will take {years} years and {months} months to repay this loan!")
                    else:
                        print(f"It will take {years} years to repay this loan!")
                else:
                    print(f"It will take {months} months to repay this loan!")
                overpayment = args.payment * periods - args.principal
                print(f"Overpayment = {overpayment}")
            except ValueError as e:
                print(e)
        else:
            print("Incorrect parameters")


if __name__ == "__main__":
    main()
