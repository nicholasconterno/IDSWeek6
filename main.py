import polars as pl
import seaborn as sns
import matplotlib.pyplot as plt

def load_data(url):
    df = pl.read_csv(url)
    # Skipping the first 31 rows. 
    df = df.slice(31, len(df) - 31)  
    return df


def get_summary_statistics(df):
    return df.describe().to_pandas()

def get_mean(df, column_name):
    return df[column_name].mean()

def get_median(df, column_name):
    return df[column_name].median()

def get_stdev(df, column_name):
    return df[column_name].std()

def plot_histogram_save(df, column_name, filename='histogram.png'):
    # Convert to pandas for plotting using seaborn and matplotlib
    df_pandas = df.to_pandas()
    
    # Using seaborn styles
    sns.set_style("whitegrid")
    
    # Create the histogram
    plt.figure(figsize=(10, 6))  # Set figure size for larger plot
    sns.histplot(df_pandas[column_name], kde=True, color="dodgerblue", bins=20)  # KDE shows density curve
    plt.title(f'Histogram of {column_name}', fontsize=18)
    plt.xlabel(column_name, fontsize=14)
    plt.ylabel('Density', fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    
    # Save the figure
    plt.tight_layout()  # This ensures that the labels don't get cut off
    plt.savefig(filename)
    plt.close()  # Close the figure to free up memory
    return filename


url = 'https://gist.githubusercontent.com/tiangechen/b68782efa49a16edaf07dc2cdaa855ea/raw/0c794a9717f18b094eabab2cd6a6b9a226903577/movies.csv'
df = load_data(url)

# Print summary statistics
print(get_summary_statistics(df))

md = df.to_pandas().to_markdown()

# with open('generated_markdown.md','w') as f:
#     f.write(md)

# Assuming the dataset has a column named 'Rotten Tomatoes %'
print(f"Mean of 'Rotten Tomatoes %': {get_mean(df, 'Rotten Tomatoes %')}")
print(f"Median of 'Rotten Tomatoes %': {get_median(df, 'Rotten Tomatoes %')}")
print(f"Standard Deviation of 'Rotten Tomatoes %': {get_stdev(df, 'Rotten Tomatoes %')}")

# Plotting a histogram for 'Rotten Tomatoes %'
fname = plot_histogram_save(df, 'Rotten Tomatoes %')
