# GitHub CLI Enhancer

[![GitHub license](https://img.shields.io/github/license/yourusername/github-cli-enhancer)](https://github.com/yourusername/github-cli-enhancer/blob/main/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/yourusername/github-cli-enhancer)](https://github.com/yourusername/github-cli-enhancer/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/yourusername/github-cli-enhancer)](https://github.com/yourusername/github-cli-enhancer/network)
[![GitHub issues](https://img.shields.io/github/issues/yourusername/github-cli-enhancer)](https://github.com/yourusername/github-cli-enhancer/issues)

A Python command-line tool that simplifies and automates common GitHub workflows. GitHub CLI Enhancer aims to save developers time by streamlining tasks such as creating issues, managing pull requests, and interacting with GitHub Actions—all from the command line.

## Features

- **Create Issues**: Easily create new issues in any GitHub repository.
- **Merge PRs Automatically**: Merge pull requests with a specified label (e.g., `ready-for-merge`).
- **Branch Management**: Create branches with naming conventions (e.g., issue numbers), and clean up merged branches.
- **GitHub Actions Status**: View the most recent workflow run status in a repository.
- **Create Releases**: Automatically create a GitHub release based on pull requests.
- **Delete Merged Branches**: Clean up local and remote branches that have already been merged.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/github-cli-enhancer.git
   ```

2. Navigate to the project directory:
   ```bash
   cd github-cli-enhancer
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your GitHub Personal Access Token:
   You need to generate a [GitHub Personal Access Token](https://github.com/settings/tokens) and store it in an environment variable `GITHUB_TOKEN`:
   ```bash
   export GITHUB_TOKEN=<your-github-token>
   ```

## Usage

After installation, you can use the tool to manage your GitHub repository with the following commands:

### Create an Issue

```bash
python github_cli.py create-issue --repo username/repo --title "Issue Title" --body "Issue description"
```

### Merge Pull Requests with a Specific Label

```bash
python github_cli.py merge-ready-prs --repo username/repo --label "ready-for-merge"
```

### Create a Branch Based on an Issue Number

```bash
python github_cli.py create-branch --repo username/repo --issue-number 123 --base-branch main
```

### Delete Merged Branches

```bash
python github_cli.py delete-merged-branches --repo username/repo --base-branch main
```

### Show GitHub Actions Workflow Status

```bash
python github_cli.py show-actions-status --repo username/repo
```

### Create a Release

```bash
python github_cli.py create-release --repo username/repo --tag-name v1.0.0 --release-name "First Release" --description "Description of the release"
```

## Example Workflow

You can create an issue, work on a branch named after that issue, open a pull request, and merge it—entirely from the command line using this tool:

1. **Create an issue**:
   ```bash
   python github_cli.py create-issue --repo username/repo --title "New Feature" --body "Description of the new feature"
   ```

2. **Create a branch based on the issue**:
   ```bash
   python github_cli.py create-branch --repo username/repo --issue-number 123 --base-branch main
   ```

3. **Work on your code, then push the branch**:
   ```bash
   git push origin issue-123
   ```

4. **Open a pull request and apply a label like `ready-for-merge`**.

5. **Merge the pull request**:
   ```bash
   python github_cli.py merge-ready-prs --repo username/repo --label "ready-for-merge"
   ```

6. **Delete the merged branch**:
   ```bash
   python github_cli.py delete-merged-branches --repo username/repo --base-branch main
   ```

## Contributing

Contributions are welcome! Please check the [issues](https://github.com/yourusername/github-cli-enhancer/issues) tab for feature requests and bug reports. If you'd like to contribute:

1. Fork the project.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Open a pull request.


