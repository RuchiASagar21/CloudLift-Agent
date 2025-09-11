# CloudLift-Agent
CloudLift Agent is an AWS Bedrock AgentCore–powered migration copilot that parses on-prem inventory, proposes target AWS architectures with cost estimates, generates Terraform, and orchestrates a dry-run migration workflow (provision → validate → report) via Step Functions. It’s reproducible, auditable, and designed for safe, low-cost demos.

Compute mapping:

≤1 vCPU / ≤2 GB → t3.nano

2 vCPU / 4 GB → t3.micro or t3.small (pick one and stick to it)

DB mapping: postgres → RDS Postgres (db.t4g.micro), mysql → RDS MySQL (db.t4g.micro), sqlite → mock/skip

Storage: one S3 bucket per app: cloudlift-demo-<app>

Region/AZ: us-east-1, single AZ for the demo

Budget guardrail: fail plan if estimated monthly > $75/app

Default mode: dry-run unless a provision=true flag is given
