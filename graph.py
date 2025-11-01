# graph.py
from graphviz import Digraph
import os
from logger import log_state

def generate_dag(outpath: str = "debate_dag.png"):
    """
    Create a simple DAG diagram and save as PNG to the project root.
    Requires Graphviz system binary available on PATH.
    """
    os.makedirs("dag_output", exist_ok=True)
    dot = Digraph(comment="Multi-Agent Debate DAG")
    dot.attr(rankdir="LR")

    dot.node("U", "UserInputNode")
    dot.node("A", "AgentA (Scientist)")
    dot.node("B", "AgentB (Philosopher)")
    dot.node("M", "MemoryNode")
    dot.node("J", "JudgeNode")

    dot.edge("U", "A")
    dot.edge("U", "B")
    dot.edge("A", "M")
    dot.edge("B", "M")
    dot.edge("M", "A")
    dot.edge("M", "B")
    dot.edge("A", "J")
    dot.edge("B", "J")
    dot.edge("M", "J")

    filename = dot.render("dag_output/debate_dag", format="png", cleanup=True)
    # filename is like dag_output/debate_dag.png
    log_state("DAGGenerated", {"file": filename})
    return filename
