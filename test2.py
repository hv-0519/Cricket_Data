import pandas as pd

df = pd.read_csv('deliveries.csv')

with open('deliveries_inserts.sql', 'w', encoding='utf-8') as f:
    insert_prefix = (
        "INSERT INTO deliveries_csv (match_id, inning, batting_team, bowling_team, overs, ball, batsman, non_striker, "
        "bowler, is_super_over, wide_runs, bye_runs, legbye_runs, noball_runs, penalty_runs, batsman_runs, extra_runs, total_runs) VALUES\n"
    )

    def esc_str(val):
        return val.replace("'", "\\'") if isinstance(val, str) else val

    for idx, row in df.iterrows():
        values = [
            'NULL' if pd.isnull(row['match_id']) else int(row['match_id']),
            'NULL' if pd.isnull(row['inning']) else int(row['inning']),
            f"'{esc_str(row['batting_team'])}'" if pd.notnull(row['batting_team']) else 'NULL',
            f"'{esc_str(row['bowling_team'])}'" if pd.notnull(row['bowling_team']) else 'NULL',
            'NULL' if pd.isnull(row['overs']) else int(row['overs']),
            'NULL' if pd.isnull(row['ball']) else int(row['ball']),
            f"'{esc_str(row['batsman'])}'" if pd.notnull(row['batsman']) else 'NULL',
            f"'{esc_str(row['non_striker'])}'" if pd.notnull(row['non_striker']) else 'NULL',
            f"'{esc_str(row['bowler'])}'" if pd.notnull(row['bowler']) else 'NULL',
            'NULL' if pd.isnull(row['is_super_over']) else int(row['is_super_over']),
            'NULL' if pd.isnull(row['wide_runs']) else int(row['wide_runs']),
            'NULL' if pd.isnull(row['bye_runs']) else int(row['bye_runs']),
            'NULL' if pd.isnull(row['legbye_runs']) else int(row['legbye_runs']),
            'NULL' if pd.isnull(row['noball_runs']) else int(row['noball_runs']),
            'NULL' if pd.isnull(row['penalty_runs']) else int(row['penalty_runs']),
            'NULL' if pd.isnull(row['batsman_runs']) else int(row['batsman_runs']),
            'NULL' if pd.isnull(row['extra_runs']) else int(row['extra_runs']),
            'NULL' if pd.isnull(row['total_runs']) else int(row['total_runs']),
        ]

        values_line = "(" + ", ".join(map(str, values)) + ")"

        if idx % 1000 == 0:
            if idx != 0:
                f.write(";\n")
            f.write(insert_prefix)
            f.write(values_line)
        else:
            f.write(",\n" + values_line)

    f.write(";\n")  # End final insert statement

print("Done! Check the 'deliveries_inserts.sql' file.")
