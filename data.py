documents = [
    # Containers & Images
    "Docker is a containerization platform that packages applications with their dependencies into isolated containers. Containers ensure consistency across development, testing, and production environments, reducing the 'works on my machine' problem.",
    "Docker images are immutable templates used to create containers. Best practices include using lightweight base images, multi-stage builds, and minimizing the number of layers to improve security and performance.",
    # Container Orchestration
    "Kubernetes is a container orchestration system that automates deployment, scaling, and management of containerized applications. It uses concepts such as pods, nodes, services, and deployments to maintain application availability.",
    "Kubernetes ensures high availability through self-healing mechanisms such as restarting failed containers, rescheduling pods, and rolling updates with zero downtime.",
    # CI/CD
    "CI/CD pipelines automate the process of building, testing, and deploying applications. Continuous Integration focuses on frequently merging code and running automated tests, while Continuous Deployment ensures rapid and reliable delivery to production.",
    "Popular CI/CD tools include Jenkins, GitHub Actions, GitLab CI, and CircleCI. Pipelines often include stages such as linting, unit testing, security scanning, container image building, and deployment.",
    # Infrastructure as Code
    "Infrastructure as Code (IaC) allows teams to provision and manage infrastructure using code rather than manual processes. Tools like Terraform and AWS CloudFormation improve repeatability, version control, and disaster recovery.",
    "Terraform uses a declarative configuration language to define infrastructure resources. It maintains a state file to track resource changes and enables teams to safely apply infrastructure updates.",
    # Cloud & Scalability
    "Cloud platforms such as AWS, Azure, and Google Cloud provide scalable infrastructure services including compute, storage, networking, and managed Kubernetes clusters.",
    "Auto-scaling dynamically adjusts resources based on demand, improving performance during traffic spikes while reducing costs during low usage periods.",
    # Monitoring & Logging
    "Monitoring and logging are critical DevOps practices used to observe system health and performance. Metrics, logs, and traces help teams detect issues early and reduce mean time to recovery (MTTR).",
    "Tools like Prometheus, Grafana, and ELK Stack enable real-time monitoring, visualization, and centralized logging for distributed systems.",
    # Security (DevSecOps)
    "DevSecOps integrates security practices into the DevOps lifecycle. Security checks such as vulnerability scanning, secrets management, and least-privilege access are automated within CI/CD pipelines.",
    "Container security includes scanning images for vulnerabilities, signing images, and using runtime security tools to detect suspicious behavior.",
    # APIs & Backend Deployment
    "FastAPI is a modern Python framework designed for building high-performance APIs. It supports asynchronous request handling, automatic OpenAPI documentation, and data validation using Pydantic.",
    "Deploying FastAPI applications typically involves containerization with Docker, orchestration with Kubernetes, and exposure through API gateways or reverse proxies like NGINX.",
    # Data & AI Infrastructure
    "Vector databases such as ChromaDB store high-dimensional embeddings and enable semantic search for AI-powered applications, including recommendation systems and retrieval-augmented generation pipelines.",
    "In AI-driven systems, DevOps engineers manage model deployments, monitoring, and scalability, often referred to as MLOps or AI DevOps.",
]
