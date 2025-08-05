import pandas as pd

# Read the CSV data
df = pd.read_csv('matches.csv')

# Open output SQL file for writing
with open('matches_inserts.sql', 'w', encoding='utf-8') as f:
    insert_prefix = (
        "INSERT INTO matches_csv (id, season, city, date, team1, team2, toss_winner, toss_decision, result, dl_applied, "
        "winner, win_by_runs, win_by_wickets, player_of_match, venue, umpire1, umpire2) VALUES\n"
    )

    for idx, row in df.iterrows():
        # Format the date to 'yyyy-mm-dd' if not null
        if pd.notnull(row['date']):
            try:
                parsed_date = pd.to_datetime(row['date']).strftime('%Y-%m-%d')
            except Exception:
                parsed_date = 'NULL'
            date_val = f"'{parsed_date}'" if parsed_date != 'NULL' else 'NULL'
        else:
            date_val = 'NULL'

        # Escape single quotes in string fields
        def esc_str(val):
            return val.replace("'", "\\'")

        values = [
            'NULL' if pd.isnull(row['id']) else int(row['id']),
            'NULL' if pd.isnull(row['season']) else int(row['season']),
            f"'{esc_str(row['city'])}'" if pd.notnull(row['city']) else 'NULL',
            date_val,
            f"'{esc_str(row['team1'])}'" if pd.notnull(row['team1']) else 'NULL',
            f"'{esc_str(row['team2'])}'" if pd.notnull(row['team2']) else 'NULL',
            f"'{esc_str(row['toss_winner'])}'" if pd.notnull(row['toss_winner']) else 'NULL',
            f"'{row['toss_decision']}'" if pd.notnull(row['toss_decision']) else 'NULL',
            f"'{row['result']}'" if pd.notnull(row['result']) else 'NULL',
            'NULL' if pd.isnull(row['dl_applied']) else int(row['dl_applied']),
            f"'{esc_str(row['winner'])}'" if pd.notnull(row['winner']) else 'NULL',
            'NULL' if pd.isnull(row['win_by_runs']) else int(row['win_by_runs']),
            'NULL' if pd.isnull(row['win_by_wickets']) else int(row['win_by_wickets']),
            f"'{esc_str(row['player_of_match'])}'" if pd.notnull(row['player_of_match']) else 'NULL',
            f"'{esc_str(row['venue'])}'" if pd.notnull(row['venue']) else 'NULL',
            f"'{esc_str(row['umpire1'])}'" if pd.notnull(row['umpire1']) else 'NULL',
            f"'{esc_str(row['umpire2'])}'" if pd.notnull(row['umpire2']) else 'NULL'
        ]

        values_line = "(" + ', '.join(map(str, values)) + ")"

        # Write insert statement or append to batch of 1000 rows
        if idx % 1000 == 0:
            if idx != 0:
                f.write(";\n")
            f.write(insert_prefix)
            f.write(values_line)
        else:
            f.write(",\n" + values_line)

    f.write(";\n")  # End final insert statement

print("Done! Check the 'matches_inserts.sql' file.")
