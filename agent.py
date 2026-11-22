from openai_orchestra import Orchestra

# --------------------------------------------------------------
# Orchestra definition – use the exact name you gave in UI
# --------------------------------------------------------------
orchestra = Orchestra(
    name="Basketball Analyst Agent",
    description="Analyzes NBA games, player stats, line‑ups and predicts outcomes.",
    model="gpt-4o-mini"
)

# --------------------------------------------------------------
# Example tools – replace the bodies with real API calls later
# --------------------------------------------------------------
@orchestra.tool
def get_player_stats(player_name: str) -> str:
    """Fetch latest stats for a player (replace with real API)."""
    # Placeholder – plug in your NBA stats API here
    return f"Stats for {player_name}: 27.4 PPG, 7.9 RPG, 5.1 APG"

@orchestra.tool
def get_team_record(team_name: str) -> str:
    """Return the win‑loss record for a team."""
    return f"{team_name} is 42‑20 (W‑L) as of today."

# --------------------------------------------------------------
# Orchestrated flow – the LLM decides which tools to call
# --------------------------------------------------------------
@orchestra.flow
def analyze_game(user_input: str) -> str:
    return orchestra.run(user_input)

# --------------------------------------------------------------
# Public entry‑point used by the HTTP layer
# --------------------------------------------------------------
def handler(user_message: str) -> str:
    return analyze_game(user_message)
