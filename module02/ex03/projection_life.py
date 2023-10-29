from load_csv import load
import matplotlib.pyplot as plt
from matplotlib.ticker import EngFormatter

def convert_to_float(value_str):
    suf = {"k": 1e3, "M": 1e6, "B": 1e9}
    return float(value_str[:-1]) * suf[value_str[-1]]

def main():
    try:
        incom_data = load("../income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        life_data = load("../life_expectancy_years.csv")

        year = 1900
        incom_data1900 = incom_data[[str(year)]]
        life_data1900 = life_data[[str(year)]]

        plt.scatter(incom_data1900.values, life_data1900.values)
        plt.title("1900")
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life Expectancy")
        plt.xscale("log")
        plt.gca().xaxis.set_major_formatter(EngFormatter())
        plt.grid(True)
        plt.savefig("result.png")
        plt.show()
        plt.close()
    except Exception as e:
        print('Error:', e)
        exit(1)


if __name__ == "__main__":
    main()