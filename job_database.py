"""
JOB REQUIREMENTS DATABASE
Built from real job postings on:
- careers.google.com
- linkedin.com
- amazon.jobs
- careers.microsoft.com
- openai.com/careers
- nvidia.com/en-us/about-nvidia/careers
- infosys.com/careers
- tcs.com/careers
- wipro.com/careers
- accenture.com/careers
- research on FAANG/top tech company requirements

Companies included:
  Google, Microsoft, Amazon, Meta, Apple, Tesla, Netflix, Adobe, IBM, Intel,
  OpenAI, NVIDIA, Salesforce, Uber, Airbnb,
  Infosys, TCS, Wipro, Accenture, HCL
"""

job_database = {

    # ─────────────────────────────────────────────
    # GOOGLE
    # ─────────────────────────────────────────────
    "Google": {
        "Software Engineer": {
            "must_have": [
                "Data Structures", "Algorithms", "Python", "Java", "C++",
                "System Design", "Distributed Systems", "OOP", "Git", "APIs",
                "Unit Testing", "Code Review", "Problem Solving"
            ],
            "good_to_have": [
                "Go", "Kubernetes", "Large-Scale Systems", "Networking",
                "Natural Language Processing", "Cloud Computing", "Linux"
            ],
            "description": "Build next-gen technologies at scale. Google looks for versatile engineers who can work across the full stack."
        },
        "Frontend Developer": {
            "must_have": [
                "JavaScript", "TypeScript", "HTML", "CSS", "React",
                "Angular", "Performance Optimization", "REST APIs",
                "Responsive Design", "Web Accessibility", "Git"
            ],
            "good_to_have": [
                "Web Components", "GraphQL", "PWA", "Webpack", "Testing (Jest)",
                "UX Principles", "Material Design"
            ],
            "description": "Google expects deep expertise in modern JS frameworks and scalable front-end architecture."
        },
        "Backend Developer": {
            "must_have": [
                "Python", "Java", "Go", "C++", "APIs", "Microservices",
                "Databases", "SQL", "NoSQL", "System Design",
                "Distributed Systems", "Cloud (GCP)", "Security"
            ],
            "good_to_have": [
                "Kafka", "Bigtable", "Spanner", "gRPC", "Kubernetes",
                "Pub/Sub", "Load Balancing"
            ],
            "description": "Build and maintain large-scale backend systems. GCP knowledge is a strong plus."
        },
        "Data Scientist": {
            "must_have": [
                "Python", "R", "Machine Learning", "Statistics",
                "Pandas", "NumPy", "SQL", "BigQuery", "Data Analysis",
                "A/B Testing", "Data Visualization", "Scikit-learn"
            ],
            "good_to_have": [
                "TensorFlow", "Deep Learning", "NLP", "Spark",
                "Looker", "Jupyter", "Experimentation"
            ],
            "description": "Google data scientists work on search, ads, and product analytics at massive scale."
        },
        "Machine Learning Engineer": {
            "must_have": [
                "Python", "TensorFlow", "PyTorch", "Machine Learning",
                "Deep Learning", "NLP", "Model Deployment", "Kubernetes",
                "Data Pipelines", "MLOps", "Statistics", "Scikit-learn"
            ],
            "good_to_have": [
                "Vertex AI", "BigQuery ML", "JAX", "TPU",
                "Transformer Models", "Computer Vision", "RL"
            ],
            "description": "Build and deploy ML models that power Google Search, Ads, Assistant, and more."
        },
        "Site Reliability Engineer": {
            "must_have": [
                "Linux", "Python", "Go", "Kubernetes", "Docker",
                "Monitoring", "Incident Management", "Distributed Systems",
                "Networking", "Automation", "CI/CD", "SLOs/SLAs"
            ],
            "good_to_have": [
                "Terraform", "Prometheus", "Grafana", "Ansible",
                "GCP", "Chaos Engineering", "On-Call Experience"
            ],
            "description": "Ensure reliability of Google's global production systems."
        },
        "Android Developer": {
            "must_have": [
                "Java", "Kotlin", "Android SDK", "Android Studio",
                "REST APIs", "Material Design", "MVVM",
                "Git", "Unit Testing", "UI/UX"
            ],
            "good_to_have": [
                "Jetpack Compose", "Coroutines", "Firebase",
                "Play Store Publishing", "Accessibility"
            ],
            "description": "Build apps used by billions on the world's most popular mobile OS."
        },
        "AI Researcher": {
            "must_have": [
                "Python", "TensorFlow", "PyTorch", "Research Papers",
                "Deep Learning", "NLP", "Computer Vision", "Mathematics",
                "Statistics", "Linear Algebra", "Publications", "PhD preferred"
            ],
            "good_to_have": [
                "JAX", "Transformer Models", "Reinforcement Learning",
                "Generative AI", "LLMs"
            ],
            "description": "Conduct cutting-edge AI research. Publication record and PhD preferred."
        },
        "UI/UX Designer": {
            "must_have": [
                "Figma", "User Research", "Wireframes", "Prototyping",
                "Usability Testing", "Material Design", "Interaction Design",
                "Visual Design", "Design Systems", "Accessibility"
            ],
            "good_to_have": [
                "Motion Design", "User Interviews", "A/B Testing",
                "HTML/CSS basics", "Adobe XD"
            ],
            "description": "Design intuitive interfaces for Google products used by billions."
        },
        "Full Stack Developer": {
            "must_have": [
                "JavaScript", "TypeScript", "React", "Node.js", "Python",
                "SQL", "NoSQL", "REST APIs", "Git", "System Design",
                "HTML", "CSS", "Cloud (GCP)"
            ],
            "good_to_have": [
                "GraphQL", "Docker", "Kubernetes", "Angular",
                "CI/CD", "Testing (Jest/Mocha)", "Redis"
            ],
            "description": "Build end-to-end features across Google products, owning both frontend and backend."
        },
        "DevOps Engineer": {
            "must_have": [
                "Linux", "Python", "Bash", "Docker", "Kubernetes",
                "CI/CD", "Terraform", "GCP", "Monitoring", "Git",
                "Automation", "Networking"
            ],
            "good_to_have": [
                "Ansible", "Prometheus", "Grafana",
                "Spinnaker", "GitHub Actions", "Security Scanning"
            ],
            "description": "Automate and scale Google's engineering infrastructure across GCP."
        },
        "Cloud Engineer": {
            "must_have": [
                "GCP", "Kubernetes", "Docker", "Terraform",
                "Networking", "Security", "Python", "IaC",
                "Monitoring", "CI/CD", "Cloud Architecture"
            ],
            "good_to_have": [
                "BigQuery", "Pub/Sub", "Cloud Run",
                "AWS", "Azure", "Cost Optimization", "Anthos"
            ],
            "description": "Design and manage Google Cloud infrastructure for internal and external customers."
        },
        "Product Manager": {
            "must_have": [
                "Product Roadmap", "Stakeholder Management", "Agile",
                "User Research", "KPIs", "Data Analysis", "PRDs",
                "Competitive Analysis", "Communication", "SQL"
            ],
            "good_to_have": [
                "A/B Testing", "OKRs", "Go-to-Market",
                "Technical Background", "JIRA", "Python basics"
            ],
            "description": "Define product vision for Google Search, Maps, Ads, or Cloud products."
        },
        "Data Analyst": {
            "must_have": [
                "SQL", "BigQuery", "Python", "Data Visualization",
                "Statistics", "Google Sheets", "Looker",
                "A/B Testing", "Business Intelligence", "Reporting"
            ],
            "good_to_have": [
                "Tableau", "R", "Pandas",
                "Data Studio", "ETL", "Spark"
            ],
            "description": "Analyze large datasets to drive decisions across Google's product and business teams."
        }
    },

    # ─────────────────────────────────────────────
    # MICROSOFT
    # ─────────────────────────────────────────────
    "Microsoft": {
        "Software Engineer": {
            "must_have": [
                "C#", "C++", "Java", "Python", "Data Structures",
                "Algorithms", "OOP", "System Design", "Azure",
                ".NET", "Git", "REST APIs", "Unit Testing"
            ],
            "good_to_have": [
                "TypeScript", "Kubernetes", "Microservices",
                "DevOps", "GitHub Actions", "PowerShell"
            ],
            "description": "Microsoft engineers work across Office 365, Azure, Teams, Xbox, and more."
        },
        "Cloud Engineer": {
            "must_have": [
                "Azure", "Kubernetes", "Docker", "Terraform",
                "Networking", "Security", "Python", "PowerShell",
                "ARM Templates", "CI/CD", "Monitoring", "IaC"
            ],
            "good_to_have": [
                "AWS", "GCP", "Bicep", "Azure DevOps",
                "Ansible", "Microservices", "Cost Optimization"
            ],
            "description": "Build and manage cloud infrastructure on Azure, the world's second-largest cloud platform."
        },
        "DevOps Engineer": {
            "must_have": [
                "Azure DevOps", "Docker", "Kubernetes", "CI/CD",
                "Git", "Python", "Bash", "Terraform",
                "Monitoring", "Linux", "Release Management"
            ],
            "good_to_have": [
                "GitHub Actions", "Ansible", "Jenkins",
                "Prometheus", "Grafana", "Security Scanning"
            ],
            "description": "Automate and improve engineering pipelines and deployment processes."
        },
        "Data Scientist": {
            "must_have": [
                "Python", "R", "Machine Learning", "Statistics",
                "SQL", "Azure ML", "Pandas", "Scikit-learn",
                "NLP", "Deep Learning", "Data Visualization"
            ],
            "good_to_have": [
                "PyTorch", "TensorFlow", "Power BI",
                "Azure Databricks", "Synapse Analytics", "Responsible AI"
            ],
            "description": "Work on Microsoft Copilot, Bing AI, and internal analytics at scale."
        },
        "Machine Learning Engineer": {
            "must_have": [
                "Python", "PyTorch", "Machine Learning", "MLOps",
                "Azure ML", "Model Deployment", "Docker", "APIs",
                "Statistics", "Data Pipelines", "Git"
            ],
            "good_to_have": [
                "ONNX", "Responsible AI", "LLMs",
                "Kubernetes", "Reinforcement Learning", "Transformers"
            ],
            "description": "Deploy ML at scale to power Azure AI, Bing, and Microsoft Copilot products."
        },
        "Product Manager": {
            "must_have": [
                "Product Roadmap", "Stakeholder Management", "Agile",
                "User Research", "KPIs", "Data Analysis",
                "Competitive Analysis", "Communication", "PRDs"
            ],
            "good_to_have": [
                "SQL", "A/B Testing", "Azure", "Technical Background",
                "OKRs", "Go-to-Market", "JIRA"
            ],
            "description": "Drive vision and strategy for Microsoft products like Teams, Office, and Azure."
        },
        "Azure Engineer": {
            "must_have": [
                "Azure", "Virtual Machines", "Azure Networking",
                "Azure Security", "ARM Templates", "Python", "PowerShell",
                "Azure AD", "Cost Management", "High Availability"
            ],
            "good_to_have": [
                "AZ-900", "AZ-104", "AZ-305", "Kubernetes (AKS)",
                "Terraform", "Azure Functions", "Logic Apps"
            ],
            "description": "Design and manage Azure cloud deployments for enterprise customers."
        },
        "Full Stack Developer": {
            "must_have": [
                "C#", ".NET", "JavaScript", "TypeScript", "React",
                "SQL", "Azure", "REST APIs", "Git", "HTML", "CSS"
            ],
            "good_to_have": [
                "Angular", "Node.js", "Docker",
                "Azure DevOps", "GraphQL", "Testing"
            ],
            "description": "Build full-stack features for Microsoft 365, Teams, and Azure portals."
        },
        "Data Analyst": {
            "must_have": [
                "SQL", "Power BI", "Excel", "Python", "Azure Synapse",
                "Data Visualization", "Statistics", "ETL", "Reporting"
            ],
            "good_to_have": [
                "R", "Tableau", "Azure Data Factory",
                "DAX", "Power Query", "Databricks"
            ],
            "description": "Turn Microsoft's enterprise data into insights using Power BI and Azure tools."
        },
        "UI/UX Designer": {
            "must_have": [
                "Figma", "User Research", "Wireframes", "Prototyping",
                "Fluent Design System", "Accessibility", "Interaction Design",
                "Visual Design", "Usability Testing", "Design Systems"
            ],
            "good_to_have": [
                "Motion Design", "Adobe XD",
                "HTML/CSS basics", "A/B Testing", "WCAG Guidelines"
            ],
            "description": "Design for Microsoft Teams, Office, Windows, and Azure using Fluent Design System."
        }
    },

    # ─────────────────────────────────────────────
    # AMAZON / AWS
    # ─────────────────────────────────────────────
    "Amazon": {
        "Software Engineer": {
            "must_have": [
                "Java", "Python", "C++", "Data Structures",
                "Algorithms", "System Design", "OOP", "REST APIs",
                "AWS", "Git", "Distributed Systems", "Leadership Principles"
            ],
            "good_to_have": [
                "DynamoDB", "S3", "Lambda", "Microservices",
                "Agile", "Kotlin", "Go"
            ],
            "description": "Amazon values Leadership Principles heavily. Behavioral interviews are critical alongside DSA."
        },
        "Backend Developer": {
            "must_have": [
                "Java", "Python", "Node.js", "REST APIs",
                "AWS", "DynamoDB", "S3", "SQS", "Lambda",
                "Microservices", "SQL", "NoSQL", "System Design"
            ],
            "good_to_have": [
                "Kafka", "ElasticSearch", "Redis",
                "CloudFormation", "CDK", "API Gateway"
            ],
            "description": "Build services that handle millions of transactions per day at Amazon scale."
        },
        "Cloud Engineer": {
            "must_have": [
                "AWS", "EC2", "S3", "VPC", "IAM",
                "CloudFormation", "Terraform", "Python",
                "Security", "Networking", "Monitoring (CloudWatch)"
            ],
            "good_to_have": [
                "CDK", "EKS", "Lambda", "AWS Certifications",
                "Cost Optimization", "Well-Architected Framework"
            ],
            "description": "Build on the world's leading cloud platform. AWS certifications are a strong advantage."
        },
        "Data Analyst": {
            "must_have": [
                "SQL", "Python", "Excel", "AWS Redshift",
                "Data Visualization", "Statistics", "QuickSight",
                "ETL", "Data Warehousing", "Business Intelligence"
            ],
            "good_to_have": [
                "Tableau", "Power BI", "Athena",
                "Pandas", "R", "Glue", "A/B Testing"
            ],
            "description": "Analyze data to improve Amazon's customer experience, supply chain, and pricing."
        },
        "Data Scientist": {
            "must_have": [
                "Python", "R", "Machine Learning", "Statistics",
                "SQL", "AWS SageMaker", "Pandas", "Spark",
                "A/B Testing", "Demand Forecasting", "NLP"
            ],
            "good_to_have": [
                "Deep Learning", "PyTorch", "TensorFlow",
                "Hadoop", "AWS Redshift", "Recommendation Systems"
            ],
            "description": "Power Amazon's recommendation engine, Alexa, logistics, and pricing systems."
        },
        "Machine Learning Engineer": {
            "must_have": [
                "Python", "Machine Learning", "AWS SageMaker",
                "PyTorch", "TensorFlow", "Model Deployment",
                "MLOps", "Statistics", "Data Pipelines", "Scikit-learn"
            ],
            "good_to_have": [
                "Spark", "Kubernetes", "Lambda",
                "Deep Learning", "NLP", "Computer Vision", "Bedrock"
            ],
            "description": "Build ML systems for Alexa, search, fraud detection, and logistics optimization."
        },
        "Cloud Solutions Architect": {
            "must_have": [
                "AWS", "Solution Design", "Cloud Architecture",
                "Security", "Networking", "High Availability",
                "Microservices", "Cost Optimization", "Customer Communication"
            ],
            "good_to_have": [
                "AWS Certified Solutions Architect", "Serverless",
                "DevOps", "Migration", "Terraform"
            ],
            "description": "Help enterprise customers design and migrate to AWS at scale."
        },
        "Full Stack Developer": {
            "must_have": [
                "Java", "JavaScript", "React", "Node.js", "Python",
                "AWS", "SQL", "NoSQL", "REST APIs", "Git", "HTML", "CSS"
            ],
            "good_to_have": [
                "TypeScript", "DynamoDB", "Lambda",
                "Docker", "GraphQL", "CI/CD"
            ],
            "description": "Build full-stack features for Amazon's retail, AWS console, and internal tools."
        },
        "DevOps Engineer": {
            "must_have": [
                "AWS", "Docker", "Kubernetes", "CI/CD",
                "Terraform", "Python", "Bash", "Linux",
                "CloudFormation", "Monitoring (CloudWatch)", "Git"
            ],
            "good_to_have": [
                "CDK", "Jenkins", "Ansible",
                "EKS", "GitHub Actions", "Security Scanning"
            ],
            "description": "Build and maintain deployment pipelines for Amazon's massive AWS infrastructure."
        },
        "UI/UX Designer": {
            "must_have": [
                "Figma", "User Research", "Wireframes", "Prototyping",
                "Usability Testing", "Interaction Design", "Visual Design",
                "Design Systems", "Accessibility", "A/B Testing"
            ],
            "good_to_have": [
                "Motion Design", "Adobe XD",
                "HTML/CSS basics", "Customer Journey Mapping"
            ],
            "description": "Design for Amazon.com, AWS Console, Alexa, and Prime — always customer-obsessed."
        },
        "Product Manager": {
            "must_have": [
                "Product Roadmap", "Amazon Leadership Principles",
                "Stakeholder Management", "Agile", "KPIs",
                "User Research", "Data Analysis", "PRDs", "SQL"
            ],
            "good_to_have": [
                "AWS knowledge", "A/B Testing", "OKRs",
                "Go-to-Market", "JIRA", "Technical Background"
            ],
            "description": "Own product direction at Amazon. Leadership Principles are evaluated heavily."
        }
    },

    # ─────────────────────────────────────────────
    # META (Facebook)
    # ─────────────────────────────────────────────
    "Meta": {
        "Software Engineer": {
            "must_have": [
                "Python", "C++", "Java", "Hack/PHP",
                "Data Structures", "Algorithms", "System Design",
                "OOP", "APIs", "Distributed Systems", "Git"
            ],
            "good_to_have": [
                "React", "GraphQL", "Presto",
                "Large-Scale Systems", "Performance Optimization"
            ],
            "description": "Meta focuses heavily on DSA and system design. Speed and scale of 3B+ users is key."
        },
        "Frontend Developer": {
            "must_have": [
                "JavaScript", "TypeScript", "React", "HTML", "CSS",
                "GraphQL", "REST APIs", "Performance Optimization",
                "Accessibility", "Git", "Testing"
            ],
            "good_to_have": [
                "React Native", "Relay", "Webpack",
                "A/B Testing", "Web Security", "Design Systems"
            ],
            "description": "Build features for Facebook, Instagram, WhatsApp — serving billions of users."
        },
        "Backend Developer": {
            "must_have": [
                "Python", "C++", "Java", "PHP/Hack",
                "Distributed Systems", "APIs", "MySQL",
                "NoSQL", "Microservices", "System Design", "Security"
            ],
            "good_to_have": [
                "Kafka", "Presto", "Hive",
                "TAO", "Graph Databases", "Thrift"
            ],
            "description": "Maintain systems handling petabytes of data and billions of requests per day."
        },
        "Data Scientist": {
            "must_have": [
                "Python", "R", "Statistics", "Machine Learning",
                "SQL", "A/B Testing", "Experimentation", "Pandas",
                "Data Analysis", "Causal Inference"
            ],
            "good_to_have": [
                "PyTorch", "Spark", "Presto",
                "Graph Analysis", "NLP", "Deep Learning"
            ],
            "description": "Drive decisions across Meta's products using experimentation and ML at scale."
        },
        "Machine Learning Engineer": {
            "must_have": [
                "Python", "PyTorch", "Deep Learning", "NLP",
                "Computer Vision", "Machine Learning", "Model Deployment",
                "Data Pipelines", "MLOps", "Statistics"
            ],
            "good_to_have": [
                "Recommendation Systems", "Ads Ranking",
                "FAISS", "Transformer Models", "LLMs", "ONNX"
            ],
            "description": "Power Meta AI, Feed ranking, Ads, and content moderation at extreme scale."
        },
        "AR/VR Engineer": {
            "must_have": [
                "C++", "Unity", "Unreal Engine", "3D Graphics",
                "OpenGL/Vulkan", "Computer Vision", "Spatial Computing",
                "Python", "Physics Simulation", "Rendering"
            ],
            "good_to_have": [
                "Hand Tracking", "Oculus SDK", "WebXR",
                "Slam", "Mixed Reality", "Metal/DirectX"
            ],
            "description": "Build the metaverse and AR/VR experiences on Quest and Ray-Ban glasses."
        },
        "Full Stack Developer": {
            "must_have": [
                "JavaScript", "TypeScript", "React", "PHP/Hack",
                "Python", "GraphQL", "SQL", "NoSQL",
                "REST APIs", "Git", "HTML", "CSS"
            ],
            "good_to_have": [
                "Relay", "React Native", "Presto",
                "Docker", "Microservices", "Performance Optimization"
            ],
            "description": "Build end-to-end features for Facebook, Instagram, and WhatsApp at 3B+ user scale."
        },
        "DevOps Engineer": {
            "must_have": [
                "Linux", "Python", "Docker", "Kubernetes",
                "CI/CD", "Git", "Monitoring", "Automation",
                "Networking", "Bash", "Terraform"
            ],
            "good_to_have": [
                "Chef", "Puppet", "Prometheus",
                "Tupperware (Meta internal)", "Scuba", "GitOps"
            ],
            "description": "Keep Meta's infrastructure running at planet scale for billions of daily users."
        },
        "Product Manager": {
            "must_have": [
                "Product Roadmap", "Stakeholder Management", "Agile",
                "User Research", "KPIs", "Data Analysis",
                "A/B Testing", "Communication", "SQL", "PRDs"
            ],
            "good_to_have": [
                "Python basics", "Ad Tech knowledge",
                "Social Media Analytics", "OKRs", "JIRA"
            ],
            "description": "Drive product strategy for Facebook, Instagram, WhatsApp, or Meta AI products."
        },
        "UI/UX Designer": {
            "must_have": [
                "Figma", "User Research", "Wireframes", "Prototyping",
                "Interaction Design", "Visual Design", "Design Systems",
                "Accessibility", "Usability Testing", "A/B Testing"
            ],
            "good_to_have": [
                "Motion Design", "AR/VR Design",
                "HTML/CSS basics", "Adobe XD", "3D Design"
            ],
            "description": "Shape the design of products used by 3 billion people across Facebook, Instagram, and WhatsApp."
        }
    },

    # ─────────────────────────────────────────────
    # APPLE
    # ─────────────────────────────────────────────
    "Apple": {
        "iOS Developer": {
            "must_have": [
                "Swift", "Objective-C", "Xcode", "iOS SDK",
                "UIKit", "SwiftUI", "REST APIs", "Core Data",
                "Auto Layout", "Git", "App Store Publishing"
            ],
            "good_to_have": [
                "Combine", "CoreML", "ARKit",
                "Instruments", "TestFlight", "Accessibility"
            ],
            "description": "Build polished, performant apps for iPhone, iPad, and beyond."
        },
        "Software Engineer": {
            "must_have": [
                "Swift", "C++", "Python", "Data Structures",
                "Algorithms", "System Design", "OOP", "macOS",
                "Git", "APIs", "Performance Optimization"
            ],
            "good_to_have": [
                "Metal", "CoreML", "Rust",
                "Kernel Programming", "Compiler Design"
            ],
            "description": "Apple engineers work on OS, hardware-software integration, privacy features, and apps."
        },
        "Machine Learning Engineer": {
            "must_have": [
                "Python", "CoreML", "TensorFlow", "PyTorch",
                "Machine Learning", "On-Device ML",
                "Model Optimization", "Swift", "Statistics"
            ],
            "good_to_have": [
                "Model Quantization", "Metal Performance Shaders",
                "Privacy-Preserving ML", "Federated Learning", "Create ML"
            ],
            "description": "Build on-device ML for Siri, Face ID, Photos, and Health. Privacy is paramount."
        },
        "UI/UX Designer": {
            "must_have": [
                "Figma", "Sketch", "Apple HIG", "Prototyping",
                "User Research", "Interaction Design", "Visual Design",
                "Accessibility", "Design Systems", "Usability Testing"
            ],
            "good_to_have": [
                "Motion Design", "SwiftUI basics",
                "Hardware Design", "Spatial Design (visionOS)"
            ],
            "description": "Design with Apple's world-class design standards — simplicity and elegance."
        },
        "Hardware Engineer": {
            "must_have": [
                "Circuit Design", "PCB Layout", "Embedded Systems",
                "C", "C++", "Schematic Review", "Silicon Design",
                "Firmware", "Signal Processing", "Testing"
            ],
            "good_to_have": [
                "ARM Architecture", "VLSI", "Custom Silicon (Apple Silicon)",
                "Python scripting", "MATLAB"
            ],
            "description": "Design chips and hardware components for iPhone, Mac, Apple Watch, and more."
        },
        "Full Stack Developer": {
            "must_have": [
                "Swift", "JavaScript", "TypeScript", "React",
                "Node.js", "Python", "REST APIs", "SQL", "Git",
                "macOS/iOS development", "HTML", "CSS"
            ],
            "good_to_have": [
                "GraphQL", "Docker", "SwiftUI",
                "CloudKit", "Xcode", "CI/CD"
            ],
            "description": "Build full-stack tools and services powering Apple's ecosystem — App Store, iCloud, Maps."
        },
        "DevOps Engineer": {
            "must_have": [
                "Linux", "Python", "Bash", "Docker", "Kubernetes",
                "CI/CD", "Git", "Monitoring", "Automation",
                "Terraform", "Security"
            ],
            "good_to_have": [
                "macOS Infrastructure", "Xcode Server",
                "Jenkins", "Ansible", "CloudKit"
            ],
            "description": "Manage Apple's build and deployment infrastructure with an extreme focus on privacy and security."
        },
        "Data Scientist": {
            "must_have": [
                "Python", "Machine Learning", "Statistics",
                "SQL", "Pandas", "CoreML", "Privacy-Preserving ML",
                "Data Analysis", "A/B Testing", "Scikit-learn"
            ],
            "good_to_have": [
                "Federated Learning", "Swift", "On-Device ML",
                "Create ML", "Differential Privacy", "R"
            ],
            "description": "Build privacy-first data science powering Siri, Health, and App Store recommendations."
        },
        "Product Manager": {
            "must_have": [
                "Product Roadmap", "Stakeholder Management",
                "User Research", "KPIs", "Data Analysis",
                "Communication", "PRDs", "Apple HIG knowledge"
            ],
            "good_to_have": [
                "iOS/macOS experience", "A/B Testing",
                "Hardware knowledge", "OKRs", "Go-to-Market"
            ],
            "description": "Drive product direction for iPhone, Mac, services, or developer tools — design and privacy are paramount."
        }
    },

    # ─────────────────────────────────────────────
    # TESLA
    # ─────────────────────────────────────────────
    "Tesla": {
        "Software Engineer": {
            "must_have": [
                "Python", "C++", "Embedded Systems", "Linux",
                "APIs", "Git", "System Design", "Algorithms",
                "Real-Time Systems", "OOP"
            ],
            "good_to_have": [
                "CUDA", "Rust", "CAN Bus",
                "AUTOSAR", "ROS", "Vehicle Systems"
            ],
            "description": "Build software for vehicles, energy systems, Autopilot, and manufacturing."
        },
        "Machine Learning Engineer": {
            "must_have": [
                "Python", "PyTorch", "Deep Learning", "Computer Vision",
                "CUDA", "Model Training", "Data Pipelines",
                "Convolutional Neural Networks", "MLOps", "Statistics"
            ],
            "good_to_have": [
                "Occupancy Networks", "3D Perception",
                "Transformer Models", "Distributed Training",
                "Video Understanding", "ONNX"
            ],
            "description": "Power Autopilot and Full Self-Driving with cutting-edge vision-based ML (no LiDAR)."
        },
        "Autopilot Engineer": {
            "must_have": [
                "Computer Vision", "Deep Learning", "C++",
                "Python", "Sensor Fusion", "CUDA",
                "Real-Time Systems", "Control Systems", "PyTorch"
            ],
            "good_to_have": [
                "Kalman Filters", "Path Planning",
                "3D Object Detection", "Neural Architecture Search"
            ],
            "description": "Build the perception and planning stack for Tesla's FSD system."
        },
        "Robotics Engineer": {
            "must_have": [
                "ROS", "Python", "C++", "Control Systems",
                "Kinematics", "Sensors", "Path Planning",
                "Computer Vision", "Embedded Systems"
            ],
            "good_to_have": [
                "Simulation", "Digital Twins", "Reinforcement Learning",
                "Optimus Robot", "Actuator Control"
            ],
            "description": "Build Tesla Optimus humanoid robot and Gigafactory automation systems."
        },
        "Full Stack Developer": {
            "must_have": [
                "Python", "JavaScript", "React", "Node.js",
                "C++", "REST APIs", "SQL", "Linux", "Git"
            ],
            "good_to_have": [
                "TypeScript", "Docker", "Embedded Linux",
                "Real-Time Systems", "GraphQL"
            ],
            "description": "Build internal tools and customer-facing apps for Tesla's vehicle and energy products."
        },
        "Data Analyst": {
            "must_have": [
                "Python", "SQL", "Data Visualization", "Statistics",
                "Pandas", "Excel", "Manufacturing Analytics", "Reporting"
            ],
            "good_to_have": [
                "Tableau", "Power BI", "Spark",
                "Vehicle Telemetry", "R", "ETL"
            ],
            "description": "Analyze vehicle telemetry, manufacturing, and energy data to drive Tesla's operations."
        },
        "DevOps Engineer": {
            "must_have": [
                "Linux", "Python", "Docker", "Kubernetes",
                "CI/CD", "Terraform", "Git", "Monitoring",
                "Automation", "Bash", "Security"
            ],
            "good_to_have": [
                "AWS", "Ansible", "Jenkins",
                "Embedded CI/CD", "Vehicle OTA Updates"
            ],
            "description": "Build deployment pipelines for Tesla's software-defined vehicle platform."
        }
    },

    # ─────────────────────────────────────────────
    # NETFLIX
    # ─────────────────────────────────────────────
    "Netflix": {
        "Backend Developer": {
            "must_have": [
                "Java", "Python", "Microservices", "AWS",
                "APIs", "Distributed Systems", "Cassandra",
                "Kafka", "System Design", "Git"
            ],
            "good_to_have": [
                "Spinnaker", "Chaos Engineering",
                "Spring Boot", "Eureka", "Hystrix"
            ],
            "description": "Netflix invented chaos engineering. Scale, resilience, and speed matter most."
        },
        "Data Engineer": {
            "must_have": [
                "Python", "Spark", "SQL", "ETL",
                "Kafka", "AWS", "Data Warehousing",
                "Airflow", "Hive", "Iceberg"
            ],
            "good_to_have": [
                "Flink", "Delta Lake", "dbt",
                "Druid", "Presto", "Databricks"
            ],
            "description": "Build pipelines for billions of events per day powering recommendations and analytics."
        },
        "Streaming Platform Engineer": {
            "must_have": [
                "C++", "Video Codecs (H.264/H.265/AV1)",
                "Networking", "CDN", "HTTP/HTTPS",
                "Python", "Java", "Distributed Systems"
            ],
            "good_to_have": [
                "ABR Streaming", "WebRTC",
                "FFmpeg", "Video Quality Metrics", "AWS CloudFront"
            ],
            "description": "Deliver ultra-high-quality video streaming to 260M+ subscribers globally."
        },
        "Machine Learning Engineer": {
            "must_have": [
                "Python", "PyTorch", "Recommendation Systems",
                "Machine Learning", "Spark", "Data Pipelines",
                "A/B Testing", "Statistics", "Scikit-learn"
            ],
            "good_to_have": [
                "Deep Learning", "NLP", "AWS SageMaker",
                "Feature Engineering", "Causal Inference"
            ],
            "description": "Power Netflix's recommendation engine and content discovery."
        },
        "Full Stack Developer": {
            "must_have": [
                "JavaScript", "TypeScript", "React", "Node.js",
                "Java", "REST APIs", "AWS", "SQL", "Git", "HTML", "CSS"
            ],
            "good_to_have": [
                "GraphQL", "Docker", "Microservices",
                "Performance Optimization", "A/B Testing"
            ],
            "description": "Build the Netflix web app, TV apps, and internal tooling at massive scale."
        },
        "DevOps Engineer": {
            "must_have": [
                "AWS", "Docker", "Kubernetes", "Spinnaker",
                "CI/CD", "Python", "Linux", "Terraform",
                "Monitoring", "Chaos Engineering", "Git"
            ],
            "good_to_have": [
                "Atlas (Netflix monitoring)", "Mantis",
                "Jenkins", "Ansible", "Security Scanning"
            ],
            "description": "Support Netflix's world-class deployment pipeline and cloud-native infrastructure."
        },
        "Data Analyst": {
            "must_have": [
                "SQL", "Python", "Presto", "Statistics",
                "Data Visualization", "A/B Testing",
                "Business Intelligence", "Experimentation", "Reporting"
            ],
            "good_to_have": [
                "R", "Tableau", "Spark",
                "Content Analytics", "Pandas", "Causal Inference"
            ],
            "description": "Analyze viewer behavior, content performance, and business metrics to shape Netflix's strategy."
        },
        "Software Engineer": {
            "must_have": [
                "Java", "Python", "Data Structures", "Algorithms",
                "Distributed Systems", "System Design", "APIs",
                "AWS", "Microservices", "Git"
            ],
            "good_to_have": [
                "Chaos Engineering", "Go", "Cassandra",
                "Kafka", "Spring Boot", "Performance Optimization"
            ],
            "description": "Build resilient, high-scale systems for the world's leading streaming platform."
        },
        "Product Manager": {
            "must_have": [
                "Product Roadmap", "Stakeholder Management",
                "User Research", "KPIs", "A/B Testing",
                "Data Analysis", "Communication", "PRDs", "SQL"
            ],
            "good_to_have": [
                "Content Strategy", "Streaming Knowledge",
                "OKRs", "Go-to-Market", "JIRA"
            ],
            "description": "Define product direction for Netflix's streaming experience and recommendation features."
        }
    },

    # ─────────────────────────────────────────────
    # ADOBE
    # ─────────────────────────────────────────────
    "Adobe": {
        "Frontend Developer": {
            "must_have": [
                "JavaScript", "TypeScript", "React", "HTML", "CSS",
                "Adobe Design Systems", "REST APIs", "Accessibility",
                "Performance", "Git", "Web Animation"
            ],
            "good_to_have": [
                "Angular", "Web Components", "GraphQL",
                "Canvas/SVG", "Creative Cloud APIs", "WebGL"
            ],
            "description": "Build tools for millions of creatives on Photoshop, Premiere, and Firefly."
        },
        "UI/UX Designer": {
            "must_have": [
                "Figma", "Adobe XD", "Photoshop", "Illustrator",
                "User Research", "Wireframes", "Prototyping",
                "Design Systems", "Visual Design", "Accessibility"
            ],
            "good_to_have": [
                "After Effects", "Motion Design",
                "Spectrum Design System", "User Testing", "Storyboarding"
            ],
            "description": "Design tools used by designers worldwide. Deep knowledge of Adobe products expected."
        },
        "Machine Learning Engineer": {
            "must_have": [
                "Python", "PyTorch", "Generative AI",
                "Computer Vision", "Diffusion Models",
                "Machine Learning", "Data Pipelines", "Statistics"
            ],
            "good_to_have": [
                "GANs", "Stable Diffusion", "Firefly AI",
                "Content Authenticity", "CLIP", "ControlNet"
            ],
            "description": "Build Adobe Firefly, AI-powered image generation, and creative AI features."
        },
        "Creative Cloud Engineer": {
            "must_have": [
                "C++", "Python", "GPU Programming",
                "Image Processing", "Cross-Platform Development",
                "macOS/Windows APIs", "REST APIs", "Git"
            ],
            "good_to_have": [
                "CUDA", "OpenGL", "Plugin Development",
                "ExtendScript", "UXP Platform"
            ],
            "description": "Build the core Creative Cloud apps: Photoshop, Premiere, Illustrator."
        },
        "Software Engineer": {
            "must_have": [
                "C++", "Java", "Python", "Data Structures",
                "Algorithms", "OOP", "APIs", "Git",
                "System Design", "Cross-Platform Development"
            ],
            "good_to_have": [
                "GPU Programming", "CUDA", "Cloud (AWS/Azure)",
                "Microservices", "Performance Optimization"
            ],
            "description": "Build the software powering Creative Cloud, Document Cloud, and Experience Cloud."
        },
        "Backend Developer": {
            "must_have": [
                "Java", "Python", "Node.js", "REST APIs",
                "SQL", "NoSQL", "Microservices", "AWS",
                "System Design", "Git", "Docker"
            ],
            "good_to_have": [
                "Kafka", "Kubernetes", "GraphQL",
                "CDN", "Security", "Performance Optimization"
            ],
            "description": "Build scalable backend services for Creative Cloud, Acrobat, and Experience Manager."
        },
        "Data Scientist": {
            "must_have": [
                "Python", "Machine Learning", "Statistics",
                "SQL", "Pandas", "Scikit-learn", "A/B Testing",
                "Data Analysis", "Deep Learning"
            ],
            "good_to_have": [
                "PyTorch", "NLP", "Computer Vision",
                "Generative AI", "Spark", "AWS"
            ],
            "description": "Drive AI/ML innovation across Firefly, Acrobat AI Assistant, and Experience Cloud."
        },
        "DevOps Engineer": {
            "must_have": [
                "AWS", "Docker", "Kubernetes", "CI/CD",
                "Terraform", "Python", "Linux", "Git",
                "Monitoring", "Security", "Bash"
            ],
            "good_to_have": [
                "Azure", "Ansible", "Jenkins",
                "Prometheus", "Grafana", "GitHub Actions"
            ],
            "description": "Maintain Adobe's cloud delivery infrastructure for Creative and Document Cloud."
        },
        "Product Manager": {
            "must_have": [
                "Product Roadmap", "Stakeholder Management",
                "User Research", "KPIs", "Data Analysis",
                "Creative Software Knowledge", "PRDs", "Agile"
            ],
            "good_to_have": [
                "A/B Testing", "SQL", "OKRs",
                "Go-to-Market", "Design Background", "JIRA"
            ],
            "description": "Lead product vision for Photoshop, Premiere, Firefly AI, or Acrobat products."
        }
    },

    # ─────────────────────────────────────────────
    # IBM
    # ─────────────────────────────────────────────
    "IBM": {
        "Backend Developer": {
            "must_have": [
                "Java", "Python", "Node.js", "Microservices",
                "IBM Cloud", "REST APIs", "SQL", "NoSQL",
                "Docker", "Kubernetes", "Git", "Security"
            ],
            "good_to_have": [
                "WebSphere", "OpenShift", "MQ",
                "Db2", "Spring Boot", "DevSecOps"
            ],
            "description": "Build enterprise-grade backend solutions across IBM's cloud and AI platform."
        },
        "Cloud Engineer": {
            "must_have": [
                "IBM Cloud", "Kubernetes", "OpenShift",
                "Terraform", "Docker", "Python", "CI/CD",
                "Networking", "Security", "IaC"
            ],
            "good_to_have": [
                "AWS", "Azure", "Ansible",
                "Hybrid Cloud", "IBM Watson", "VMware"
            ],
            "description": "Design hybrid cloud solutions. IBM specializes in enterprise/hybrid environments."
        },
        "Mainframe Developer": {
            "must_have": [
                "COBOL", "z/OS", "JCL", "VSAM",
                "DB2", "CICS", "MQ Series",
                "Batch Processing", "RPG", "REXX"
            ],
            "good_to_have": [
                "Zowe", "IBM ADDI", "Python on z/OS",
                "DevOps for Mainframe", "zCX"
            ],
            "description": "Maintain and modernize mainframe systems powering banks and government globally."
        },
        "Enterprise Architect": {
            "must_have": [
                "TOGAF", "Solution Design", "Cloud Architecture",
                "Security", "Stakeholder Management", "APIs",
                "DevOps", "Microservices", "Presentation Skills"
            ],
            "good_to_have": [
                "ITIL", "SAFe Agile", "IBM Cloud Pak",
                "Digital Transformation", "Cost Optimization"
            ],
            "description": "Lead digital transformation for Fortune 500 companies."
        },
        "Data Scientist": {
            "must_have": [
                "Python", "Machine Learning", "Statistics",
                "IBM Watson", "SQL", "Pandas", "Scikit-learn",
                "Data Analysis", "Deep Learning", "Jupyter"
            ],
            "good_to_have": [
                "AutoAI", "IBM OpenScale", "PyTorch",
                "NLP", "Spark", "Responsible AI"
            ],
            "description": "Build AI solutions using IBM Watson and open-source tools for enterprise clients."
        },
        "Software Engineer": {
            "must_have": [
                "Java", "Python", "C++", "Data Structures",
                "Algorithms", "OOP", "APIs", "Git",
                "IBM Cloud", "Microservices", "Security"
            ],
            "good_to_have": [
                "Go", "OpenShift", "Kubernetes",
                "Quantum Computing basics", "Blockchain"
            ],
            "description": "Build enterprise software across IBM Cloud, Watson, and hybrid cloud products."
        },
        "DevOps Engineer": {
            "must_have": [
                "IBM Cloud", "Docker", "Kubernetes", "OpenShift",
                "CI/CD", "Terraform", "Python", "Bash",
                "Linux", "Monitoring", "Git"
            ],
            "good_to_have": [
                "Ansible", "Jenkins", "Tekton",
                "DevSecOps", "GitHub Actions", "Prometheus"
            ],
            "description": "Automate IBM's enterprise software pipelines using OpenShift and IBM Cloud."
        },
        "Full Stack Developer": {
            "must_have": [
                "Java", "JavaScript", "React", "Node.js",
                "IBM Cloud", "SQL", "REST APIs", "Git",
                "HTML", "CSS", "Docker"
            ],
            "good_to_have": [
                "TypeScript", "Angular", "GraphQL",
                "OpenShift", "DB2", "Microservices"
            ],
            "description": "Build full-stack enterprise applications on IBM Cloud for global clients."
        }
    },

    # ─────────────────────────────────────────────
    # INTEL
    # ─────────────────────────────────────────────
    "Intel": {
        "Software Engineer": {
            "must_have": [
                "C", "C++", "Python", "Assembly",
                "Computer Architecture", "Embedded Systems",
                "Linux", "Git", "Debugging", "Performance Profiling"
            ],
            "good_to_have": [
                "CUDA", "oneAPI", "OpenCL",
                "Driver Development", "BIOS/UEFI", "FPGA"
            ],
            "description": "Build software that pushes the limits of Intel hardware performance."
        },
        "Chip Design Engineer": {
            "must_have": [
                "VLSI", "Verilog", "VHDL", "RTL Design",
                "Logic Synthesis", "Timing Analysis", "EDA Tools",
                "SystemVerilog", "Verification", "ASIC/FPGA"
            ],
            "good_to_have": [
                "UVM", "Formal Verification",
                "Physical Design", "DFT", "Synopsys/Cadence"
            ],
            "description": "Design next-gen Intel processors, GPUs, and AI accelerators."
        },
        "Embedded Systems Engineer": {
            "must_have": [
                "C", "C++", "Embedded Linux", "RTOS",
                "Firmware", "Microcontrollers", "Debugging (JTAG)",
                "I2C", "SPI", "UART", "Hardware Interfaces"
            ],
            "good_to_have": [
                "AUTOSAR", "Yocto", "OpenEmbedded",
                "Power Management", "Security (TEE/TrustZone)"
            ],
            "description": "Build firmware and embedded software for Intel's hardware ecosystem."
        },
        "Hardware Engineer": {
            "must_have": [
                "PCB Design", "Schematic Capture",
                "Signal Integrity", "Power Delivery",
                "Altium/Cadence", "Lab Equipment",
                "DDR", "PCIe", "USB", "EMI/EMC"
            ],
            "good_to_have": [
                "SPICE Simulation", "High-Speed Design",
                "Thermal Analysis", "DFM", "BIOS Validation"
            ],
            "description": "Design hardware platforms for Intel's next-generation processors and platforms."
        },
        "Machine Learning Engineer": {
            "must_have": [
                "Python", "PyTorch", "TensorFlow", "Machine Learning",
                "oneAPI", "OpenVINO", "Model Optimization",
                "Deep Learning", "Data Pipelines", "Statistics"
            ],
            "good_to_have": [
                "ONNX", "Quantization", "Intel Gaudi",
                "Computer Vision", "NLP", "CUDA"
            ],
            "description": "Optimize ML models for Intel CPUs, GPUs, and Gaudi AI accelerators using OpenVINO."
        },
        "Data Scientist": {
            "must_have": [
                "Python", "Machine Learning", "Statistics",
                "SQL", "Pandas", "Scikit-learn",
                "Data Analysis", "Intel Analytics Toolkit"
            ],
            "good_to_have": [
                "oneAPI", "Spark", "Deep Learning",
                "Manufacturing Analytics", "R", "Jupyter"
            ],
            "description": "Use data science to optimize Intel's chip manufacturing, supply chain, and product decisions."
        },
        "DevOps Engineer": {
            "must_have": [
                "Linux", "Python", "Docker", "Kubernetes",
                "CI/CD", "Terraform", "Git", "Monitoring",
                "Automation", "Bash", "Security"
            ],
            "good_to_have": [
                "Ansible", "Jenkins", "Prometheus",
                "GitHub Actions", "OpenShift", "Azure DevOps"
            ],
            "description": "Manage build and deployment pipelines for Intel's software and developer tools."
        },
        "Full Stack Developer": {
            "must_have": [
                "JavaScript", "TypeScript", "React", "Node.js",
                "Python", "SQL", "REST APIs", "Git",
                "HTML", "CSS", "Linux"
            ],
            "good_to_have": [
                "C++", "Docker", "GraphQL",
                "oneAPI", "Microservices", "Performance Optimization"
            ],
            "description": "Build developer tools, internal dashboards, and customer-facing apps for Intel products."
        }
    },

    # ─────────────────────────────────────────────
    # OPENAI
    # ─────────────────────────────────────────────
    "OpenAI": {
        "Machine Learning Engineer": {
            "must_have": [
                "Python", "PyTorch", "Deep Learning", "LLMs",
                "Transformer Models", "CUDA", "Distributed Training",
                "Model Training", "Data Pipelines", "Statistics", "MLOps"
            ],
            "good_to_have": [
                "JAX", "Reinforcement Learning from Human Feedback (RLHF)",
                "Model Fine-Tuning", "Triton", "DeepSpeed", "ONNX"
            ],
            "description": "Train and improve GPT, DALL-E, and Sora models. One of the most competitive ML roles in the world."
        },
        "AI Researcher": {
            "must_have": [
                "Python", "PyTorch", "Deep Learning", "NLP",
                "Research Papers", "Mathematics", "Linear Algebra",
                "Statistics", "Transformer Models", "LLMs", "Publications"
            ],
            "good_to_have": [
                "Reinforcement Learning", "RLHF", "JAX",
                "Multimodal Models", "Safety Research", "PhD preferred"
            ],
            "description": "Push the frontier of AI. Strong publication record and original research required."
        },
        "Software Engineer": {
            "must_have": [
                "Python", "Go", "C++", "Distributed Systems",
                "APIs", "System Design", "Data Structures",
                "Algorithms", "Git", "Cloud (Azure)"
            ],
            "good_to_have": [
                "Kubernetes", "Rust", "CUDA",
                "Large-Scale Infrastructure", "Triton", "OpenAI API"
            ],
            "description": "Build the infrastructure and APIs that power ChatGPT, the OpenAI API, and internal tools."
        },
        "Backend Developer": {
            "must_have": [
                "Python", "Go", "REST APIs", "Distributed Systems",
                "SQL", "NoSQL", "Microservices", "Azure",
                "System Design", "Git", "Security"
            ],
            "good_to_have": [
                "Kubernetes", "Kafka", "Redis",
                "Rate Limiting", "LLM API integration", "gRPC"
            ],
            "description": "Build the backend systems serving billions of ChatGPT and API requests per day."
        },
        "Frontend Developer": {
            "must_have": [
                "JavaScript", "TypeScript", "React", "HTML", "CSS",
                "REST APIs", "GraphQL", "Performance Optimization",
                "Accessibility", "Git"
            ],
            "good_to_have": [
                "Next.js", "WebSockets", "AI/LLM UI patterns",
                "Testing", "Design Systems", "WebAssembly"
            ],
            "description": "Build ChatGPT and the OpenAI Playground — products used by hundreds of millions."
        },
        "Full Stack Developer": {
            "must_have": [
                "Python", "JavaScript", "TypeScript", "React",
                "Node.js", "REST APIs", "SQL", "Git",
                "HTML", "CSS", "Azure"
            ],
            "good_to_have": [
                "Go", "GraphQL", "Docker",
                "LLM integration", "Next.js", "Microservices"
            ],
            "description": "Build full-stack tools and interfaces for OpenAI's products and internal systems."
        },
        "Data Scientist": {
            "must_have": [
                "Python", "Machine Learning", "Statistics",
                "SQL", "Pandas", "Experimentation", "A/B Testing",
                "NLP", "Data Analysis", "LLM Evaluation"
            ],
            "good_to_have": [
                "PyTorch", "Deep Learning", "RLHF",
                "Causal Inference", "Human Feedback Analysis"
            ],
            "description": "Evaluate and improve GPT models using data — from human feedback to large-scale experiments."
        },
        "DevOps Engineer": {
            "must_have": [
                "Azure", "Kubernetes", "Docker", "CI/CD",
                "Terraform", "Python", "Linux", "Monitoring",
                "Security", "Git", "Large-Scale Infrastructure"
            ],
            "good_to_have": [
                "Triton", "GPU cluster management",
                "Ansible", "Prometheus", "GitHub Actions"
            ],
            "description": "Manage the infrastructure that trains and serves the world's most powerful AI models."
        },
        "Product Manager": {
            "must_have": [
                "Product Roadmap", "Stakeholder Management",
                "User Research", "KPIs", "Data Analysis",
                "AI/LLM Product Knowledge", "PRDs", "Communication"
            ],
            "good_to_have": [
                "API Product Experience", "SQL",
                "A/B Testing", "Safety/Ethics awareness", "OKRs"
            ],
            "description": "Shape the future of ChatGPT, the OpenAI API, and enterprise AI products."
        }
    },

    # ─────────────────────────────────────────────
    # NVIDIA
    # ─────────────────────────────────────────────
    "NVIDIA": {
        "Machine Learning Engineer": {
            "must_have": [
                "Python", "CUDA", "PyTorch", "TensorFlow",
                "Deep Learning", "GPU Programming", "Model Optimization",
                "Computer Vision", "Data Pipelines", "Statistics"
            ],
            "good_to_have": [
                "TensorRT", "Triton Inference Server", "ONNX",
                "Quantization", "NLP", "JAX", "Distributed Training"
            ],
            "description": "Optimize deep learning models for NVIDIA GPUs using CUDA and TensorRT."
        },
        "Software Engineer": {
            "must_have": [
                "C++", "CUDA", "Python", "GPU Architecture",
                "Parallel Computing", "Linux", "Git",
                "Data Structures", "Algorithms", "Performance Optimization"
            ],
            "good_to_have": [
                "Rust", "OpenCL", "Vulkan",
                "Driver Development", "Kernel Programming", "Assembly"
            ],
            "description": "Build CUDA libraries, GPU drivers, and tools powering AI and graphics worldwide."
        },
        "AI Researcher": {
            "must_have": [
                "Python", "PyTorch", "CUDA", "Deep Learning",
                "Computer Vision", "NLP", "Research Papers",
                "Mathematics", "Statistics", "GPU Computing"
            ],
            "good_to_have": [
                "Generative AI", "Diffusion Models", "LLMs",
                "JAX", "Reinforcement Learning", "PhD preferred"
            ],
            "description": "Research next-generation AI at NVIDIA — from generative models to autonomous driving."
        },
        "Hardware Engineer": {
            "must_have": [
                "GPU Architecture", "VLSI", "Verilog",
                "RTL Design", "Logic Synthesis", "Timing Analysis",
                "EDA Tools", "SystemVerilog", "PCIe", "Memory Systems"
            ],
            "good_to_have": [
                "Physical Design", "Power Analysis",
                "DFT", "Synopsys/Cadence", "HBM Memory"
            ],
            "description": "Design the next generation of NVIDIA GPUs powering AI, gaming, and data centers."
        },
        "Data Scientist": {
            "must_have": [
                "Python", "Machine Learning", "Statistics",
                "CUDA", "SQL", "Pandas", "Deep Learning",
                "Data Analysis", "RAPIDS (cuDF/cuML)"
            ],
            "good_to_have": [
                "Spark", "Dask", "GPU-accelerated analytics",
                "NLP", "Computer Vision", "R"
            ],
            "description": "Use NVIDIA's own GPU-accelerated data science tools (RAPIDS) to drive product insights."
        },
        "DevOps Engineer": {
            "must_have": [
                "Linux", "Docker", "Kubernetes", "CI/CD",
                "Python", "Terraform", "Git", "GPU cluster management",
                "Monitoring", "Security", "Bash"
            ],
            "good_to_have": [
                "Slurm", "NGC (NVIDIA GPU Cloud)",
                "Ansible", "Prometheus", "GitHub Actions"
            ],
            "description": "Manage NVIDIA's GPU cluster infrastructure and CI/CD pipelines for AI workloads."
        },
        "Full Stack Developer": {
            "must_have": [
                "JavaScript", "TypeScript", "React", "Node.js",
                "Python", "REST APIs", "SQL", "Git",
                "HTML", "CSS", "Linux"
            ],
            "good_to_have": [
                "CUDA basics", "Docker", "GraphQL",
                "GPU Dashboard tools", "Microservices"
            ],
            "description": "Build NVIDIA's developer portals, NGC platform, and internal engineering tools."
        },
        "Embedded Systems Engineer": {
            "must_have": [
                "C", "C++", "Embedded Linux", "CUDA",
                "Jetson Platform", "RTOS", "Firmware",
                "Sensors", "Computer Vision", "Git"
            ],
            "good_to_have": [
                "ROS", "TensorRT", "DeepStream",
                "Automotive (AUTOSAR)", "Camera ISP", "Path Planning"
            ],
            "description": "Build embedded AI systems on NVIDIA Jetson for robotics, autonomous vehicles, and edge computing."
        }
    },

    # ─────────────────────────────────────────────
    # SALESFORCE
    # ─────────────────────────────────────────────
    "Salesforce": {
        "Software Engineer": {
            "must_have": [
                "Java", "Python", "Apex (Salesforce)", "JavaScript",
                "Data Structures", "Algorithms", "OOP",
                "REST APIs", "Git", "System Design", "SQL"
            ],
            "good_to_have": [
                "Salesforce Platform", "Lightning Web Components",
                "Heroku", "MuleSoft", "Tableau CRM", "Kubernetes"
            ],
            "description": "Build CRM features and platform services for the world's #1 customer platform."
        },
        "Salesforce Developer": {
            "must_have": [
                "Apex", "LWC (Lightning Web Components)", "Visualforce",
                "SOQL", "Salesforce Admin", "REST APIs",
                "JavaScript", "Git", "Flows", "Triggers"
            ],
            "good_to_have": [
                "Salesforce Certifications", "Heroku",
                "MuleSoft", "Omnistudio", "CPQ", "Experience Cloud"
            ],
            "description": "Develop custom solutions on Salesforce CRM, Sales Cloud, Service Cloud, and more."
        },
        "Machine Learning Engineer": {
            "must_have": [
                "Python", "Machine Learning", "PyTorch", "NLP",
                "Einstein AI", "Data Pipelines", "MLOps",
                "Statistics", "Model Deployment", "Scikit-learn"
            ],
            "good_to_have": [
                "Salesforce Einstein", "LLMs", "Deep Learning",
                "AWS/GCP", "Feature Engineering", "A/B Testing"
            ],
            "description": "Build Salesforce Einstein AI features that automate sales, service, and marketing workflows."
        },
        "Data Analyst": {
            "must_have": [
                "SQL", "Salesforce Reports & Dashboards", "Tableau",
                "Python", "Excel", "CRM Analytics", "KPIs",
                "Data Visualization", "Business Intelligence"
            ],
            "good_to_have": [
                "Einstein Analytics", "Power BI",
                "Pandas", "R", "SOQL", "ETL"
            ],
            "description": "Analyze CRM data to deliver insights across Salesforce's sales, support, and marketing."
        },
        "Full Stack Developer": {
            "must_have": [
                "JavaScript", "TypeScript", "React", "LWC",
                "Apex", "Node.js", "REST APIs", "SQL",
                "Git", "HTML", "CSS"
            ],
            "good_to_have": [
                "Heroku", "GraphQL", "Docker",
                "Salesforce Platform", "Microservices"
            ],
            "description": "Build Salesforce's web applications across the Customer 360 platform."
        },
        "DevOps Engineer": {
            "must_have": [
                "Salesforce DX", "CI/CD", "Git", "Docker",
                "Kubernetes", "Python", "Bash", "Linux",
                "Terraform", "Monitoring", "Security"
            ],
            "good_to_have": [
                "Copado", "GitHub Actions", "Jenkins",
                "AWS", "Ansible", "Heroku"
            ],
            "description": "Manage Salesforce deployments and DevOps pipelines across global release cycles."
        },
        "Product Manager": {
            "must_have": [
                "Product Roadmap", "CRM Knowledge", "Stakeholder Management",
                "Agile", "KPIs", "User Research", "PRDs",
                "Data Analysis", "Communication"
            ],
            "good_to_have": [
                "Salesforce Platform", "SQL", "A/B Testing",
                "OKRs", "Go-to-Market", "JIRA"
            ],
            "description": "Drive product strategy for Salesforce CRM, Einstein AI, Slack, or Tableau."
        },
        "UI/UX Designer": {
            "must_have": [
                "Figma", "Lightning Design System", "User Research",
                "Wireframes", "Prototyping", "Interaction Design",
                "Visual Design", "Accessibility", "Design Systems"
            ],
            "good_to_have": [
                "Motion Design", "Salesforce Platform",
                "Adobe XD", "Usability Testing", "A/B Testing"
            ],
            "description": "Design Salesforce's CRM interfaces using the Lightning Design System."
        }
    },

    # ─────────────────────────────────────────────
    # UBER
    # ─────────────────────────────────────────────
    "Uber": {
        "Software Engineer": {
            "must_have": [
                "Go", "Python", "Java", "Data Structures",
                "Algorithms", "Distributed Systems", "System Design",
                "Microservices", "REST APIs", "Git"
            ],
            "good_to_have": [
                "Kafka", "Cassandra", "MySQL",
                "Uber's M3/Cadence", "Real-Time Systems", "gRPC"
            ],
            "description": "Build the platform that coordinates millions of rides and food deliveries in real time."
        },
        "Backend Developer": {
            "must_have": [
                "Go", "Python", "Java", "REST APIs",
                "Microservices", "SQL", "NoSQL",
                "Distributed Systems", "Kafka", "Git", "System Design"
            ],
            "good_to_have": [
                "gRPC", "Cassandra", "Redis",
                "Cadence (workflow)", "Real-Time Processing"
            ],
            "description": "Power Uber's core trip, payment, and matching services at planet scale."
        },
        "Machine Learning Engineer": {
            "must_have": [
                "Python", "Machine Learning", "Deep Learning",
                "PyTorch", "Data Pipelines", "Demand Forecasting",
                "ETA Prediction", "Statistics", "MLOps", "Spark"
            ],
            "good_to_have": [
                "Reinforcement Learning", "NLP",
                "Michaelangelo (Uber ML platform)", "Real-Time ML", "A/B Testing"
            ],
            "description": "Build ML models for surge pricing, ETA, fraud detection, and driver-rider matching."
        },
        "Data Scientist": {
            "must_have": [
                "Python", "SQL", "Statistics", "Machine Learning",
                "A/B Testing", "Experimentation", "Pandas",
                "Data Analysis", "Causal Inference", "Spark"
            ],
            "good_to_have": [
                "PyTorch", "Presto", "Hive",
                "Marketplace Analytics", "Causal ML", "R"
            ],
            "description": "Drive decisions across Uber's marketplace, pricing, and product teams."
        },
        "Frontend Developer": {
            "must_have": [
                "JavaScript", "TypeScript", "React", "HTML", "CSS",
                "REST APIs", "Performance Optimization",
                "Accessibility", "Git", "Mobile-first design"
            ],
            "good_to_have": [
                "React Native", "GraphQL", "Next.js",
                "Testing", "Maps/Geolocation", "Design Systems"
            ],
            "description": "Build the Uber app interface used by millions of riders and drivers globally."
        },
        "DevOps Engineer": {
            "must_have": [
                "AWS", "Docker", "Kubernetes", "CI/CD",
                "Terraform", "Python", "Linux", "Monitoring",
                "Git", "Bash", "Large-Scale Infrastructure"
            ],
            "good_to_have": [
                "Spinnaker", "Kafka infrastructure",
                "M3 (Uber monitoring)", "Cadence", "Ansible"
            ],
            "description": "Maintain Uber's global deployment infrastructure handling millions of requests per second."
        },
        "Full Stack Developer": {
            "must_have": [
                "JavaScript", "TypeScript", "React", "Go",
                "Python", "REST APIs", "SQL", "Git",
                "HTML", "CSS", "Microservices"
            ],
            "good_to_have": [
                "GraphQL", "Docker", "Node.js",
                "Maps/Geo APIs", "Real-Time Systems"
            ],
            "description": "Build end-to-end features for Uber's rider, driver, and Eats platforms."
        },
        "Product Manager": {
            "must_have": [
                "Product Roadmap", "Marketplace Knowledge",
                "Stakeholder Management", "Agile", "KPIs",
                "User Research", "Data Analysis", "PRDs", "SQL"
            ],
            "good_to_have": [
                "A/B Testing", "Geospatial Products",
                "Rideshare/Delivery domain", "OKRs", "JIRA"
            ],
            "description": "Own product direction for Uber Rides, Eats, Freight, or the Driver platform."
        }
    },

    # ─────────────────────────────────────────────
    # AIRBNB
    # ─────────────────────────────────────────────
    "Airbnb": {
        "Software Engineer": {
            "must_have": [
                "Java", "Ruby on Rails", "Python", "JavaScript",
                "Data Structures", "Algorithms", "System Design",
                "REST APIs", "SQL", "Git", "Microservices"
            ],
            "good_to_have": [
                "Kotlin", "React", "Airflow",
                "Spark", "Kafka", "Distributed Systems"
            ],
            "description": "Build the platform connecting 4M+ hosts and 150M+ guests across 220 countries."
        },
        "Frontend Developer": {
            "must_have": [
                "JavaScript", "TypeScript", "React", "HTML", "CSS",
                "REST APIs", "Performance Optimization",
                "Accessibility", "Git", "Responsive Design"
            ],
            "good_to_have": [
                "GraphQL", "React Native", "Next.js",
                "Testing", "Design Systems (DLS)", "A/B Testing"
            ],
            "description": "Build Airbnb's beautiful, accessible booking interface used by millions worldwide."
        },
        "Data Scientist": {
            "must_have": [
                "Python", "SQL", "Machine Learning", "Statistics",
                "A/B Testing", "Experimentation", "Pandas",
                "Pricing Models", "Data Analysis", "Causal Inference"
            ],
            "good_to_have": [
                "PyTorch", "Spark", "Airflow",
                "Trust & Safety Analytics", "NLP", "R"
            ],
            "description": "Use data science to optimize Airbnb's pricing, search ranking, and trust systems."
        },
        "Machine Learning Engineer": {
            "must_have": [
                "Python", "Machine Learning", "PyTorch",
                "Search Ranking", "Recommendation Systems",
                "Data Pipelines", "Statistics", "MLOps", "Spark"
            ],
            "good_to_have": [
                "Deep Learning", "NLP", "Trust & Safety ML",
                "Airflow", "Real-Time ML", "A/B Testing"
            ],
            "description": "Build Airbnb's search ranking, smart pricing, and fraud detection ML systems."
        },
        "Backend Developer": {
            "must_have": [
                "Java", "Ruby on Rails", "Python", "REST APIs",
                "SQL", "NoSQL", "Microservices", "System Design",
                "Git", "AWS", "Kafka"
            ],
            "good_to_have": [
                "Kotlin", "GraphQL", "gRPC",
                "Distributed Systems", "Payments", "Redis"
            ],
            "description": "Power Airbnb's booking, payments, messaging, and host management backend services."
        },
        "UI/UX Designer": {
            "must_have": [
                "Figma", "User Research", "Wireframes", "Prototyping",
                "Airbnb Design Language System (DLS)", "Interaction Design",
                "Visual Design", "Usability Testing", "Accessibility"
            ],
            "good_to_have": [
                "Motion Design", "Illustration",
                "HTML/CSS basics", "A/B Testing", "Content Design"
            ],
            "description": "Design one of the world's most beautiful and trusted consumer apps."
        },
        "DevOps Engineer": {
            "must_have": [
                "AWS", "Docker", "Kubernetes", "CI/CD",
                "Terraform", "Python", "Linux", "Monitoring",
                "Git", "Bash", "Security"
            ],
            "good_to_have": [
                "Spinnaker", "Airflow infrastructure",
                "Ansible", "Prometheus", "GitHub Actions"
            ],
            "description": "Maintain Airbnb's AWS-based infrastructure and deployment pipelines."
        },
        "Product Manager": {
            "must_have": [
                "Product Roadmap", "Marketplace Knowledge",
                "Stakeholder Management", "Agile", "KPIs",
                "User Research", "Data Analysis", "PRDs", "SQL"
            ],
            "good_to_have": [
                "A/B Testing", "Travel/Hospitality domain",
                "Trust & Safety", "OKRs", "JIRA"
            ],
            "description": "Shape the Airbnb host or guest experience products — deeply customer-centric culture."
        }
    },

    # ─────────────────────────────────────────────
    # INFOSYS
    # ─────────────────────────────────────────────
    "Infosys": {
        "Software Engineer": {
            "must_have": [
                "Java", "Python", "C++", "Data Structures",
                "Algorithms", "OOP", "REST APIs", "SQL",
                "Git", "Agile", "SDLC"
            ],
            "good_to_have": [
                "Spring Boot", "Microservices", "AWS/Azure",
                "Docker", "Angular", "React"
            ],
            "description": "Develop enterprise software for Infosys clients across banking, retail, and healthcare."
        },
        "Full Stack Developer": {
            "must_have": [
                "Java", "JavaScript", "React", "Angular",
                "Node.js", "SQL", "REST APIs", "Git",
                "HTML", "CSS", "Spring Boot"
            ],
            "good_to_have": [
                "TypeScript", "Docker", "Azure",
                "Microservices", "MongoDB", "CI/CD"
            ],
            "description": "Build full-stack enterprise applications for global Infosys clients."
        },
        "Data Analyst": {
            "must_have": [
                "SQL", "Excel", "Python", "Power BI",
                "Data Visualization", "Statistics",
                "Business Intelligence", "Reporting", "ETL"
            ],
            "good_to_have": [
                "Tableau", "R", "Pandas",
                "Azure Data Factory", "SAP", "SSIS"
            ],
            "description": "Deliver business intelligence and analytics solutions for Infosys enterprise clients."
        },
        "Machine Learning Engineer": {
            "must_have": [
                "Python", "Machine Learning", "TensorFlow",
                "PyTorch", "NLP", "Data Pipelines",
                "Statistics", "Scikit-learn", "SQL", "Git"
            ],
            "good_to_have": [
                "Azure ML", "AWS SageMaker", "MLOps",
                "Deep Learning", "Computer Vision", "Model Deployment"
            ],
            "description": "Build AI/ML solutions for Infosys clients in banking, insurance, and manufacturing."
        },
        "Cloud Engineer": {
            "must_have": [
                "AWS", "Azure", "GCP", "Docker", "Kubernetes",
                "Terraform", "Networking", "Security", "Python",
                "CI/CD", "Linux"
            ],
            "good_to_have": [
                "Cloud Certifications", "Ansible",
                "Cost Optimization", "VMware", "OpenShift"
            ],
            "description": "Design and manage multi-cloud solutions for Infosys's global enterprise clients."
        },
        "DevOps Engineer": {
            "must_have": [
                "Docker", "Kubernetes", "CI/CD", "Jenkins",
                "Git", "Python", "Bash", "Linux",
                "Terraform", "Monitoring", "Ansible"
            ],
            "good_to_have": [
                "AWS DevOps", "Azure DevOps",
                "Prometheus", "Grafana", "GitHub Actions"
            ],
            "description": "Automate CI/CD pipelines and manage infrastructure for Infosys client projects."
        },
        "Business Analyst": {
            "must_have": [
                "Requirements Gathering", "Documentation", "SQL",
                "Stakeholder Management", "Process Mapping",
                "Excel", "Agile", "JIRA", "Use Cases"
            ],
            "good_to_have": [
                "Power BI", "Visio", "BPMN",
                "SAP", "Salesforce", "CBAP certification"
            ],
            "description": "Bridge business and technology for Infosys clients across industries."
        },
        "UI/UX Designer": {
            "must_have": [
                "Figma", "User Research", "Wireframes", "Prototyping",
                "Visual Design", "Interaction Design",
                "Usability Testing", "Design Systems", "Accessibility"
            ],
            "good_to_have": [
                "Adobe XD", "Motion Design",
                "HTML/CSS basics", "Enterprise UX", "A/B Testing"
            ],
            "description": "Design enterprise UX solutions for Infosys client applications across industries."
        }
    },

    # ─────────────────────────────────────────────
    # TCS (Tata Consultancy Services)
    # ─────────────────────────────────────────────
    "TCS": {
        "Software Engineer": {
            "must_have": [
                "Java", "Python", "C++", "Data Structures",
                "Algorithms", "OOP", "REST APIs", "SQL",
                "Git", "Agile", "SDLC"
            ],
            "good_to_have": [
                "Spring Boot", "Microservices", "AWS/Azure",
                "Angular", "React", "Docker"
            ],
            "description": "Build enterprise solutions across TCS's banking, telecom, and manufacturing clients."
        },
        "Full Stack Developer": {
            "must_have": [
                "Java", "JavaScript", "React", "Angular",
                "Node.js", "SQL", "REST APIs", "Git",
                "HTML", "CSS", "Spring Boot"
            ],
            "good_to_have": [
                "TypeScript", "Docker", "Azure",
                "Microservices", "MongoDB", "CI/CD"
            ],
            "description": "Develop and maintain full-stack applications for TCS global clients."
        },
        "Data Analyst": {
            "must_have": [
                "SQL", "Excel", "Python", "Power BI",
                "Data Visualization", "Statistics",
                "Business Intelligence", "Reporting", "ETL"
            ],
            "good_to_have": [
                "Tableau", "R", "Pandas",
                "SSIS", "SAP BW", "Azure Synapse"
            ],
            "description": "Provide analytics and BI solutions to TCS's global enterprise clients."
        },
        "Machine Learning Engineer": {
            "must_have": [
                "Python", "Machine Learning", "TensorFlow",
                "NLP", "Data Pipelines", "Statistics",
                "Scikit-learn", "SQL", "Git", "Jupyter"
            ],
            "good_to_have": [
                "AWS SageMaker", "Azure ML", "Deep Learning",
                "Computer Vision", "MLOps", "PyTorch"
            ],
            "description": "Deliver AI/ML solutions for TCS clients in BFSI, healthcare, and retail."
        },
        "Cloud Engineer": {
            "must_have": [
                "AWS", "Azure", "GCP", "Docker", "Kubernetes",
                "Terraform", "Networking", "Security",
                "Python", "CI/CD", "Linux"
            ],
            "good_to_have": [
                "Cloud Certifications", "VMware",
                "Cost Optimization", "Ansible", "OpenShift"
            ],
            "description": "Implement cloud migration and managed services for TCS's enterprise client base."
        },
        "DevOps Engineer": {
            "must_have": [
                "Jenkins", "Docker", "Kubernetes", "CI/CD",
                "Git", "Python", "Bash", "Linux",
                "Terraform", "Ansible", "Monitoring"
            ],
            "good_to_have": [
                "Azure DevOps", "AWS CodePipeline",
                "Prometheus", "Grafana", "GitHub Actions"
            ],
            "description": "Build and maintain DevOps pipelines for TCS client delivery projects globally."
        },
        "Business Analyst": {
            "must_have": [
                "Requirements Gathering", "Documentation", "SQL",
                "Stakeholder Management", "Process Mapping",
                "Excel", "Agile", "JIRA", "BRD/FSD writing"
            ],
            "good_to_have": [
                "Power BI", "Visio", "BPMN",
                "SAP", "Banking domain", "CBAP"
            ],
            "description": "Analyze and document business requirements for TCS's global client engagements."
        },
        "SAP Consultant": {
            "must_have": [
                "SAP S/4HANA", "SAP ABAP", "SAP FI/CO",
                "SAP MM/SD", "Business Process", "RICEF",
                "SAP Configuration", "SQL", "Client Communication"
            ],
            "good_to_have": [
                "SAP BTP", "SAP Fiori", "S/4HANA Migration",
                "SAP Activate methodology", "ABAP OO"
            ],
            "description": "Implement and customize SAP solutions for TCS's global manufacturing and BFSI clients."
        }
    },

    # ─────────────────────────────────────────────
    # WIPRO
    # ─────────────────────────────────────────────
    "Wipro": {
        "Software Engineer": {
            "must_have": [
                "Java", "Python", "C++", "Data Structures",
                "Algorithms", "OOP", "REST APIs", "SQL",
                "Git", "Agile", "SDLC"
            ],
            "good_to_have": [
                "Spring Boot", "AWS/Azure", "Microservices",
                "Angular", "React", "Docker"
            ],
            "description": "Deliver enterprise software for Wipro's clients in banking, utilities, and healthcare."
        },
        "Full Stack Developer": {
            "must_have": [
                "Java", "JavaScript", "React", "Angular",
                "Node.js", "SQL", "REST APIs", "Git",
                "HTML", "CSS", "Spring Boot"
            ],
            "good_to_have": [
                "TypeScript", "Docker", "Azure",
                "MongoDB", "Microservices", "CI/CD"
            ],
            "description": "Build full-stack applications for Wipro's enterprise clients worldwide."
        },
        "Data Analyst": {
            "must_have": [
                "SQL", "Excel", "Python", "Power BI",
                "Data Visualization", "Statistics",
                "ETL", "Reporting", "Business Intelligence"
            ],
            "good_to_have": [
                "Tableau", "R", "Azure Data Factory",
                "SAP", "SSIS", "Pandas"
            ],
            "description": "Provide analytics solutions for Wipro's global enterprise and government clients."
        },
        "Cloud Engineer": {
            "must_have": [
                "AWS", "Azure", "GCP", "Docker", "Kubernetes",
                "Terraform", "Linux", "Networking", "Security",
                "CI/CD", "Python"
            ],
            "good_to_have": [
                "Cloud Certifications", "Ansible",
                "VMware", "Cost Optimization", "OpenShift"
            ],
            "description": "Manage cloud infrastructure and migration projects for Wipro's enterprise clients."
        },
        "DevOps Engineer": {
            "must_have": [
                "Jenkins", "Docker", "Kubernetes", "CI/CD",
                "Git", "Terraform", "Ansible", "Python",
                "Bash", "Linux", "Monitoring"
            ],
            "good_to_have": [
                "Azure DevOps", "GitHub Actions",
                "Prometheus", "Grafana", "AWS DevOps"
            ],
            "description": "Automate and improve delivery pipelines for Wipro's client engagements."
        },
        "Machine Learning Engineer": {
            "must_have": [
                "Python", "Machine Learning", "TensorFlow",
                "NLP", "Data Pipelines", "Statistics",
                "Scikit-learn", "SQL", "Git"
            ],
            "good_to_have": [
                "AWS SageMaker", "Azure ML", "PyTorch",
                "Deep Learning", "MLOps", "Computer Vision"
            ],
            "description": "Build AI/ML solutions for Wipro clients across BFSI, telecom, and retail sectors."
        },
        "Business Analyst": {
            "must_have": [
                "Requirements Gathering", "Documentation", "SQL",
                "Stakeholder Management", "Process Mapping",
                "Excel", "Agile", "JIRA", "Use Cases"
            ],
            "good_to_have": [
                "Power BI", "Visio", "BPMN",
                "SAP", "Utilities domain", "CBAP"
            ],
            "description": "Gather and analyze business requirements for Wipro's global client programs."
        }
    },

    # ─────────────────────────────────────────────
    # ACCENTURE
    # ─────────────────────────────────────────────
    "Accenture": {
        "Software Engineer": {
            "must_have": [
                "Java", "Python", "JavaScript", "Data Structures",
                "REST APIs", "SQL", "Git", "Agile",
                "OOP", "SDLC", "Communication"
            ],
            "good_to_have": [
                "Spring Boot", "React", "Angular",
                "AWS/Azure", "Docker", "Microservices"
            ],
            "description": "Build and modernize enterprise applications across Accenture's global client base."
        },
        "Full Stack Developer": {
            "must_have": [
                "Java", "JavaScript", "React", "Angular",
                "Node.js", "SQL", "REST APIs", "Git",
                "HTML", "CSS", "Spring Boot"
            ],
            "good_to_have": [
                "TypeScript", "Docker", "Azure",
                "GraphQL", "MongoDB", "CI/CD"
            ],
            "description": "Develop full-stack solutions for Accenture's Fortune 500 clients across industries."
        },
        "Data Analyst": {
            "must_have": [
                "SQL", "Excel", "Python", "Power BI",
                "Data Visualization", "Statistics",
                "ETL", "Reporting", "Tableau"
            ],
            "good_to_have": [
                "R", "Azure Synapse", "SAP",
                "Pandas", "SSIS", "Snowflake"
            ],
            "description": "Deliver data insights and BI solutions for Accenture's consulting engagements."
        },
        "Cloud Engineer": {
            "must_have": [
                "AWS", "Azure", "GCP", "Docker", "Kubernetes",
                "Terraform", "Security", "Networking",
                "Python", "CI/CD", "Linux"
            ],
            "good_to_have": [
                "Cloud Certifications (AWS/Azure/GCP)",
                "Ansible", "VMware", "Cost Optimization", "FinOps"
            ],
            "description": "Design and implement cloud solutions for Accenture's enterprise transformation projects."
        },
        "Machine Learning Engineer": {
            "must_have": [
                "Python", "Machine Learning", "TensorFlow", "PyTorch",
                "NLP", "MLOps", "Data Pipelines", "Statistics",
                "Model Deployment", "AWS/Azure ML", "Git"
            ],
            "good_to_have": [
                "Generative AI", "LLMs", "Computer Vision",
                "Deep Learning", "Responsible AI", "A/B Testing"
            ],
            "description": "Build AI/ML solutions for Accenture's clients, including Generative AI transformation projects."
        },
        "DevOps Engineer": {
            "must_have": [
                "Jenkins", "Docker", "Kubernetes", "CI/CD",
                "Terraform", "Ansible", "Git", "Python",
                "Linux", "Monitoring", "Security"
            ],
            "good_to_have": [
                "Azure DevOps", "GitHub Actions",
                "Prometheus", "Grafana", "AWS DevOps"
            ],
            "description": "Implement DevOps transformations and cloud-native pipelines for Accenture clients."
        },
        "Business Analyst": {
            "must_have": [
                "Requirements Gathering", "Documentation", "SQL",
                "Stakeholder Management", "Process Mapping",
                "Excel", "Agile", "JIRA", "Consulting Skills"
            ],
            "good_to_have": [
                "Power BI", "SAP", "Salesforce",
                "BPMN", "CBAP", "Presentation Skills"
            ],
            "description": "Drive digital transformation for Accenture's clients through business analysis and consulting."
        },
        "UI/UX Designer": {
            "must_have": [
                "Figma", "User Research", "Wireframes", "Prototyping",
                "Visual Design", "Interaction Design",
                "Usability Testing", "Design Systems", "Accessibility"
            ],
            "good_to_have": [
                "Adobe XD", "Motion Design",
                "Service Design", "Enterprise UX", "HTML/CSS basics"
            ],
            "description": "Design enterprise digital experiences for Accenture's clients across industries."
        },
        "SAP Consultant": {
            "must_have": [
                "SAP S/4HANA", "SAP ABAP", "SAP FI/CO",
                "Business Processes", "SAP Configuration",
                "Client Communication", "SQL", "Documentation"
            ],
            "good_to_have": [
                "SAP BTP", "SAP Fiori", "S/4HANA Migration",
                "Agile", "SAP Activate", "ABAP OO"
            ],
            "description": "Implement SAP transformations for Accenture's global enterprise clients."
        }
    },

    # ─────────────────────────────────────────────
    # HCL Technologies
    # ─────────────────────────────────────────────
    "HCL": {
        "Software Engineer": {
            "must_have": [
                "Java", "Python", "C++", "Data Structures",
                "Algorithms", "OOP", "REST APIs", "SQL",
                "Git", "Agile", "SDLC"
            ],
            "good_to_have": [
                "Spring Boot", "AWS/Azure", "Microservices",
                "Angular", "React", "Docker"
            ],
            "description": "Build enterprise IT solutions for HCL's global clients in technology and services."
        },
        "Full Stack Developer": {
            "must_have": [
                "Java", "JavaScript", "React", "Angular",
                "Node.js", "SQL", "REST APIs", "Git",
                "HTML", "CSS", "Spring Boot"
            ],
            "good_to_have": [
                "TypeScript", "Docker", "Azure",
                "MongoDB", "Microservices", "CI/CD"
            ],
            "description": "Develop full-stack applications for HCL's technology product and services divisions."
        },
        "Cloud Engineer": {
            "must_have": [
                "AWS", "Azure", "GCP", "Docker", "Kubernetes",
                "Terraform", "Networking", "Security",
                "Python", "CI/CD", "Linux"
            ],
            "good_to_have": [
                "Cloud Certifications", "Ansible",
                "VMware", "OpenShift", "Cost Optimization"
            ],
            "description": "Design and deliver cloud infrastructure for HCL's enterprise clients globally."
        },
        "DevOps Engineer": {
            "must_have": [
                "Jenkins", "Docker", "Kubernetes", "CI/CD",
                "Git", "Terraform", "Ansible", "Python",
                "Linux", "Bash", "Monitoring"
            ],
            "good_to_have": [
                "Azure DevOps", "GitHub Actions",
                "Prometheus", "Grafana", "AWS CodePipeline"
            ],
            "description": "Build and manage DevOps pipelines for HCL's software products and client projects."
        },
        "Data Analyst": {
            "must_have": [
                "SQL", "Excel", "Python", "Power BI",
                "Data Visualization", "Statistics",
                "ETL", "Reporting", "Business Intelligence"
            ],
            "good_to_have": [
                "Tableau", "R", "SAP",
                "Azure Data Factory", "SSIS", "Snowflake"
            ],
            "description": "Provide analytics and reporting solutions for HCL's global client engagements."
        },
        "Machine Learning Engineer": {
            "must_have": [
                "Python", "Machine Learning", "TensorFlow",
                "NLP", "Data Pipelines", "Statistics",
                "Scikit-learn", "SQL", "Git"
            ],
            "good_to_have": [
                "AWS SageMaker", "Azure ML", "PyTorch",
                "Deep Learning", "MLOps", "Computer Vision"
            ],
            "description": "Build AI and analytics solutions for HCL's clients in BFSI, telecom, and manufacturing."
        },
        "Business Analyst": {
            "must_have": [
                "Requirements Gathering", "Documentation", "SQL",
                "Stakeholder Management", "Process Mapping",
                "Excel", "Agile", "JIRA", "Use Cases"
            ],
            "good_to_have": [
                "Power BI", "Visio", "BPMN",
                "SAP", "CBAP", "Presentation Skills"
            ],
            "description": "Analyze and document requirements for HCL's global technology services and product teams."
        }
    },

    # ─────────────────────────────────────────────
    # GENERIC (for custom companies)
    # ─────────────────────────────────────────────
    "Generic": {
        "Software Engineer": {
            "must_have": ["Python", "Java", "Data Structures", "Algorithms", "OOP", "APIs", "Git", "System Design"],
            "good_to_have": ["Cloud", "Microservices", "Testing", "CI/CD", "Agile"],
            "description": "General software engineer position."
        },
        "Frontend Developer": {
            "must_have": ["HTML", "CSS", "JavaScript", "React", "REST APIs", "Git", "Responsive Design"],
            "good_to_have": ["TypeScript", "Vue.js", "Testing", "Performance Optimization"],
            "description": "General frontend developer position."
        },
        "Backend Developer": {
            "must_have": ["Python", "Java", "Node.js", "APIs", "SQL", "NoSQL", "System Design", "Git"],
            "good_to_have": ["Docker", "Kubernetes", "Cloud", "Microservices", "Security"],
            "description": "General backend developer position."
        },
        "Full Stack Developer": {
            "must_have": ["HTML", "CSS", "JavaScript", "React", "Node.js", "SQL", "APIs", "Git"],
            "good_to_have": ["TypeScript", "Docker", "Cloud", "Testing", "CI/CD"],
            "description": "General full stack developer position."
        },
        "Data Analyst": {
            "must_have": ["SQL", "Excel", "Python", "Data Visualization", "Statistics", "Business Intelligence"],
            "good_to_have": ["Power BI", "Tableau", "Pandas", "R", "ETL"],
            "description": "General data analyst position."
        },
        "Data Scientist": {
            "must_have": ["Python", "Machine Learning", "Statistics", "SQL", "Pandas", "Scikit-learn", "Data Analysis"],
            "good_to_have": ["Deep Learning", "NLP", "Spark", "TensorFlow", "Cloud"],
            "description": "General data scientist position."
        },
        "Machine Learning Engineer": {
            "must_have": ["Python", "TensorFlow", "PyTorch", "Machine Learning", "Model Deployment", "Statistics", "Data Pipelines"],
            "good_to_have": ["MLOps", "Kubernetes", "Docker", "Cloud", "NLP", "Computer Vision"],
            "description": "General machine learning engineer position."
        },
        "DevOps Engineer": {
            "must_have": ["Docker", "Kubernetes", "CI/CD", "Linux", "Python", "Git", "Monitoring"],
            "good_to_have": ["Terraform", "Ansible", "AWS", "Prometheus", "Security"],
            "description": "General DevOps engineer position."
        },
        "Cloud Engineer": {
            "must_have": ["AWS/Azure/GCP", "Kubernetes", "Docker", "Terraform", "Networking", "Security", "IaC"],
            "good_to_have": ["Cost Optimization", "Monitoring", "CI/CD", "Python"],
            "description": "General cloud engineer position."
        },
        "UI/UX Designer": {
            "must_have": ["Figma", "User Research", "Wireframes", "Prototyping", "Visual Design", "Accessibility"],
            "good_to_have": ["Adobe XD", "Design Systems", "Usability Testing", "Motion Design"],
            "description": "General UI/UX designer position."
        },
        "Product Manager": {
            "must_have": ["Product Roadmap", "Stakeholders", "Agile", "KPIs", "User Research", "Data Analysis"],
            "good_to_have": ["SQL", "A/B Testing", "JIRA", "Go-to-Market", "OKRs"],
            "description": "General product manager position."
        },
        "Business Analyst": {
            "must_have": ["Requirements Gathering", "Documentation", "SQL", "Stakeholder Management", "Process Mapping", "Excel"],
            "good_to_have": ["JIRA", "Agile", "Power BI", "Visio", "BPMN"],
            "description": "General business analyst position."
        }
    }
}


def get_job_info(company: str, role: str) -> dict:
    """
    Returns the job requirements for a given company and role.
    Falls back to Generic if company not found.
    Falls back to the closest generic role if specific role not found.
    """
    # Try exact company match
    company_data = job_database.get(company)

    if not company_data:
        # Try case-insensitive match
        for key in job_database:
            if key.lower() == company.lower():
                company_data = job_database[key]
                break

    if not company_data:
        company_data = job_database["Generic"]

    # Try exact role match
    role_data = company_data.get(role)

    if not role_data:
        # Try case-insensitive match
        for key in company_data:
            if key.lower() == role.lower():
                role_data = company_data[key]
                break

    if not role_data:
        # Fall back to Generic role
        role_data = job_database["Generic"].get(role)

    if not role_data:
        # Fall back to Generic Software Engineer
        role_data = job_database["Generic"]["Software Engineer"]

    return role_data


def get_all_keywords(company: str, role: str) -> list:
    """Returns combined must_have + good_to_have keywords for ATS matching."""
    info = get_job_info(company, role)
    return info.get("must_have", []) + info.get("good_to_have", [])


def get_must_have_keywords(company: str, role: str) -> list:
    """Returns only critical must-have keywords."""
    info = get_job_info(company, role)
    return info.get("must_have", [])


def get_available_roles(company: str) -> list:
    """Returns list of roles available for a company."""
    company_data = job_database.get(company, job_database["Generic"])
    return list(company_data.keys())


def get_available_companies() -> list:
    """Returns all companies in the database."""
    return [c for c in job_database.keys() if c != "Generic"]