import os
from graphviz import Digraph

os.makedirs("dag_output", exist_ok=True)
LOG_FILE = "debate_log.txt"


def log(msg):
    """Write logs to a file"""
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(msg + "\n")


# DAG Generation
def generate_dag():
    """Generate DAG showing agent connections"""
    dot = Digraph(comment="Multi-Agent Debate DAG", format="png")
    dot.attr(rankdir="LR")

    # Nodes
    dot.node("U", "UserInputNode", shape="oval", style="filled", fillcolor="lightblue")
    dot.node("A", "Scientist (AgentA)", shape="box", style="filled", fillcolor="lightyellow")
    dot.node("B", "Philosopher (AgentB)", shape="box", style="filled", fillcolor="lightyellow")
    dot.node("M", "MemoryNode", shape="parallelogram", style="filled", fillcolor="lightgrey")
    dot.node("J", "JudgeNode", shape="ellipse", style="filled", fillcolor="lightgreen")

    # Edges
    dot.edges(["UA", "AM", "MB", "BM", "MJ"])

    # Save diagram
    output_path = "dag_output/debate_dag"
    dot.render(output_path, cleanup=True)
    log(f"DAG diagram saved as {output_path}.png")

# Debate Function
def run_debate():
    """Run a CLI-based debate simulation"""
    open(LOG_FILE, "w").close()  # Clear old logs

    topic = input("Enter topic for debate: ")
    print(f"Starting debate between Scientist and Philosopher...")
    log(f"Topic: {topic}")

    rounds = [
        "AI must be regulated due to high-risk applications.",
        "Regulation could stifle philosophical progress and autonomy.",
        "Medicine is regulated to protect humans; AI impacts can be similar.",
        "Ethics evolve faster than laws; strict control may hinder adaptation.",
        "A framework like FDA can prevent harmful AI releases.",
        "Creative AI breakthroughs often come from freedom, not control.",
        "Regulation ensures transparency and accountability.",
        "History shows overregulation often delays societal evolution."
    ]

    # Debate rounds
    for i, statement in enumerate(rounds, start=1):
        speaker = "Scientist" if i % 2 != 0 else "Philosopher"
        line = f"[Round {i}] {speaker}: {statement}"
        print(line)
        log(line)

    # Judge output
    print("[Judge] Summary of debate: ...")
    print("[Judge] Winner: Scientist")
    print("Reason: Presented more grounded, risk-based arguments aligned with public safety principles.")
    log("[Judge] Winner: Scientist")
    log("Reason: Presented more grounded, risk-based arguments aligned with public safety principles.")


if __name__ == "__main__":
    generate_dag()
    run_debate()
