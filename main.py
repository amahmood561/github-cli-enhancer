import typer
import requests
import subprocess
import os

app = typer.Typer()

def get_github_token():
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        raise typer.Exit("Please set the GITHUB_TOKEN environment variable.")
    return token

# Create Issue
@app.command()
def create_issue(repo: str, title: str, body: str):
    token = get_github_token()
    url = f"https://api.github.com/repos/{repo}/issues"
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"}
    data = {"title": title, "body": body}
    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 201:
        typer.echo("Issue created successfully!")
    else:
        typer.echo(f"Failed to create issue: {response.status_code}, {response.text}")

# Merge PRs with specific label
@app.command()
def merge_ready_prs(repo: str, label: str = "ready-for-merge"):
    token = get_github_token()
    url = f"https://api.github.com/repos/{repo}/pulls"
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        typer.echo(f"Failed to retrieve pull requests: {response.status_code}, {response.text}")
        return

    pulls = response.json()
    for pr in pulls:
        if label in [lbl['name'] for lbl in pr.get('labels', [])]:
            pr_number = pr['number']
            merge_url = f"https://api.github.com/repos/{repo}/pulls/{pr_number}/merge"
            merge_response = requests.put(merge_url, headers=headers)

            if merge_response.status_code == 200:
                typer.echo(f"PR #{pr_number} merged successfully!")
            else:
                typer.echo(f"Failed to merge PR #{pr_number}: {merge_response.status_code}, {merge_response.text}")

# Create a branch with naming convention
@app.command()
def create_branch(issue_number: int, repo: str, base_branch: str = "main"):
    branch_name = f"issue-{issue_number}"
    try:
        subprocess.run(["git", "fetch"], check=True)
        subprocess.run(["git", "checkout", base_branch], check=True)
        subprocess.run(["git", "pull"], check=True)
        subprocess.run(["git", "checkout", "-b", branch_name], check=True)
        typer.echo(f"Branch '{branch_name}' created successfully from '{base_branch}'!")
    except subprocess.CalledProcessError as e:
        typer.echo(f"Failed to create branch: {e}")

# Delete merged branches
@app.command()
def delete_merged_branches(repo: str, base_branch: str = "main"):
    try:
        subprocess.run(["git", "fetch", "--prune"], check=True)
        subprocess.run(["git", "checkout", base_branch], check=True)
        subprocess.run(["git", "pull"], check=True)
        merged_branches = subprocess.check_output(["git", "branch", "--merged"]).decode().splitlines()

        for branch in merged_branches:
            branch = branch.strip()
            if branch not in ["main", base_branch, "develop"]:
                subprocess.run(["git", "branch", "-d", branch], check=True)
                subprocess.run(["git", "push", "origin", "--delete", branch], check=True)
                typer.echo(f"Deleted branch '{branch}' locally and remotely.")
    except subprocess.CalledProcessError as e:
        typer.echo(f"Failed to delete branches: {e}")

# Show GitHub Actions status
@app.command()
def show_actions_status(repo: str):
    token = get_github_token()
    url = f"https://api.github.com/repos/{repo}/actions/runs"
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        typer.echo(f"Failed to retrieve workflow runs: {response.status_code}, {response.text}")
        return

    workflows = response.json().get("workflow_runs", [])
    if not workflows:
        typer.echo("No workflows found.")
        return
    
    for workflow in workflows[:5]:
        typer.echo(f"Workflow: {workflow['name']}, Status: {workflow['status']}, Conclusion: {workflow['conclusion']}")

# Create a release
@app.command()
def create_release(repo: str, tag_name: str, release_name: str, description: str = ""):
    token = get_github_token()
    url = f"https://api.github.com/repos/{repo}/releases"
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"}
    data = {"tag_name": tag_name, "name": release_name, "body": description, "draft": False, "prerelease": False}

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 201:
        typer.echo("Release created successfully!")
    else:
        typer.echo(f"Failed to create release: {response.status_code}, {response.text}")

if __name__ == "__main__":
    app()
