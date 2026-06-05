import matplotlib.pyplot as plt

# Data
periods = ["1100 CE", "1757", "1947", "2021", "2026"]
ranks = [1, 10, 100, 132, 148]

# Create figure
fig, ax = plt.subplots(figsize=(8, 5))

# Vertical bars
bars = ax.bar(periods, ranks)

# Add labels above each bar
for bar, rank in zip(bars, ranks):
    if rank <= 100:
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 3,
            f"Rank ~{rank}",
            ha="center",
            va="bottom",
            fontsize=11,
        )
    else:
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 3,
            f"Rank {rank}",
            ha="center",
            va="bottom",
            fontsize=11,
        )

# Labels and title
ax.set_ylabel("GDP Per Capita Rank (Lower is Better)")
ax.set_title("India's GDP Per Capita Rank Through History\n(Illustrative Milestones)")

# Add some space above tallest bar
ax.set_ylim(0, max(ranks) * 1.15)

plt.tight_layout()
plt.show()
