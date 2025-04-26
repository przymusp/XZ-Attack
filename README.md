# Wolves in the Repository: A Software Engineering Analysis of the XZ Utils Supply Chain Attack

[Publication](https://arxiv.org/abs/2504.17473)

## Citation

If you find this work useful, please cite:

**Przymus, P., & Durieux, T.** (2025).  
*Wolves in the Repository: A Software Engineering Analysis of the XZ Utils Supply Chain Attack*.  
Presented at the [MSR 2025 Conference](https://2025.msrconf.org/details/msr-2025-technical-papers/30/Wolves-in-the-Repository-A-Software-Engineering-Analysis-of-the-XZ-Utils-Supply-Chai).  
Available on [arXiv:2504.17473](https://arxiv.org/abs/2504.17473).

## Abstract: 
Open Source Software (OSS) has become a cornerstone of modern software development, offering numerous benefits but also introducing unique vulnerabilities. This paper examines a critical security incident involving the XZ Utils project (CVE-2024-3094), where malicious actors exploited the open-source model to inject a backdoor into a widely-used compression library. Through a comprehensive analysis of the attack timeline, we investigate the software engineering practices employed by the attackers, their evolution over time, and the automated tools utilized in the process. Our study reveals how seemingly beneficial contributions to project management and development infrastructure were leveraged to establish credibility and maintain long-term control. We present a detailed dataset of attacker activities, compare them with legitimate contributor patterns, and identify key red flags that could signal similar attacks in other OSS projects. The findings highlight the need for enhanced vigilance in OSS maintenance, particularly for projects with high impact but low contributor engagement. We conclude by proposing guidelines for improving OSS security and sustainability, emphasizing the importance of community oversight, automated security checks, and support for critical yet under-resourced projects.

## Dataset structure

* affected_commits/ - annotated commits of attacker (including other repositories)
* affected_repositories/ - all repositories that attacker commited to
* data_repositories/
    * data_repositories/emails/ - author emails gathered from affected repositories
    * data_repositories/events/ - Github events with reference to attacker or main author
    * data_repositories/jiat75-logs/ - logs concerning attacker
    * data_repositories/mailing-lists/ - mailing list communication
    * data_repositories/project/ - all Github events connected to xz project
    * data_repositories/(*.log|*.csv) - preprocessed data from this directory
* notebooks/ - notebbok analysing diffrent aspects of this study
* scripts - scripts and notebooks for extracting and visualising data
