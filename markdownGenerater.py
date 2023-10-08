from main import load_data, get_summary_statistics, plot_histogram_save

def main():
    url = 'https://gist.githubusercontent.com/tiangechen/b68782efa49a16edaf07dc2cdaa855ea/raw/0c794a9717f18b094eabab2cd6a6b9a226903577/movies.csv'
    df = load_data(url)

    summary_stats = get_summary_statistics(df)

    histogram_filename = plot_histogram_save(df, 'Rotten Tomatoes %')

    # Create markdown content
    md_content = "# Movie Dataset Summary\n\n"
    md_content += "## Summary Statistics\n"
    md_content += summary_stats.to_markdown() + "\n\n"
    md_content += f"![Histogram of Rotten Tomatoes %]({histogram_filename})\n"

    with open('generated_markdown.md', 'w') as md_file:
        md_file.write(md_content)


if __name__ == "__main__":
    main()