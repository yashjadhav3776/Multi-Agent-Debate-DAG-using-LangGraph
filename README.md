# Multi-Agent-Debate-DAG-using-LangGraph
This project simulates a multi-agent debate system between two AI personas — a Scientist and a Philosopher — on any user-defined topic. The debate is modeled as a Directed Acyclic Graph (DAG), where each node represents a distinct role in the discussion pipeline.
The system runs entirely through a Command-Line Interface (CLI) and demonstrates how structured reasoning, logging, and graph-based workflow design can simulate agent-based debate systems.

## What this program does
- Implements a CLI debate simulation with two persona agents (Scientist vs Philosopher).
- Exactly **8 rounds** (4 per agent), alternating.
- MemoryNode stores transcript and provides per-agent memory views.
- JudgeNode evaluates and decides a winner and logs detailed state.
- All messages, state transitions, and final verdict are logged to `debate_log.txt`.
- Generates a DAG image `dag_output/debate_dag.png` using Graphviz.

## Requirements
1. Python 3.8+ installed and on PATH.
2. Python package: `graphviz` (installed via pip).
3. **Graphviz system binary** installed and on PATH (so the `dot` command is available). Download from: https://graphviz.org/download/

## Install (Windows PowerShell)
```powershell
python -m pip install -r requirements.txt





