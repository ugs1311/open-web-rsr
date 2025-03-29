# Jenkins Git with SSH Credentials

This document outlines the steps to configure Jenkins to access Git repositories using SSH credentials.

## Prerequisites

*   Jenkins Server running.
*   SSH Agent running on the Jenkins server.
*   Your private SSH key (`~/.ssh/id_rsa` or similar) added to the SSH agent.
*   Your Git repository URL.

## Configuration Steps

1.  **Start the SSH Agent:**
    *   On the Jenkins server, execute: `eval "$(ssh-agent)"`

2.  **Add Your SSH Key:**
    *   Add your private SSH key to the agent: `ssh-add ~/.ssh/id_rsa` (adjust the path if your key is located elsewhere). You'll be prompted for your passphrase.

3.  **Configure Jenkins Git Credentials:**
    *   In Jenkins, go to "Manage Jenkins" -> "Manage Credentials".
    *   Select "System" -> "Global credentials".
    *   Click "Add Credentials".
    *   Choose "SSH Username with private key".
    *   *   **ID:** `github-ssh-key` (or your chosen ID)
    *   *   **Username:** Your GitHub username (or the username for the Git repository).
    *   *   **Private Key:** Enter directly the content of your private key file.
    *   *   **Description:**  "SSH key for GitHub" (or your chosen description).
    *   Click "OK" to save.

4.  **Jenkinsfile Configuration (Example):**

    ```groovy
    pipeline {
       agent any
       stages {
           stage('Checkout') {
               steps {
                   git credentialsId: 'github-ssh-key', url: 'your-git-repository-url'
               }
           }
       }
   }
    ```

    *   Replace `'your-git-repository-url'` with the actual URL of your Git repository.

## Notes

*   Never hardcode your private key directly into your Jenkinsfile.
*   Ensure your private key file has appropriate permissions (chmod 600 ~/.ssh/id_rsa).
*   Consider SSH agent forwarding if running Jenkins on a different machine, but be aware of the security implications.

---

**Created by [Your Name/Organization]**
