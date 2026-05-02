from mcp.server.fastmcp import FastMCP
import json
import os

mcp = FastMCP("task-manager")

FILE_NAME = "tasks.json"

# Load tasks
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save tasks
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


# ➤ MCP TOOL: Add Task
@mcp.tool()
def add_task(title: str):
    tasks = load_tasks()

    priority = "High" if "urgent" in title.lower() else "Normal"

    new_task = {
        "task": title,
        "priority": priority
    }

    tasks.append(new_task)
    save_tasks(tasks)

    return f"Added: {title} ({priority})"


# ➤ MCP TOOL: Get Tasks
@mcp.tool()
def list_tasks():
    return load_tasks()


# ➤ MCP RESOURCE
@mcp.resource("tasks://all")
def get_tasks():
    return load_tasks()


# ➤ MCP TOOL: Suggest Task
@mcp.tool()
def suggest_task():
    tasks = load_tasks()

    if not tasks:
        return "No tasks available"

    for t in tasks:
        if t["priority"] == "High":
            return f"Do this first: {t['task']}"

    return f"Start with: {tasks[0]['task']}"


# ➤ MCP TOOL: Delete Task
@mcp.tool()
def delete_task(index: int):
    tasks = load_tasks()

    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        save_tasks(tasks)
        return f"Deleted: {removed['task']}"

    return "Invalid index"


if __name__ == "__main__":
    mcp.run()