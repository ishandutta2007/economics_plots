import matplotlib.pyplot as plt

# Data for India's GDP Rank in PPP terms
# Historical data based on Maddison Project and internal project estimates
periods = ["1100 CE", "1757", "1947", "2021", "2026"]
ranks = [1, 2, 5, 3, 3]

# Create figure with a professional size
fig, ax = plt.subplots(figsize=(10, 6))

# Use a professional color palette (Deep Coral/Terracotta for PPP to distinguish from GDP Per Capita)
bar_color = '#d35400' 
bars = ax.bar(periods, ranks, color=bar_color, alpha=0.85, width=0.6)

# Add labels above each bar with better formatting
for bar, rank in zip(bars, ranks):
    label = f"Rank {rank}"
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 0.1,
        label,
        ha="center",
        va="bottom",
        fontsize=10,
        fontweight='bold',
        color='#e67e22'
    )

# Title and Labels
ax.set_title("India's GDP Rank (PPP) Through History", fontsize=16, fontweight='bold', pad=45)
ax.set_ylabel("Global Rank (Lower is Better)", fontsize=11, labelpad=15)

# Add a subtle subtitle for context
ax.text(0.5, 1.02, "India's relative economic size measured by Purchasing Power Parity", 
        transform=ax.transAxes, ha='center', fontsize=11, color='#666666', style='italic')

# Adjust y-axis - since ranks are small, we can fix the limit or let it breathe
ax.set_ylim(0, max(ranks) + 1)
ax.set_yticks(range(0, max(ranks) + 2))

# Add horizontal grid lines for readability
ax.yaxis.grid(True, linestyle='--', alpha=0.6)
ax.set_axisbelow(True)

# Clean up spines (borders)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_alpha(0.3)
ax.spines['bottom'].set_alpha(0.3)

# Customize ticks for a cleaner look
ax.tick_params(axis='both', which='major', labelsize=10, colors='#2c3e50')

# Add a source/note at the bottom
plt.figtext(0.99, 0.01, "Source: Historical estimates (Maddison Project) & IMF Projections", 
            ha="right", fontsize=8, color='#7f8c8d', style='italic')

plt.tight_layout()
plt.show()
