from invoke import task

@task
def run(c):
    """Run the main Python script and clear cache before execution."""
    c.run("find /workspace -type d -name '__pycache__' -exec rm -rf {} +")
    c.run("python ./src/main.py")

@task
def test(c):
    """Run Python tests and clear cache before execution."""
    c.run("find /workspace -type d -name '__pycache__' -exec rm -rf {} +")
    c.run("pytest")

@task
def clear_cache(c):
    """Clear all __pycache__ directories."""
    c.run("find /workspace -type d -name '__pycache__' -exec rm -rf {} +")

@task
def update_pip(c):
    """Update requirements"""
    c.run("pip freeze > requirements.txt")
