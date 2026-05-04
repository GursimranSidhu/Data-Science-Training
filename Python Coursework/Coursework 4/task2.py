import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# 1 Load dataset
def load_dataset(file_path):
    df = pd.read_csv(file_path)
    return df


# Display first 5 rows
def show_first_rows(df):
    return df.head()


# 2 Clean dataset
def clean_dataset(df):

    df = df.drop_duplicates().copy()

    numeric_cols = [
        "Year",
        "Engine Size (L)",
        "Horsepower",
        "Torque (lb-ft)",
        "0-60 MPH Time (seconds)",
        "Price (in USD)"
    ]

    for col in numeric_cols:
        df[col] = df[col].astype(str).str.replace(",", "", regex=False)
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.dropna().copy()

    return df


# 3 Summary statistics
def compute_summary_statistics(df):

    numeric_df = df.select_dtypes(include=[np.number])

    mean = numeric_df.mean()
    median = numeric_df.median()

    mode_df = numeric_df.mode()
    if not mode_df.empty:
        mode = mode_df.iloc[0]
    else:
        mode = pd.Series(index=numeric_df.columns)

    std = numeric_df.std()
    range_val = numeric_df.max() - numeric_df.min()

    stats = pd.DataFrame({
        "Mean": mean,
        "Median": median,
        "Mode": mode,
        "Std Dev": std,
        "Range": range_val
    })

    return stats


# 4 Average price by car make
def average_price_by_make(df):
    return df.groupby("Car Make")["Price (in USD)"].mean()


# 5 Average horsepower by year
def average_hp_by_year(df):
    return df.groupby("Year")["Horsepower"].mean()


# 6 Scatter plot with regression line
def scatter_with_regression(df):

    x = df["Horsepower"]
    y = df["Price (in USD)"]

    coeff = np.polyfit(x, y, 1)
    regression = np.poly1d(coeff)

    plt.scatter(x, y)
    plt.plot(x, regression(x))

    plt.xlabel("Horsepower")
    plt.ylabel("Price (USD)")
    plt.title("Price vs Horsepower")

    plt.show()

    return coeff


# 7 Histogram of 0-60 MPH times
def create_histogram(df):

    data = df["0-60 MPH Time (seconds)"]

    bins = np.arange(data.min(), data.max() + 0.5, 0.5)

    plt.hist(data, bins=bins)

    plt.xlabel("0-60 MPH Time (seconds)")
    plt.ylabel("Frequency")
    plt.title("Histogram of 0-60 MPH Times")

    plt.show()

    return bins


# 8 Filter expensive cars
def filter_expensive_cars(df):

    filtered = df[df["Price (in USD)"] > 500000]

    sorted_df = filtered.sort_values(by="Horsepower", ascending=False)

    return sorted_df


# 9 Export cleaned dataset
def export_dataset(df, filename):

    df.to_csv(filename, index=False)

    return filename



if __name__ == "__main__":

    file_path = "Sport car price.csv"

    df = load_dataset(file_path)

    first_rows = show_first_rows(df)

    cleaned_df = clean_dataset(df)

    summary_stats = compute_summary_statistics(cleaned_df)

    avg_price_make = average_price_by_make(cleaned_df)

    avg_hp_year = average_hp_by_year(cleaned_df)

    regression_coeff = scatter_with_regression(cleaned_df)

    histogram_bins = create_histogram(cleaned_df)

    expensive_cars = filter_expensive_cars(cleaned_df)

    exported_file = export_dataset(cleaned_df, "cleaned_sports_car_prices.csv")


    print("First 5 Rows of Dataset:")
    print(first_rows)

    print("\nSummary Statistics:")
    print(summary_stats)

    print("\nAverage Price by Car Make:")
    print(avg_price_make)

    print("\nAverage Horsepower by Year:")
    print(avg_hp_year)

    print("\nCars with Price > $500000 sorted by Horsepower:")
    print(expensive_cars)

    print("\nCleaned dataset exported to:", exported_file)